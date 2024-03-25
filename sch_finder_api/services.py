import dataclasses
import datetime
import jwt
from .models import User, School
from django.conf import settings

@dataclasses.dataclass
class UserDataClass:
    first_name: str
    last_name: str
    email: str
    password: str = None
    id: int = None

    @classmethod
    def from_instance(cls, user:"User"):
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            id=user.id
        )

def create_user(user_dc:"UserDataClass"):
    instance = User(
        first_name=user_dc.first_name,
        last_name=user_dc.last_name,
        email=user_dc.email
    )
    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()

    return UserDataClass.from_instance(instance)

def get_user_by_email(email: str) -> "User":
    user = User.objects.filter(email=email).first()

    return user

def create_token(user_id: int) -> str:
    payload = dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        iat=datetime.datetime.utcnow()
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

    return token

def edit_user(user: "User", data):
    user.first_name = data["first_name"]
    user.last_name = data["last_name"]

    if data["password"] is not None:
        user.set_password(data["password"])

    user.save()

    return user

@dataclasses.dataclass
class SchoolDataClass:
    name: str
    address: str
    email: str
    website: str
    phone_number: int

    @classmethod
    def from_instance(cls, school:"School"):
        return cls(
            name=school.name,
            address=school.address,
            email=school.email,
            website=school.website,
            phone_number=school.phone_number
        )

def create_school(sch:"SchoolDataClass"):
    instance = School(
        name=sch.name,
        address=sch.address,
        email=sch.email,
        website=sch.website,
        phone_number=sch.phone_number
    )
    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()

    return UserDataClass.from_instance(instance)