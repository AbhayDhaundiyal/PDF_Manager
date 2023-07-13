from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from dashboard.models import File_Shared
from IAM.utils.utils import verify_token

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
        print(payload)
        return HttpResponse("sddasd")
    
    def post(self, request):
        try:
            token = request.headers["Authorization"].split(" ")[1]
            payload = verify_token(token)
            print(request.data)
            return HttpResponse("sss")
        except Exception as e:
            response = HttpResponse(str(e))
            response.status_code = 400
            return response
        print(payload)
        return None
        # file = request.FILES["file"]
        # with open(file.name, "wb") as obj:
        #     obj.write(file.read())
        