from datetime import datetime, timezone

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class UserProfile(db.Model):
    __tablename__ = "user_profiles"

    id = db.Column(db.Integer, primary_key=True)

    wallet_address = db.Column(
        db.String(42),
        unique=True,
        nullable=False,
        index=True,
    )

    full_name = db.Column(
        db.String(150),
        nullable=False,
    )

    role = db.Column(
        db.Integer,
        nullable=False,
    )

    email = db.Column(
        db.String(150),
        nullable=True,
    )

    institution = db.Column(
        db.String(200),
        nullable=True,
    )

    department = db.Column(
        db.String(150),
        nullable=True,
    )

    speciality = db.Column(
        db.String(150),
        nullable=True,
    )

    professional_id = db.Column(
        db.String(100),
        nullable=True,
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "wallet_address": self.wallet_address,
            "full_name": self.full_name,
            "role": self.role,
            "email": self.email,
            "institution": self.institution,
            "department": self.department,
            "speciality": self.speciality,
            "professional_id": self.professional_id,
            "created_at": self.created_at.isoformat(),
        }