from flask import Flask
from app.extensions import db, login_manager
from flask_wtf.csrf import CSRFProtect
from datetime import timedelta
import os

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'merit360-unilag-cbt-excellence-2025-xk9pqz')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///cbt_app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Keep users logged in reliably across visits/restarts
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=30)
    app.config['SESSION_COOKIE_SECURE'] = os.environ.get('FLASK_ENV') == 'production'
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
    app.config['REMEMBER_COOKIE_SECURE'] = os.environ.get('FLASK_ENV') == 'production'
    app.config['REMEMBER_COOKIE_SAMESITE'] = 'Lax'

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'

    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.exam import exam_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(exam_bp)

    with app.app_context():
        from app.models.user import User
        from app.models.exam import Exam, Question, Result, Answer, Topic, TournamentEntry
        db.create_all()

    return app