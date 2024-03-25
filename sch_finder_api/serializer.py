from rest_framework import serializers
from . import services


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def to_internal_value(self, data):
        data =super().to_internal_value(data)

        return services.UserDataClass(**data)
    

class UserEditSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)


class SchoolSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    address = serializers.CharField()
    email = serializers.CharField()
    website = serializers.CharField()
    phone_number = serializers.IntegerField()

    def to_internal_value(self, data):
        data =super().to_internal_value(data)

        return services.UserDataClass(**data)
