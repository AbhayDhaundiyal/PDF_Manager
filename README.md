# The PDF Manager(Backend)



## Description

The goal of this project is to develop a secure and user-friendly web application that allows users to sign up, authenticate, upload, share, and comment on PDF files. The objectives include user management, secure file upload and storage, a dashboard for file access, file sharing, commenting functionality, an intuitive user interface. The aim is to create a reliable platform for secure file management, collaboration, and user interaction with PDF files.


## **Installation**

 - Install python3 on your os
 - In the root directory of project run `pip install -r requirements.txt`
 - Now run `python manage.py migrate`
 - For starting the project locally `python manage.py runserver`


## **Usage**

Users can upload PDF files and make them accessible to others. Additionally, users can receive feedback comments on their PDF files. To utilize these functionalities, users are required to register an account. However, public files can be viewed by anyone, while commenting on the files is limited to registered users. The project aims to provide a platform where users can easily share and collaborate on PDF files while maintaining a seamless user experience.

## API Endpoints

**[POST]**  `base_url/iam/login/ :` 
  
This endpoint serves the purpose of user identity verification. When the user provides their credentials, the endpoint generates an access token as a response.

**[POST]**  `base_url/iam/register/ :` 
  
This endpoint facilitates the user registration process. It allows users to create an account within the system by providing necessary information such as name, email address, and password.

**[GET]**  `base_url/iam/users/ :` 
  
This endpoint retrieves a list of users who have been successfully authenticated.

**[GET]**  `dashboard/:` 
  
This endpoint provides the front-end with a list of files and their associated details specific to the logged-in user. It allows the front-end application to retrieve and display the files relevant to the user who is currently authenticated.


**[POST]**  `dashboard/:` 
  
This endpoint enables users to upload files to the backend server for storage and processing. It provides a response indicating the success or failure of the upload process.

**[PATCH]**  `dashboard/:` 
  
This endpoint enables users change the status of the file i.e. make it public or private also this endpoint also enables user to share files to other authenticated user.

**[GET]**  `dashboard/file/<int:file_id>/:` 
 
This endpoint retrieves a file by its ID and sends it to the frontend.

**[POST]**  `base_url/iam/login/:` 
  
This endpoint serves the purpose of user identity verification. When the user provides their credentials, the endpoint generates an access token as a response.

**[GET]**  `file/<int:file_id>/<int:comment_id>/:` 
  
This endpoint retrieves either the replies associated with a given comment (with a specific comment ID) or the parent comments associated with the files (with a comment ID of 0). The backend server retrieves the corresponding data based on the provided comment ID, which is then returned to the client or front-end application for display.

**[POST]**  `file/<int:file_id>/<int:comment_id>/:` 
  
This endpoint enables users to add comments or replies based on the same conditions as previously described. Users can make a POST request to this endpoint with the necessary parameters, including the comment ID for replying or 0 for adding parent comments. The backend server processes the request and adds the comment or reply accordingly. This API functionality allows users to actively participate in the discussion by adding their comments or replies in response to existing content.

**[POST]**  `file_detail/<int:file_id>/` 
  
This is an end point used to fetch the status of the file i.e. Private/Public associated with the file id.





[Project Link](https://pdfmanager124.netlify.app/)
