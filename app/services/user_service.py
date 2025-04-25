from routes.models import User, AgeStatus, GenderStatus
from config import db
from flask import abort

def create_user(name, age, gender, email):
    try:
        new_user = User(
            name=name,
            age=AgeStatus(age),
            gender=GenderStatus(gender),
            email=email
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()
    except Exception as e:
        db.session.rollback()
        abort(400, f"유저 생성 실패: {str(e)}")

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404, "해당 유저를 찾을 수 없습니다.")
    return user.to_dict()
