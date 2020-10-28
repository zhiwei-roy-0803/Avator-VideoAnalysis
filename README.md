# Avator-VideoAnalysis


**How to install**
+ For docker user
```angular2
TODO
```
+ For non-docker user
```
bash scripts/seetup.sh
```

**How to use** 
```
python3 start_model_servers.py
python3 manage.py runserver`
```
Entry for web browser: http://localhost:8000/account/login/.


**System Architecture**

![](./static/System_Architecture.png)

**Key Feature**
+ Object detection is accomplished by [Yolo v3](https://github.com/eriklindernoren/PyTorch-YOLOv3) and pre-trained weights are utilized.
+ Face Detection is based on [face_recognition](https://github.com/ageitgey/face_recognition)——the world's simplest facial recognition api for Python and the command line. 
+ Web service is based on [Django](https://www.djangoproject.com/) and [Django REST Framwork](https://www.django-rest-framework.org/).
+ Computational intensive deep learning inference is accomplished via customized deep learning servers to improve the scalability. Communications between the backend server and deep learning servers are supported by [gRPC](https://grpc.io/).
+ Uploaded vedios of any resolution is supported. 
+ A user management prototype is implemented and user login, registration and authentification is supported. Multi-user simultaneously processing is also allowed.


**To Do**
+ Add some audio signal processing features like denoising, fading-in, fading-out etc.
+ Try asynchronized stream RPC service to reduce process delay.


