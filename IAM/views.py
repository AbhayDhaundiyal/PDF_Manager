from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from rest_framework.views import APIView
from IAM.utils.utils import verify_token
from .models import User
import jwt
from IAM.serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password
class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        try:
            if "" in [data["first_name"], data["last_name"], data["email"], data["password"]]:
                response = HttpResponse("Empty Fields Not Accepted")
                response.status_code = 400 
                return response
            user = User(first_name = data["first_name"], last_name = data["last_name"], email = data["email"], password = make_password(data["password"]))
            user.save()
        except IntegrityError as e:
            response = HttpResponse("Account with the same email already exists")
            response.status_code = 400 
            return response
        except Exception as e:
            response = HttpResponse("Some fields are missing")
            response.status_code = 400 
            return response
        response = HttpResponse("User Created Successfully")
        response.status_code = 201
        return response
    
class Login(APIView):
    def post(self, request):
        data = request.data
        try:
            user = User.objects.get(email = data["email"])
        except:
            response = HttpResponse("No account associated with the given email")
            response.status_code = 400 
            return response
        
        if not check_password(data["password"], user.password):
            response = HttpResponse("Incorrect Password")
            response.status_code = 400 
            return response
        payload_data = {
            "user_id": user.id,
            "email": user.email,
        }
        token = jwt.encode(
            payload=payload_data,
            key=settings.SECRET_KEY
        )
        response_body = {
            "access_token" : token,
            "first_name" : user.first_name,
            "last_name" : user.last_name,
            "email" : user.email,
        }
        response = JsonResponse(response_body)
        response.status_code = 200
        return response


class UserListView(APIView):
    def get(self, request):
        try:
            payload = verify_token(request.headers["Authorization"].split(" ")[1])
            users = User.objects.all()
            user_list = list()
            for user in users:
                user_list.append(UserSerializer(user).data)
            response = JsonResponse({"result" : user_list}, safe= False)
            response.status_code = 200
            return response
        except Exception as e:
            response = HttpResponse(str(e))
            response.status_code = 400
            return response