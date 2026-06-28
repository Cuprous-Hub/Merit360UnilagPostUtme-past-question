from app import create_app, db
from app.models.exam import TournamentEntry

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ tournament_entries table created successfully!")
