import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from IAM.models import User
from dashboard.models import FileShared, File, FileDetails, Comments
from IAM.utils.utils import verify_token
from dashboard.serializers import FileDetailsSerializer, CommentsSerializer

class PDFView(APIView):
    def get(self, request):
        try: 
            payload = verify_token(request.headers["Authorization"].split(" ")[1])
            files = FileShared.objects.filter(user_id = payload["user_id"])
            response_dict = list()
            for file in files:
                file_detail = FileDetails.objects.get(file_id = file.file_id)
                response_dict.append(FileDetailsSerializer(file_detail).data)
            response = JsonResponse({"result" : response_dict}, safe= False)
            response.status_code = 200
            return response
        except Exception as e:
            response = HttpResponse(str(e))
            response.status_code = 400
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
                user = User.objects.filter(email = data["second_user"])
                if len(user) == 0:
                    raise Exception("No such user")
                shared = FileShared.objects.filter(user_id = user[0].id, file_id = data["file_id"])
                if len(shared) > 0:
                    response = HttpResponse(f"This File is already shared to {data['second_user']}")
                    response.status_code = 400
                    return response
                file_shared = FileShared()
                file_shared.user_id = user[0].id
                file_shared.file_id = data["file_id"]
                file_shared.save()
                response = HttpResponse(f"The file was shared successfully with {data['second_user']}")
                response.status_code = 200
                return response
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
        

class CommentsView(APIView):
    def post(self, request, file_id, comment_id):
        try:
            payload = verify_token(request.headers["Authorization"].split(" ")[1])
            data = request.data
            file_details = get_object_or_404(FileDetails, file_id = data['file_id'])
            if not file_details.is_public:
                get_object_or_404(FileShared, file_id = data['file_id'], user_id = payload["user_id"])
            if comment_id:
                get_object_or_404(Comments, id = data["comment_id"])
            comment = Comments()
            comment.user_id = payload["user_id"]
            comment.file_id = data["file_id"]
            comment.content = data["content"]
            if comment_id:
                comment.parent = comment_id
            comment.save()
            response = HttpResponse("comment added")
            response.status_code = 201
            return response
        except Exception as e:
            response = HttpResponse(str(e))
            response.status_code = 500
            return response
    def get(self, request, file_id, comment_id):
        try:
            file_details = get_object_or_404(FileDetails, file_id = file_id)
            if not file_details.is_public:
                payload = verify_token(request.headers["Authorization"].split(" ")[1])
                get_object_or_404(FileShared, file_id = file_id, user_id = payload["user_id"])
            if comment_id == 0:
                comments = Comments.objects.filter(file_id = file_id, parent = None)
                comment_list = list()
                for comment in comments:
                    comment_list.append(CommentsSerializer(comment).data)
                response = JsonResponse(comment_list, safe=False)
                response.status_code = 200
                return response
            else:
                get_object_or_404(Comments, id = comment_id)
                replies = Comments.objects.filter(parent = comment_id)
                reply_list = list()
                for reply in replies:
                    reply_list.append(CommentsSerializer(reply).data)
                response = JsonResponse(reply_list, safe=False)
                response.status_code = 200
                return response
        except Exception as e:
            response = HttpResponse(str(e))
            response.status_code = 500
            return response

