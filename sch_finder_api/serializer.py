from rest_framework import serializers
from . import services
from .models import User, School


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    middle_name = serializers.CharField(required=False)
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    current_degree = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    nationality = serializers.CharField(required=False)
    dob = serializers.DateField(required=False)

    def to_internal_value(self, data):
        data =super().to_internal_value(data)

        return services.UserDataClass(**data)
    

class UserEditSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    last_name = serializers.CharField()
    current_degree = serializers.CharField()
    gender = serializers.CharField()
    nationality = serializers.CharField()
    dob = serializers.DateField()


class SchoolSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    country = serializers.CharField()
    city = serializers.CharField()
    degrees = serializers.CharField()
    website = serializers.CharField()
    money = serializers.IntegerField()
    rating = serializers.DecimalField(max_digits=2, decimal_places=1, read_only=True)

    def to_internal_value(self, data):
        data =super().to_internal_value(data)

        return services.SchoolDataClass(**data)

class EditSchoolSerializer(serializers.Serializer):
    name = serializers.CharField()
    country = serializers.CharField()
    city = serializers.CharField()
    degrees = serializers.CharField()
    website = serializers.CharField()
    money = serializers.IntegerField()


class ScholarshipSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    benefit = serializers.CharField()
    link = serializers.CharField()
    school = serializers.CharField()

    def to_internal_value(self, data):
        data =super().to_internal_value(data)

        return services.ScholarshipDataClass(**data)

class EditScholarshipSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    benefit = serializers.CharField()
    link = serializers.CharField()
    school = serializers.CharField()


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    school_id = serializers.PrimaryKeyRelatedField(queryset=School.objects.all().values_list('id', flat=True))
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    # user_id = UserSerializer(read_only=True)
    description = serializers.CharField(max_length=3000)
    rating = serializers.IntegerField()

    def to_internal_value(self, data):
        data =super().to_internal_value(data)

        return services.ReviewDataClass(**data)


class EditReviewSerializer(serializers.Serializer):
    description = serializers.CharField()
    rating = serializers.IntegerField()
