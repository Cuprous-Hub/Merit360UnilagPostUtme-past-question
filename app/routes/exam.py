from unittest import result

from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from datetime import datetime, timedelta
from app import db
from app.models.exam import Exam, Question, Result, Answer, Topic
from app.models.user import User
from sqlalchemy import desc, func
import random

exam_bp = Blueprint('exam', __name__)

@exam_bp.route('/exam/<int:exam_id>')
@login_required
def view_exam(exam_id):
    exam = Exam.query.get_or_404(exam_id)
    user_results = Result.query.filter_by(user_id=current_user.id, exam_id=exam_id).all()
    return render_template('exam/view_exam.html', exam=exam, user_results=user_results)

@exam_bp.route('/exam/<int:exam_id>/start')
@login_required
def start_exam(exam_id):
    exam = Exam.query.get_or_404(exam_id)
    result = Result(user_id=current_user.id, exam_id=exam_id, started_at=datetime.utcnow())
    db.session.add(result)
    db.session.commit()
    return redirect(url_for('exam.take_exam', exam_id=exam_id, result_id=result.id))

@exam_bp.route('/exam/<int:exam_id>/take/<int:result_id>')
@login_required
def take_exam(exam_id, result_id):
    exam = Exam.query.get_or_404(exam_id)
    result = Result.query.get_or_404(result_id)
    if result.user_id != current_user.id:
        flash('You do not have permission to take this exam.', 'error')
        return redirect(url_for('main.dashboard'))
    if result.completed_at:
        flash('This exam has already been completed.', 'info')
        return redirect(url_for('exam.view_exam', exam_id=exam_id))
    questions = Question.query.filter_by(exam_id=exam_id).order_by(Question.question_order).all()
    return render_template('exam/take_exam.html', exam=exam, result=result, questions=questions)

@exam_bp.route('/api/exam/<int:exam_id>/submit-answer', methods=['POST'])
@login_required
def submit_answer(exam_id):
    data = request.get_json()
    result_id = data.get('result_id')
    question_id = data.get('question_id')
    user_answer = data.get('answer')
    result = Result.query.get_or_404(result_id)
    question = Question.query.get_or_404(question_id)
    if result.user_id != current_user.id or question.exam_id != exam_id:
        return jsonify({'error': 'Unauthorized'}), 403
    existing_answer = Answer.query.filter_by(result_id=result_id, question_id=question_id).first()
    is_correct = user_answer == question.correct_answer
    score = question.marks if is_correct else 0
    if existing_answer:
        existing_answer.user_answer = user_answer
        existing_answer.is_correct = is_correct
        existing_answer.score_obtained = score
    else:
        answer = Answer(
            result_id=result_id,
            question_id=question_id,
            user_answer=user_answer,
            is_correct=is_correct,
            score_obtained=score
        )
        db.session.add(answer)
    db.session.commit()
    return jsonify({'success': True, 'is_correct': is_correct})

@exam_bp.route('/exam/<int:exam_id>/submit/<int:result_id>', methods=['POST'])
@login_required
def submit_exam(exam_id, result_id):
    exam = Exam.query.get_or_404(exam_id)
    result = Result.query.get_or_404(result_id)
    if result.user_id != current_user.id:
        flash('You do not have permission to submit this exam.', 'error')
        return redirect(url_for('main.dashboard'))
    answers = Answer.query.filter_by(result_id=result_id).all()
    total_score = sum(a.score_obtained for a in answers)
    questions = Question.query.filter_by(exam_id=exam_id).all()
    total_marks = sum(q.marks for q in questions)
    percentage = (total_score / total_marks * 100) if total_marks > 0 else 0
    is_passed = percentage >= exam.passing_score
    result.completed_at = datetime.utcnow()
    result.total_score = total_score
    result.percentage = percentage
    result.is_passed = is_passed
    result.time_taken_seconds = int((result.completed_at - result.started_at).total_seconds())
    db.session.commit()
    return redirect(url_for('exam.view_result', exam_id=exam_id, result_id=result_id))

@exam_bp.route('/exam/<int:exam_id>/result/<int:result_id>')
@login_required
def view_result(exam_id, result_id):
    exam = Exam.query.get_or_404(exam_id)
    result = Result.query.get_or_404(result_id)
    if result.user_id != current_user.id:
        flash('You do not have permission to view this result.', 'error')
        return redirect(url_for('main.dashboard'))
    answers = Answer.query.filter_by(result_id=result_id).all()
    total_marks = sum(q.marks for q in exam.questions)
    return render_template('exam/result.html', exam=exam, result=result, answers=answers, total_marks=total_marks)


# ============ FEATURE 1: EXAM MODE ============

@exam_bp.route('/exam-mode')
@login_required
def exam_mode_home():
    return render_template('exam/exam_mode.html')


@exam_bp.route('/exam-mode/start', methods=['POST'])
@login_required
def exam_mode_start():
    subjects = ['Mathematics', 'English', 'General Paper']
    # UNILAG Post-UTME format: 30 questions total (English:15, Math:12, General Paper:3)
    subjects_config = [('English', 15), ('Mathematics', 12), ('General Paper', 3)]
    all_questions = []
    for subject in subjects:
    for subject, count in subjects_config:
        questions = Question.query.filter_by(subject=subject).all()
        if subject == 'Mathematics':
            all_questions.extend(random.sample(questions, min(20, len(questions))))
        elif subject == 'English':
            all_questions.extend(random.sample(questions, min(15, len(questions))))
        else:
            all_questions.extend(random.sample(questions, min(5, len(questions))))
    if len(all_questions) >= 40:
        all_questions = random.sample(all_questions, 40)
        if questions:
            all_questions.extend(random.sample(questions, min(count, len(questions))))
    if len(all_questions) > 30:
        all_questions = random.sample(all_questions, 30)
    if not all_questions:
        return jsonify({'error': 'No questions available'}), 400
    exam = Exam.query.filter_by(title='Full Exam').first()
    if not exam:
        exam = Exam.query.filter_by(subject='English').first()
    if not exam:
        return jsonify({'error': 'No exam found'}), 400
    result = Result(
        user_id=current_user.id,
        exam_id=exam.id if exam else 1,
        exam_mode='full_exam',
        selected_subjects='Mathematics,English,General Paper',
        num_questions_allowed=40,
        num_questions_allowed=30,
        time_limit_minutes=30,
        passing_score=30,
        passing_score=18,
        started_at=datetime.utcnow()
    )
    db.session.add(result)
    db.session.commit()
    for q in all_questions:
        existing = Answer.query.filter_by(result_id=result.id, question_id=q.id).first()
        if not existing:
            placeholder = Answer(
                result_id=result.id,
                question_id=q.id,
                user_answer=None,
                is_correct=False,
                score_obtained=0
            )
            db.session.add(placeholder)
    db.session.commit()
    return jsonify({'success': True, 'redirect': url_for('exam.exam_mode_take', result_id=result.id)})


@exam_bp.route('/exam-mode/take/<int:result_id>')
@login_required
def exam_mode_take(result_id):
    result = Result.query.get_or_404(result_id)
    if result.user_id != current_user.id:
        flash('Unauthorized access.', 'error')
        return redirect(url_for('main.dashboard'))
    if result.completed_at:
        flash('This exam has already been completed.', 'info')
        return redirect(url_for('exam.exam_mode_result', result_id=result_id))
    answers = Answer.query.filter_by(result_id=result_id).all()
    question_ids = [a.question_id for a in answers]
    questions = Question.query.filter(Question.id.in_(question_ids)).all()
    answered_question_ids = [a.question_id for a in answers if a.user_answer is not None]
    return render_template('exam/exam_mode_take.html', result=result, questions=questions, answered_ids=answered_question_ids)


@exam_bp.route('/exam-mode/result/<int:result_id>')
@login_required
def exam_mode_result(result_id):
    result = Result.query.get_or_404(result_id)
    if result.user_id != current_user.id:
        flash('Unauthorized access.', 'error')
        return redirect(url_for('main.dashboard'))
    answers = Answer.query.filter_by(result_id=result_id).all()
    total_marks = 40
    total_marks = 30
    return render_template('exam/exam_mode_result.html', result=result, answers=answers, total_marks=total_marks)


@exam_bp.route('/api/exam-mode/<int:result_id>/submit-answer', methods=['POST'])
@login_required
def exam_mode_submit_answer(result_id):
    data = request.get_json()
    result = Result.query.get_or_404(result_id)
    question_id = data.get('question_id')
    user_answer = data.get('answer')
    if result.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    question = Question.query.get_or_404(question_id)
    existing_answer = Answer.query.filter_by(result_id=result_id, question_id=question_id).first()
    is_correct = user_answer == question.correct_answer
    score = question.marks if is_correct else 0
    if existing_answer:
        existing_answer.user_answer = user_answer
        existing_answer.is_correct = is_correct
        existing_answer.score_obtained = score
    else:
        answer = Answer(
            result_id=result_id,
            question_id=question_id,
            user_answer=user_answer,
            is_correct=is_correct,
            score_obtained=score
        )
        db.session.add(answer)
    db.session.commit()
    return jsonify({'success': True, 'is_correct': is_correct})


@exam_bp.route('/api/exam-mode/<int:result_id>/finish', methods=['POST'])
@login_required
def exam_mode_finish(result_id):
    result = Result.query.get_or_404(result_id)
    if result.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    answers = Answer.query.filter_by(result_id=result_id).all()
    total_score = sum(a.score_obtained for a in answers)
    result.completed_at = datetime.utcnow()
    result.total_score = total_score
    result.percentage = (total_score / 40 * 100)
    result.percentage = (total_score / 30 * 100)
    result.is_passed = result.total_score >= result.passing_score
    result.is_graded = True
    result.time_taken_seconds = int((result.completed_at - result.started_at).total_seconds())
    db.session.commit()
    return jsonify({'success': True, 'redirect': url_for('exam.exam_mode_result', result_id=result_id)})


# ============ FEATURE 2: PRACTICE MODE ============

@exam_bp.route('/practice-mode')
@login_required
def practice_mode_home():
    topics = Topic.query.all()
    subjects = db.session.query(Topic.subject).distinct().all()
    subjects = [s[0] for s in subjects]
    return render_template('exam/practice_mode.html', subjects=subjects, topics=topics)


@exam_bp.route('/practice-mode/subjects')
@login_required
def practice_mode_subjects():
    subject = request.args.get('subject')
    topics = Topic.query.filter_by(subject=subject).all()
    return jsonify({
        'topics': [{'id': t.id, 'name': t.name, 'description': t.description} for t in topics]
    })


@exam_bp.route('/practice-mode/start/<int:topic_id>', methods=['POST'])
@login_required
def practice_mode_start(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    questions = Question.query.filter_by(topic_id=topic_id).all()
    if not questions:
        return jsonify({'error': 'No questions available for this topic'}), 404
    exam = Exam.query.first()
    result = Result(
        user_id=current_user.id,
        exam_id=exam.id if exam else 1,
        exam_mode='practice_topic',
        selected_topic_id=topic_id,
        num_questions_allowed=len(questions),
        time_limit_minutes=None,
        passing_score=0,
        is_graded=False,
        started_at=datetime.utcnow()
    )
    db.session.add(result)
    db.session.commit()
    return jsonify({'success': True, 'result_id': result.id, 'redirect': url_for('exam.practice_mode_take', result_id=result.id)})


@exam_bp.route('/practice-mode/take/<int:result_id>')
@login_required
def practice_mode_take(result_id):
    result = Result.query.get_or_404(result_id)
    if result.user_id != current_user.id:
        flash('Unauthorized access.', 'error')
        return redirect(url_for('main.dashboard'))
    questions = Question.query.filter_by(topic_id=result.selected_topic_id).all()
    answered_ids = [a.question_id for a in result.answers]
    return render_template('exam/practice_mode_take.html', result=result, questions=questions, answered_ids=answered_ids)


@exam_bp.route('/practice-mode/result/<int:result_id>')
@login_required
def practice_mode_result(result_id):
    result = Result.query.get_or_404(result_id)
    if result.user_id != current_user.id:
        flash('Unauthorized access.', 'error')
        return redirect(url_for('main.dashboard'))
    if not result.completed_at:
        answers = Answer.query.filter_by(result_id=result_id).all()
        total_score = sum(a.score_obtained for a in answers)
        total_questions = len(answers)
        result.completed_at = datetime.utcnow()
        result.total_score = total_score
        result.percentage = (total_score / total_questions * 100) if total_questions > 0 else 0
        result.time_taken_seconds = int((result.completed_at - result.started_at).total_seconds())
        db.session.commit()
    answers = Answer.query.filter_by(result_id=result_id).all()
    return render_template('exam/practice_mode_result.html', result=result, answers=answers)


@exam_bp.route('/api/practice-mode/<int:result_id>/submit-answer', methods=['POST'])
@login_required
def practice_mode_submit_answer(result_id):
    data = request.get_json()
    result = Result.query.get_or_404(result_id)
    question_id = data.get('question_id')
    user_answer = data.get('answer')
    if result.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    question = Question.query.get_or_404(question_id)
    existing_answer = Answer.query.filter_by(result_id=result_id, question_id=question_id).first()
    is_correct = user_answer == question.correct_answer
    score = question.marks if is_correct else 0
    if existing_answer:
        existing_answer.user_answer = user_answer
        existing_answer.is_correct = is_correct
        existing_answer.score_obtained = score
    else:
        answer = Answer(
            result_id=result_id,
            question_id=question_id,
            user_answer=user_answer,
            is_correct=is_correct,
            score_obtained=score
        )
        db.session.add(answer)
    db.session.commit()
    return jsonify({'success': True, 'is_correct': is_correct, 'explanation': question.explanation})


# ============ FEATURE 3: LEADERBOARD ============

@exam_bp.route('/leaderboard')
@login_required
def leaderboard():
    top_results = Result.query.filter_by(exam_mode='full_exam', is_graded=True)\
        .order_by(desc(Result.total_score))\
        .limit(50).all()
    user_best = Result.query.filter_by(
        user_id=current_user.id,
        exam_mode='full_exam',
        is_graded=True
    ).order_by(desc(Result.total_score)).first()
    user_rank = db.session.query(func.count(Result.id)).filter(
        Result.exam_mode == 'full_exam',
        Result.is_graded == True,
        Result.total_score > (user_best.total_score if user_best else 0)
    ).scalar() + 1
    return render_template('exam/leaderboard.html', top_results=top_results, user_rank=user_rank)
    return render_template('exam/leaderboard.html', top_results=top_results, user_rank=user_rank)

# ============ FEATURE 4: TOURNAMENT MODE ============
# Opens Saturday & Sunday only. Fee: ₦500 to Zenith Bank 4315395322, Atode Excellence Samuel
# Payment generates a one-time access code stored in the TournamentEntry model.

import secrets
import string
from app.models.exam import TournamentEntry  # add this model to models/exam.py

TOURNAMENT_BANK_NAME = "Atode Excellence Samuel"
TOURNAMENT_BANK_ACCOUNT = "4315395322"
TOURNAMENT_BANK = "Zenith Bank"
TOURNAMENT_FEE = 500


def is_tournament_open():
    """Tournament runs on Saturdays (5) and Sundays (6) only."""
    return datetime.utcnow().weekday() in (5, 6)


def generate_tournament_code():
    """Generate a unique 8-character alphanumeric access code."""
    alphabet = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(secrets.choice(alphabet) for _ in range(8))
        if not TournamentEntry.query.filter_by(access_code=code).first():
            return code


@exam_bp.route('/tournament')
@login_required
def tournament_home():
    open_today = is_tournament_open()
    day_name = datetime.utcnow().strftime('%A')
    # Check if user already has a valid unused entry for today
    today_start = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    existing_entry = TournamentEntry.query.filter(
        TournamentEntry.user_id == current_user.id,
        TournamentEntry.created_at >= today_start,
        TournamentEntry.is_used == False
    ).first()
    user_result = Result.query.filter_by(
        user_id=current_user.id,
        exam_mode='tournament'
    ).order_by(desc(Result.started_at)).first()
    # Leaderboard: top 20 tournament scores this week
    week_start = datetime.utcnow() - timedelta(days=datetime.utcnow().weekday())
    top_results = Result.query.filter(
        Result.exam_mode == 'tournament',
        Result.is_graded == True,
        Result.started_at >= week_start
    ).order_by(desc(Result.total_score)).limit(20).all()
    return render_template('exam/tournament.html',
        open_today=open_today,
        day_name=day_name,
        existing_entry=existing_entry,
        user_result=user_result,
        top_results=top_results,
        bank_name=TOURNAMENT_BANK_NAME,
        bank_account=TOURNAMENT_BANK_ACCOUNT,
        bank=TOURNAMENT_BANK,
        fee=TOURNAMENT_FEE
    )


@exam_bp.route('/tournament/verify-code', methods=['POST'])
@login_required
def tournament_verify_code():
    """User enters their access code to join the tournament."""
    if not is_tournament_open():
        flash('Tournament is only available on Saturdays and Sundays!', 'error')
        return redirect(url_for('exam.tournament_home'))
    code = request.form.get('access_code', '').strip().upper()
    if not code:
        flash('Please enter your access code.', 'error')
        return redirect(url_for('exam.tournament_home'))
    entry = TournamentEntry.query.filter_by(access_code=code, is_used=False).first()
    if not entry:
        flash('Invalid or already used access code. Please check and try again.', 'error')
        return redirect(url_for('exam.tournament_home'))
    # Mark code as used and link to this user
    entry.is_used = True
    entry.user_id = current_user.id
    entry.used_at = datetime.utcnow()
    db.session.commit()
    flash('Access code verified! Starting your tournament...', 'success')
    return redirect(url_for('exam.tournament_start'))


@exam_bp.route('/tournament/start')
@login_required
def tournament_start():
    """Start the tournament exam session."""
    if not is_tournament_open():
        flash('Tournament is only available on Saturdays and Sundays!', 'error')
        return redirect(url_for('exam.tournament_home'))
    # Check user has verified entry today
    today_start = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    entry = TournamentEntry.query.filter(
        TournamentEntry.user_id == current_user.id,
        TournamentEntry.used_at >= today_start,
        TournamentEntry.is_used == True
    ).first()
    if not entry:
        flash('You need a valid access code to enter the tournament.', 'error')
        return redirect(url_for('exam.tournament_home'))
    # Build 30-question set (same Post-UTME format)
    subjects_config = [('English', 15), ('Mathematics', 12), ('General Paper', 3)]
    all_questions = []
    for subject, count in subjects_config:
        questions = Question.query.filter_by(subject=subject).all()
        if questions:
            all_questions.extend(random.sample(questions, min(count, len(questions))))
    if len(all_questions) > 30:
        all_questions = random.sample(all_questions, 30)
    if not all_questions:
        flash('No questions available for tournament.', 'error')
        return redirect(url_for('exam.tournament_home'))
    exam = Exam.query.filter_by(title='Full Exam').first()
    if not exam:
        exam = Exam.query.first()
    result = Result(
        user_id=current_user.id,
        exam_id=exam.id if exam else 1,
        exam_mode='tournament',
        selected_subjects='Mathematics,English,General Paper',
        num_questions_allowed=30,
        time_limit_minutes=30,
        passing_score=18,
        started_at=datetime.utcnow()
    )
    db.session.add(result)
    db.session.commit()
    for q in all_questions:
        placeholder = Answer(
            result_id=result.id,
            question_id=q.id,
            user_answer=None,
            is_correct=False,
            score_obtained=0
        )
        db.session.add(placeholder)
    db.session.commit()
    return redirect(url_for('exam.tournament_take', result_id=result.id))


@exam_bp.route('/tournament/take/<int:result_id>')
@login_required
def tournament_take(result_id):
    result = Result.query.get_or_404(result_id)
    if result.user_id != current_user.id or result.exam_mode != 'tournament':
        flash('Unauthorized access.', 'error')
        return redirect(url_for('main.dashboard'))
    if result.completed_at:
        return redirect(url_for('exam.tournament_result', result_id=result_id))
    answers = Answer.query.filter_by(result_id=result_id).all()
    question_ids = [a.question_id for a in answers]
    questions = Question.query.filter(Question.id.in_(question_ids)).all()
    answered_ids = [a.question_id for a in answers if a.user_answer is not None]
    return render_template('exam/tournament_take.html',
        result=result, questions=questions, answered_ids=answered_ids)


@exam_bp.route('/api/tournament/<int:result_id>/submit-answer', methods=['POST'])
@login_required
def tournament_submit_answer(result_id):
    data = request.get_json()
    result = Result.query.get_or_404(result_id)
    if result.user_id != current_user.id or result.exam_mode != 'tournament':
        return jsonify({'error': 'Unauthorized'}), 403
    question_id = data.get('question_id')
    user_answer = data.get('answer')
    question = Question.query.get_or_404(question_id)
    existing = Answer.query.filter_by(result_id=result_id, question_id=question_id).first()
    is_correct = user_answer == question.correct_answer
    score = question.marks if is_correct else 0
    if existing:
        existing.user_answer = user_answer
        existing.is_correct = is_correct
        existing.score_obtained = score
    else:
        db.session.add(Answer(
            result_id=result_id, question_id=question_id,
            user_answer=user_answer, is_correct=is_correct, score_obtained=score
        ))
    db.session.commit()
    return jsonify({'success': True, 'is_correct': is_correct})


@exam_bp.route('/api/tournament/<int:result_id>/finish', methods=['POST'])
@login_required
def tournament_finish(result_id):
    result = Result.query.get_or_404(result_id)
    if result.user_id != current_user.id or result.exam_mode != 'tournament':
        return jsonify({'error': 'Unauthorized'}), 403
    answers = Answer.query.filter_by(result_id=result_id).all()
    total_score = sum(a.score_obtained for a in answers)
    result.completed_at = datetime.utcnow()
    result.total_score = total_score
    result.percentage = (total_score / 30 * 100)
    result.is_passed = result.total_score >= result.passing_score
    result.is_graded = True
    result.time_taken_seconds = int((result.completed_at - result.started_at).total_seconds())
    db.session.commit()
    return jsonify({'success': True, 'redirect': url_for('exam.tournament_result', result_id=result_id)})


@exam_bp.route('/tournament/result/<int:result_id>')
@login_required
def tournament_result(result_id):
    result = Result.query.get_or_404(result_id)
    if result.user_id != current_user.id:
        flash('Unauthorized access.', 'error')
        return redirect(url_for('main.dashboard'))
    answers = Answer.query.filter_by(result_id=result_id).all()
    # Rank among all tournament results this week
    week_start = datetime.utcnow() - timedelta(days=datetime.utcnow().weekday())
    rank = db.session.query(func.count(Result.id)).filter(
        Result.exam_mode == 'tournament',
        Result.is_graded == True,
        Result.started_at >= week_start,
        Result.total_score > result.total_score
    ).scalar() + 1
    total_participants = db.session.query(func.count(Result.id)).filter(
        Result.exam_mode == 'tournament',
        Result.is_graded == True,
        Result.started_at >= week_start
    ).scalar()
    return render_template('exam/tournament_result.html',
        result=result, answers=answers, total_marks=30,
        rank=rank, total_participants=total_participants)


# ---- Admin: Generate tournament access codes (admin route) ----
@exam_bp.route('/admin/tournament/generate-codes', methods=['GET', 'POST'])
@login_required
def admin_generate_codes():
    """Admin-only: generate paid tournament access codes."""
    if not current_user.is_admin if hasattr(current_user, 'is_admin') else False:
        flash('Admin access required.', 'error')
        return redirect(url_for('main.dashboard'))
    generated = []
    if request.method == 'POST':
        count = int(request.form.get('count', 1))
        for _ in range(min(count, 50)):  # max 50 at a time
            code = generate_tournament_code()
            entry = TournamentEntry(
                access_code=code,
                is_used=False,
                created_at=datetime.utcnow()
            )
            db.session.add(entry)
            generated.append(code)
        db.session.commit()
        flash(f'{len(generated)} access codes generated successfully!', 'success')
    return render_template('exam/admin_codes.html', generated_codes=generated)
