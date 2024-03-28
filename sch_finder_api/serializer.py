from rest_framework import serializers
from . import services


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
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
    address = serializers.CharField()
    email = serializers.CharField()
    website = serializers.CharField()
    phone_number = serializers.IntegerField()

    def to_internal_value(self, data):
        data =super().to_internal_value(data)

        return services.SchoolDataClass(**data)

class EditSchoolSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    email = serializers.CharField()
    website = serializers.CharField()
    phone_number = serializers.IntegerField()

class ScholarshipSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    benefit = serializers.CharField()
    requirement = serializers.CharField()
    link = serializers.CharField()

    def to_internal_value(self, data):
        data =super().to_internal_value(data)

        return services.ScholarshipDataClass(**data)

class EditScholarshipSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    benefit = serializers.CharField()
    requirement = serializers.CharField()
    link = serializers.CharField()


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)