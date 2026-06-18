"""
Admin utilities for managing exams and questions
"""

from app import create_app, db
from app.models import Exam, Question, User, Result
from datetime import datetime

app = create_app()

def list_all_exams():
    """List all exams in the system"""
    exams = Exam.query.all()
    print("\n" + "="*60)
    print("AVAILABLE EXAMS")
    print("="*60)
    for exam in exams:
        question_count = Question.query.filter_by(exam_id=exam.id).count()
        print(f"\nID: {exam.id}")
        print(f"Title: {exam.title}")
        print(f"Subject: {exam.subject}")
        print(f"Duration: {exam.duration_minutes} minutes")
        print(f"Questions: {question_count}")
        print(f"Passing Score: {exam.passing_score}%")
        print(f"Active: {exam.is_active}")

def list_all_users():
    """List all registered users"""
    users = User.query.all()
    print("\n" + "="*60)
    print("REGISTERED USERS")
    print("="*60)
    for user in users:
        print(f"\nID: {user.id}")
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")
        print(f"Full Name: {user.full_name}")
        print(f"Department: {user.department or 'Not specified'}")
        print(f"Registered: {user.created_at}")

def get_user_statistics(user_id):
    """Get statistics for a specific user"""
    user = User.query.get(user_id)
    if not user:
        print(f"User with ID {user_id} not found")
        return
    
    results = Result.query.filter_by(user_id=user_id).all()
    
    print("\n" + "="*60)
    print(f"STATISTICS FOR {user.username}")
    print("="*60)
    print(f"Total Exams Taken: {len(results)}")
    
    if results:
        passed = sum(1 for r in results if r.is_passed)
        avg_percentage = sum(r.percentage for r in results) / len(results)
        
        print(f"Exams Passed: {passed}/{len(results)}")
        print(f"Pass Rate: {(passed/len(results)*100):.1f}%")
        print(f"Average Score: {avg_percentage:.1f}%")
        
        print("\nRecent Attempts:")
        for result in sorted(results, key=lambda x: x.completed_at, reverse=True)[:5]:
            if result.completed_at:
                print(f"  - {result.exam.title}: {result.percentage:.1f}% ({result.total_score}/{sum(q.marks for q in result.exam.questions)})")

def delete_user(user_id):
    """Delete a user and their results"""
    user = User.query.get(user_id)
    if not user:
        print(f"User with ID {user_id} not found")
        return
    
    username = user.username
    db.session.delete(user)
    db.session.commit()
    print(f"✅ User '{username}' and all their results have been deleted")

def deactivate_exam(exam_id):
    """Deactivate an exam (hide from students)"""
    exam = Exam.query.get(exam_id)
    if not exam:
        print(f"Exam with ID {exam_id} not found")
        return
    
    exam.is_active = False
    db.session.commit()
    print(f"✅ Exam '{exam.title}' has been deactivated")

def activate_exam(exam_id):
    """Activate an exam (show to students)"""
    exam = Exam.query.get(exam_id)
    if not exam:
        print(f"Exam with ID {exam_id} not found")
        return
    
    exam.is_active = True
    db.session.commit()
    print(f"✅ Exam '{exam.title}' has been activated")

def reset_all_results():
    """Reset all user results (careful with this!)"""
    result_count = Result.query.count()
    Result.query.delete()
    db.session.commit()
    print(f"✅ All {result_count} results have been deleted")

def get_exam_statistics(exam_id):
    """Get statistics for a specific exam"""
    exam = Exam.query.get(exam_id)
    if not exam:
        print(f"Exam with ID {exam_id} not found")
        return
    
    results = Result.query.filter_by(exam_id=exam_id).all()
    
    print("\n" + "="*60)
    print(f"STATISTICS FOR {exam.title}")
    print("="*60)
    print(f"Total Attempts: {len(results)}")
    
    if results:
        passed = sum(1 for r in results if r.is_passed)
        avg_percentage = sum(r.percentage for r in results) / len(results)
        avg_time = sum(r.time_taken_seconds for r in results if r.time_taken_seconds) / len([r for r in results if r.time_taken_seconds])
        
        print(f"Pass Rate: {(passed/len(results)*100):.1f}%")
        print(f"Average Score: {avg_percentage:.1f}%")
        print(f"Average Time: {int(avg_time)}s ({int(avg_time/60)}m {int(avg_time%60)}s)")

if __name__ == '__main__':
    with app.app_context():
        print("\nUNILAG CBT Practice - Admin Utilities")
        print("-" * 60)
        print("\nUsage Examples:")
        print("  list_all_exams()")
        print("  list_all_users()")
        print("  get_user_statistics(user_id)")
        print("  get_exam_statistics(exam_id)")
        print("  delete_user(user_id)")
        print("  deactivate_exam(exam_id)")
        print("  activate_exam(exam_id)")
        print("  reset_all_results()")
        print("\nEnter commands in the Python shell above:")
