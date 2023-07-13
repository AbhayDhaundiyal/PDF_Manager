import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from IAM.models import User
from dashboard.models import FileShared, File, FileDetails
from IAM.utils.utils import verify_token
from dashboard.serializers import FileDetailsSerializer

def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data
class PDFView(APIView):
    def get(self, request):
        payload = verify_token(request.headers["Authorization"].split(" ")[1])
        files = FileShared.objects.filter(user_id = payload["user_id"])
        response_dict = list()
        for file in files:
            file_detail = FileDetails.objects.get(file_id = file.file_id)
            response_dict.append(FileDetailsSerializer(file_detail).data)
        response = JsonResponse({"result" : response_dict}, safe= False)
        response.status_code = 200
        return response
    
    def post(self, request):
        try:
            token = request.headers["Authorization"].split(" ")[1]
            header_payload = verify_token(token)
            uploaded_file = request.FILES['file']
            payload = request.data
            file_details = FileDetails()
            file_details.file_name = payload["fileName"]
            file_details.owner = header_payload["user_id"]
            file_details.created_at = datetime.datetime.now()
            file_details.save()
            file = File()
            file.file_id = file_details.file_id
            file.file = uploaded_file.read()
            file.save()
            file_shared = FileShared()
            file_shared.file_id = file_details.file_id
            file_shared.user_id = header_payload["user_id"]
            file_shared.save()
            response = JsonResponse({
                "message" : "File uploaded successfully",
                "file_id" : file.file_id
            })
            response.status_code = 200
            return response
        except Exception as e:
            response = HttpResponse(str(e))
            response.status_code = 500
            return response
    def patch(self, request):
        try:
            payload = verify_token(request.headers["Authorization"].split(" ")[1])
            data = request.data
            file_detail = FileDetails.objects.filter(file_id = data["file_id"], owner = payload["user_id"])
            if len(file_detail) == 0:
                raise Exception("Permission Denied")
            if data["operation"] == "share":
                user = User.objects.filter(id = data["second_user"])
                if len(user) == 0:
                    raise Exception("No such user")
                file_shared = FileShared()
                file_shared.user_id = data["second_user"]
                file_shared.file_id = data["file_id"]
                file_shared.save()
            elif data["operation"] == "toggle":
                file_detail = FileDetails.objects.get(file_id = data["file_id"])
                file_detail.is_public = not file_detail.is_public
                file_detail.save()
                if file_detail.is_public:
                    response = JsonResponse({"file_status" : file_detail.is_public, "message" : "made the file public"})
                else:
                    response = JsonResponse({"file_status" : file_detail.is_public, "message" : "made the file available to selected users"})
                response.status_code = 200
                return response
        except Exception as e:
            response = HttpResponse(str(e))
            response.status_code = 400
            return response
        

class OpenPDFView(APIView):
    def get(self, request, file_id : int):
        try:
            file = FileDetails.objects.get(file_id = file_id)
            if not file.is_public :
                payload = verify_token(request.headers["Authorization"].split(" ")[1])
                get_object_or_404(FileShared, file_id = file_id, user_id = payload["user_id"])
            file = File.objects.get(file_id = file_id)
            response = HttpResponse(file.file, content_type='application/octet-stream')
            response.status_code = 200
            return response
        except Exception as e:
            response = HttpResponse(str(e))
            response.status_code = 500
            return response
        
        
