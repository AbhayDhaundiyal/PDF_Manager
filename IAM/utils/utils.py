from django.conf import settings
import jwt
from IAM.models import User


def verify_token(token):
    payload = jwt.decode(token, key= settings.SECRET_KEY, algorithms=["HS256"])
    if not payload.get("user_id", None) and not payload.get("email", None):
        raise ValueError("Invalid Token")
    if payload["user_id"] == "" or payload["email"] == "":
        raise ValueError("Invalid Token")
    return payload