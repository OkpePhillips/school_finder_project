from rest_framework import views, response, exceptions, permissions, status

from .serializer import UserSerializer, UserEditSerializer, SchoolSerializer, EditSchoolSerializer, ScholarshipSerializer, EditScholarshipSerializer, ChangePasswordSerializer, ReviewSerializer, EditReviewSerializer
from . import services, authentication
from .models import School, Scholarship, Review

class RegisterUserApi(views.APIView):

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
        serializer = UserSerializer(user)
        res = response.Response({"token": token, "user": serializer.data})

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


class SchoolApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_school(sch=data)

        return response.Response(data=serializer.data)

    def get(self, request, id=None):
        self.authentication_classes = []
        self.permission_classes = [permissions.AllowAny]
        
        if id is not None:
            school = School.objects.filter(id=id)
        else:
            schools = School.objects.all()

        serializer = SchoolSerializer(schools, many=True)

        return response.Response(serializer.data)
    
    def delete(self, request, id):
        try:
            school = School.objects.get(id=id)
        except School.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

        school.delete()
        return response.Response({"message": "school deleted"}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        serializer = EditSchoolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        sch_update = services.update_sch(id, data)
        return response.Response({"message": "Successful"})


class ScholarshipApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        serializer = ScholarshipSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_scholarship(ship=data)

        return response.Response(data=serializer.data)

    def get(self, request, id=None):
        self.authentication_classes = []
        self.permission_classes = [permissions.AllowAny]

        if id is not None:
            scholarship = Scholarship.objects.filter(id=id)
        else:
            scholarships = Scholarship.objects.all()
        
        serializer = ScholarshipSerializer(scholarships, many=True)

        return response.Response(serializer.data)
    
    def delete(self, request, id):
        try:
            scholarship = Scholarship.objects.get(id=id)
        except Scholarship.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

        scholarship.delete()
        return response.Response({"message": "school deleted"}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        serializer = EditScholarshipSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        schship_update = services.update_scholarship(id, data)
        return response.Response({"message": "Successful"})

class ChangePassword(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        if user.check_password(serializer.data.get('old_password')):
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return response.Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
        return response.Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
  

class ReviewApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        school = School.objects.get(id=data.school_id)
        serializer.instance = services.create_review(school=school, user=request.user, review=data)

        school.update_rating()
        return response.Response(data=serializer.data)

    def get(self, request, id=None):
        self.authentication_classes = []
        self.permission_classes = [permissions.AllowAny]

        if id is not None:
            reviews = Review.objects.filter(school_id=id)
        else:
            reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True)

        return response.Response(serializer.data)
    
    def delete(self, request, id):
        try:
            review = Review.objects.get(id=id)
        except Review.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return response.Response({"message": "review deleted"}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        serializer = EditReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        review = services.update_review(id, data)
        return response.Response({"message": "Success"})