"""
Run this ONCE after deploying to add the is_admin column to users table.
Usage: python add_admin_column.py
"""
from app import create_app, db
from app.models.user import User
from app.models.exam import TournamentEntry
import sqlalchemy as sa

app = create_app()

with app.app_context():
    # Create any missing tables (tournament_entries, etc.)
    db.create_all()

    # Add is_admin column if it doesn't exist
    with db.engine.connect() as conn:
        try:
            conn.execute(sa.text('ALTER TABLE users ADD COLUMN is_admin BOOLEAN DEFAULT 0'))
            conn.commit()
            print("✅ is_admin column added to users table")
        except Exception as e:
            if 'duplicate column' in str(e).lower() or 'already exists' in str(e).lower():
                print("ℹ️  is_admin column already exists — skipping")
            else:
                print(f"⚠️  {e}")

    print("✅ All done! To make yourself admin, run:")
    print("   python make_admin.py your@email.com")
