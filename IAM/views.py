from django.conf import settings
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import User
import jwt

class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        try:
            if "" in [data["first_name"], data["last_name"], data["email"], data["password"]]:
                response = HttpResponse("Empty Fields Not Accepted")
                response.status_code = 400 
                return response
        except:
            response = HttpResponse("Some fields are missing")
            response.status_code = 400 
            return response
        user = User(first_name = data["first_name"], last_name = data["last_name"], email = data["email"], password = data["password"])
        user.save()
        return HttpResponse("User Created")
    
class Login(APIView):
    def post(self, request):
        data = request.data
        try:
            user = User.objects.get(email = data["email"])
        except:
            response = HttpResponse("No account associated with the given email")
            response.status_code = 400 
            return response
        
        if user.password != data["password"]:
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
        response = HttpResponse(f"Token : {token}")
        return response
