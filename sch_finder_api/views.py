from rest_framework import views, response, exceptions, permissions, status

from .serializer import UserSerializer, UserEditSerializer
from . import services, authentication

class RegisterApi(views.APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_user(user_dc=data)

        return response.Response(data=serializer.data)

class LoginApi(views.APIView):
    def post(self, request):
        email = request.data["email"]
        password =request.data["password"]

        user = services.get_user_by_email(email=email)

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        
        token = services.create_token(user_id=user.id)
        res = response.Response({"token": token})
        # res.set_cookie(key="jwt", value=token, httponly=True)

        return res

class UserApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user

        serializer = UserSerializer(user)

        return response.Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = UserEditSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        updated_user = services.edit_user(user, data)
        return response.Response({"message": "Profile updated successfully"})
    
    def delete(self, request):
        user = request.user
        user.delete()

        return response.Response({"message": "user deleted successfully"})

class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        res = response.Response()
        res.delete_cookie("jwt")
        res.data = {"message": "See you soon!"}

        return res

