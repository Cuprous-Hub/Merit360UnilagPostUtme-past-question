import sys
from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    # 1. Grab and normalize email input
    if len(sys.argv) > 1:
        email = sys.argv[1]
    else:
        email = input("Enter user email: ").strip()
    
    # 2. Query the user (lowercasing handles accidental typos)
    user = User.query.filter_by(email=email.lower()).first()
    
    if not user:
        print(f"❌ No user found with email: {email}")
    elif user.is_admin:
        print(f"ℹ️ {user.username} ({email}) is already an admin.")
    else:
        try:
            # 3. Update and commit safely
            user.is_admin = True
            db.session.commit()
            print(f"✅ {user.username} ({email}) is now an admin!")
        except Exception as e:
            db.session.rollback()
            print(f"🚨 An error occurred while updating the database: {e}")