import os
import pytest
from app import create_app, db
from app.models.user import User


@pytest.fixture()
def client():
    os.environ['FLASK_ENV'] = 'testing'
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.app_context():
        db.drop_all()
        db.create_all()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.drop_all()


def test_exam_mode_page_shows_30_question_format(client):
    user = User(username='analyst', email='analyst@example.com', full_name='Analyst User')
    user.set_password('secret123')
    with client.application.app_context():
        db.session.add(user)
        db.session.commit()

    client.post('/login', data={
        'username': 'analyst',
        'password': 'secret123'
    }, follow_redirects=True)

    response = client.get('/exam-mode')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert '30 Questions' in html
    assert '30 Minutes' in html


def test_analytics_page_is_available_to_logged_in_users(client):
    user = User(username='analytics', email='analytics@example.com', full_name='Analytics User')
    user.set_password('secret123')
    with client.application.app_context():
        db.session.add(user)
        db.session.commit()

    client.post('/login', data={
        'username': 'analytics',
        'password': 'secret123'
    }, follow_redirects=True)

    response = client.get('/analytics')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'Performance Analytics' in html
    assert 'Preparation Level' in html
