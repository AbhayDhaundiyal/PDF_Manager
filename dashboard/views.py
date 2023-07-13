from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
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
            response.status_code = 400
            return response
        print(payload)
        return None
        # file = request.FILES["file"]
        # with open(file.name, "wb") as obj:
        #     obj.write(file.read())
        