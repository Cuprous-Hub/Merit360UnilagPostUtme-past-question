from flask import Blueprint, render_template, redirect, url_for, flash, send_from_directory
from flask_login import login_required, current_user
from app import db
from app.models import Exam, Result
from app.models.exam import Topic
from sqlalchemy import desc
import os

main_bp = Blueprint('main', __name__)

# ─── PWA Service Worker ──────────────────────────────────────────────────────
@main_bp.route('/sw.js')
def service_worker():
    return send_from_directory(
        os.path.join(os.path.dirname(__file__), '..', 'static'),
        'sw.js',
        mimetype='application/javascript'
    )

# ─── PWA Manifest ────────────────────────────────────────────────────────────
@main_bp.route('/manifest.json')
def manifest():
    return send_from_directory(
        os.path.join(os.path.dirname(__file__), '..', 'static'),
        'manifest.json',
        mimetype='application/manifest+json'
    )

# ─── Main Routes ─────────────────────────────────────────────────────────────
@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    exams = Exam.query.filter_by(is_active=True).all()
    user_results = Result.query.filter_by(user_id=current_user.id).all()
    
    # Calculate statistics
    total_tests = len(user_results)
    passed_tests = sum(1 for r in user_results if r.is_passed)
    avg_score = sum(r.percentage for r in user_results) / len(user_results) if user_results else 0
    
    # Calculate total marks for each result for display
    for result in user_results:
        result.total_marks = sum(q.marks for q in result.exam.questions)
    
    # Practice mode subjects
    subjects = [s[0] for s in db.session.query(Topic.subject).distinct().all()]

    return render_template('dashboard.html',
                         exams=exams,
                         user_results=user_results,
                         total_tests=total_tests,
                         passed_tests=passed_tests,
                         avg_score=avg_score,
                         subjects=subjects,
                         is_admin=getattr(current_user, 'is_admin', False))

@main_bp.route('/analytics')
@login_required
def analytics():
    user_results = Result.query.filter_by(user_id=current_user.id).filter(Result.completed_at.isnot(None)).order_by(desc(Result.completed_at)).all()
    completed_results = [result for result in user_results if result.completed_at]

    total_tests = len(completed_results)
    passed_tests = sum(1 for result in completed_results if result.is_passed)
    avg_score = sum(result.total_score or 0 for result in completed_results) / total_tests if total_tests else 0
    avg_percentage = sum(result.percentage or 0 for result in completed_results) / total_tests if total_tests else 0
    best_score = max((result.total_score or 0) for result in completed_results) if completed_results else 0
    best_percentage = max((result.percentage or 0) for result in completed_results) if completed_results else 0
    latest_result = completed_results[0] if completed_results else None

    full_exam_results = Result.query.filter(
        Result.exam_mode == 'full_exam',
        Result.is_graded == True,
        Result.completed_at.isnot(None)
    ).order_by(desc(Result.total_score)).all()

    user_rank = 1
    if full_exam_results:
        user_rank = next((index + 1 for index, result in enumerate(full_exam_results) if result.user_id == current_user.id), len(full_exam_results) + 1)

    subject_stats = {}
    for result in completed_results:
        for answer in result.answers:
            question = answer.question
            if not question or not question.subject:
                continue
            entry = subject_stats.setdefault(question.subject, {'correct': 0, 'attempted': 0})
            entry['attempted'] += 1
            if answer.is_correct:
                entry['correct'] += 1

    subject_breakdown = []
    for subject, stats in sorted(subject_stats.items()):
        accuracy = round((stats['correct'] / stats['attempted']) * 100, 1) if stats['attempted'] else 0
        subject_breakdown.append({'subject': subject, 'accuracy': accuracy, 'correct': stats['correct'], 'attempted': stats['attempted']})

    if avg_percentage >= 75:
        preparation_level = 'Excellent preparation'
        insight = 'You are preparing very well and are ready to tackle the exam with confidence.'
        insight_badge = 'success'
    elif avg_percentage >= 60:
        preparation_level = 'Good preparation'
        insight = 'Your scores are solid. Keep practicing to turn good results into excellent ones.'
        insight_badge = 'info'
    elif avg_percentage >= 40:
        preparation_level = 'Steady improvement'
        insight = 'You are improving. A bit more revision on weak areas will push your results higher.'
        insight_badge = 'warning'
    else:
        preparation_level = 'Needs more revision'
        insight = 'Your recent attempts show room to improve. Focus on weak topics and practice more consistently.'
        insight_badge = 'danger'

    return render_template(
        'analytics.html',
        user_results=completed_results,
        total_tests=total_tests,
        passed_tests=passed_tests,
        avg_score=avg_score,
        avg_percentage=avg_percentage,
        best_score=best_score,
        best_percentage=best_percentage,
        latest_result=latest_result,
        user_rank=user_rank,
        total_students=len(full_exam_results),
        subject_breakdown=subject_breakdown,
        preparation_level=preparation_level,
        insight=insight,
        insight_badge=insight_badge,
        overall_avg_score=round(sum(result.percentage or 0 for result in full_exam_results) / len(full_exam_results), 1) if full_exam_results else 0,
        top_score=full_exam_results[0].total_score if full_exam_results else 0,
    )

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')
