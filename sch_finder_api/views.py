from rest_framework import views, response, exceptions, permissions, status, filters

from .serializer import UserSerializer, UserEditSerializer, SchoolSerializer, EditSchoolSerializer, ScholarshipSerializer, EditScholarshipSerializer, ChangePasswordSerializer, ReviewSerializer, EditReviewSerializer, CountrySerializer, CitySerializer
from . import services, authentication
from .models import School, Scholarship, Review, Country, City
from django.db.models import Q

#API Documentation imports
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class RegisterUserApi(views.APIView):
    """
    User registration endpoint
    """
    @swagger_auto_schema(
        operation_description="User registration endpoint",
        responses={
            200: "Registered user details",
            400: "Bad Request",
        },
        request_body=UserSerializer,
        )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_user(user_dc=data)

        return response.Response(data=serializer.data)

class LoginApi(views.APIView):
    """
    API view to log a user in using email and password
    """
    @swagger_auto_schema(
        operation_description="User Login endpoint",
        responses={
            200: "authentication token, and Logged in user",
            400: "Bad Request",
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(
                    type=openapi.TYPE_STRING, description="User email"),
                'password': openapi.Schema(
                    type=openapi.TYPE_STRING, description="Password"),
            },
            required=['email', 'password']
        )
    )
    def post(self, request):
        """
        Log in user with email and password.
        """
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
    """
    API view to carry out logged user related activities.
    """
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
    )
    def get(self, request):
        """
        API view to retrieve a logged in user.
        """
        user = request.user

        serializer = UserSerializer(user)

        return response.Response(serializer.data)
    
    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
        operation_description="Edit Logged in user details",
        request_body=UserEditSerializer,
    )
    def put(self, request):
        """
        Endpoint to edit user details
        """
        user = request.user
        serializer = UserEditSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        updated_user = services.edit_user(user, data)
        return response.Response({"message": "Profile updated successfully"})
    
    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
    )
    def delete(self, request):
        """ Api view to delete a user """
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
    """
    API view to create, retrieve, update and delete school
    """
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
        responses={
            200: "Registered school details",
            400: "Bad Request",
        },
        request_body=SchoolSerializer,
        consumes=['multipart/form-data'],
    )
    def post(self, request):
        """ Create a school object """
        serializer = SchoolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_school(sch=data)

        return response.Response(data=serializer.data)
    
    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
    )
    def delete(self, request, id):
        """ 
        Delete school with id provided
        """
        try:
            school = School.objects.get(id=id)
        except School.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

        school.delete()
        return response.Response({"message": "school deleted"}, status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
        responses={
            200: "Successful",
            400: "Bad Request",
        },
        request_body=EditSchoolSerializer,
    )
    def put(self, request, id):
        """Edit School Details"""
        serializer = EditSchoolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        sch_update = services.update_sch(id, data)
        return response.Response({"message": "Successful"})


class GetSchoolApi(views.APIView):
    """ View to get schools without authentication """
    def get(self, request, id=None):
        """
        Retrieve school with id provided, or all schools if no id
        """        
        if id is not None:
            schools = School.objects.filter(id=id)
        else:
            schools = School.objects.all()

        serializer = SchoolSerializer(schools, many=True)

        return response.Response(serializer.data)

class ScholarshipApi(views.APIView):
    """
    API view to create, retrieve, update and delete scholarship objects
    """
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
        responses={
            200: "Created scholarship details",
            400: "Bad Request",
        },
        request_body=ScholarshipSerializer,
    )
    def post(self, request):
        """
        Create a new scholarship object
        """
        serializer = ScholarshipSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_scholarship(ship=data)

        return response.Response(serializer.data)
    
    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
    )
    def delete(self, request, id):
        """
        Delete a scholarship object based on id provided.
        """
        try:
            scholarship = Scholarship.objects.get(id=id)
        except Scholarship.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

        scholarship.delete()
        return response.Response({"message": "school deleted"}, status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
        responses={
            200: "Successful",
            400: "Bad Request",
        },
        request_body=EditScholarshipSerializer,
    )
    def put(self, request, id):
        """
        Edit scholarship details
        """
        serializer = EditScholarshipSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        schship_update = services.update_scholarship(id, data)
        return response.Response({"message": "Successful"})

class ScholarshipGetApi(views.APIView):
    """ Retrieve scholarships """
    def get(self, request, id=None):
        """
        Retrieve specific scholarship if id, else retrieve all scholarship objects.
        """
        if id is not None:
            scholarships = Scholarship.objects.filter(id=id)
        else:
            scholarships = Scholarship.objects.all()
        
        serializer = ScholarshipSerializer(scholarships, many=True)

        return response.Response(serializer.data)


class ChangePassword(views.APIView):
    """
    API view for change of password
    """
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
        responses={
            200: "Password successfully changed",
            400: "Bad Request",
        },
        request_body=ChangePasswordSerializer,
    )
    def post(self, request):
        """ Change user password """
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
    """
    API view for creating, editing, retrieving and deleting a review object
    """
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
        responses={
            200: "Review data",
            400: "Bad Request",
        },
        request_body=ReviewSerializer,
    )
    def post(self, request):
        """ Create a new review object """
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        school = School.objects.get(id=data.school_id)
        print(request.user)
        serializer.instance = services.create_review(school=school, user=request.user, review=data)

        school.update_rating()
        return response.Response(data=serializer.data)
    
    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
    )
    def delete(self, request, id):
        """
        Delete a review object based on id provided

        Parameters:
        - id: The ID of the review to delete (integer)

        Example:
        DELETE /api/reviews/12/
        """
        try:
            review = Review.objects.get(id=id)
        except Review.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return response.Response({"message": "review deleted"}, status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
        responses={
            200: "Success",
            400: "Bad Request",
        },
        request_body=EditReviewSerializer,
    )
    def put(self, request, id):
        """
        Edit a review object
        """
        serializer = EditReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        review = services.update_review(id, data)
        return response.Response({"message": "Success"})

class ReviewGetApi(views.APIView):
    """ Returns reviews """
    def get(self, request, id=None):
        """
        Retrieve a specific review or all reviews if id is not provided
        """
        if id is not None:
            reviews = Review.objects.filter(school_id=id)
        else:
            reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True)

        return response.Response(serializer.data)


class CountryApi(views.APIView):
    """
    API view to create and retrieve country
    """
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
        responses={
            200: "Success",
            400: "Bad Request",
        },
        request_body=CountrySerializer,
    )
    def post(self, request):
        """ Create a Country object """
        serializer = CountrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_country(country=data)

        return response.Response(data=serializer.data)


class GetCountryApi(views.APIView):
    """ Retrieve countries """
    def get(self, request, id=None):
        """
        Retrieve country with id provided, or all countries if no id provided
        """
        if id is not None:
            coountry = Country.objects.filter(id=id)
        else:
            country = Country.objects.all()

        serializer = CountrySerializer(country, many=True)

        return response.Response(serializer.data)


class CityApi(views.APIView):
    """
    API view to create and retrieve city
    """
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter(
            name='token',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='token',
            required=True,
            ),
        ],
        responses={
            200: "Success",
            400: "Bad Request",
        },
        request_body=CitySerializer,
    )
    def post(self, request):
        """ Create a City object """
        serializer = CitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        country = data.country
        serializer.instance = services.create_city(country, city=data)

        return response.Response({"message": "Successful"})


class GetCitiesApi(views.APIView):
    """ Retrieve cities in the database """
    def get(self, request, id=None):
        """
        Retrieve city with id provided, or all cities if no id provided
        """        
        if id is not None:
            city = City.objects.filter(id=id)
        else:
            city = City.objects.all()

        serializer = CitySerializer(city, many=True)

        return response.Response(serializer.data)


class SearchApi(views.APIView):
    filter_backends = [filters.SearchFilter]
    search_fields = {
        School: ['name', 'degrees'],
        City: ['name'],
        Scholarship: ['title', 'description', 'benefit'],
        Country: ['name'],
    }

    def get_queryset(self):
        query = self.request.query_params.get('search', '')
        queryset = []

        for model, fields in self.search_fields.items():
            for field in fields:
                queryset.extend(model.objects.filter(Q(**{f'{field}__icontains': query})))
        return queryset

    def get_serializer_class(self, instance):
        """ Get appropriate serializer class based on model instance """
        if isinstance(instance, School):
            return SchoolSerializer
        elif isinstance(instance, City):
            return CitySerializer
        elif isinstance(instance, Scholarship):
            return ScholarshipSerializer
        elif isinstance(instance, Country):
            return CountrySerializer
        else:
            raise ValueError("Invalid instance type")

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Search query string',
                required=True,
            ),
        ],
        responses={
            200: "Success",
            400: "Bad Request",
        },
    )
    def get(self, request):
        queryset = self.get_queryset()
        serialized_data = []
        for obj in queryset:
            serializer_class = self.get_serializer_class(obj)
            serializer = serializer_class(obj)
            serialized_data.append(serializer.data)
        return response.Response(serialized_data)
