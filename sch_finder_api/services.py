import dataclasses
import datetime
import jwt
from .models import User, School, Scholarship, Review, Country, City
from django.conf import settings
from django.shortcuts import get_object_or_404

@dataclasses.dataclass
class UserDataClass:
    first_name: str
    last_name: str
    middle_name: str
    email: str
    password: str = None
    id: int = None
    current_degree: str = None
    gender: str = None
    nationality: str = None
    dob: datetime = None

    @classmethod
    def from_instance(cls, user:"User"):
        return cls(
            first_name=user.first_name,
            middle_name=user.middle_name,
            last_name=user.last_name,
            email=user.email,
            id=user.id,
            current_degree=user.current_degree,
            gender=user.gender,
            nationality=user.nationality,
            dob=user.dob
        )

def create_user(user_dc:"UserDataClass"):
    instance = User(
        first_name=user_dc.first_name,
        middle_name=user_dc.middle_name,
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
    user.middle_name = data["middle_name"]
    user.last_name = data["last_name"]
    user.current_degree = data["current_degree"]
    user.gender = data["gender"]
    user.nationality = data["nationality"]
    user.dob = data["dob"]


    user.save()

    return user

@dataclasses.dataclass
class SchoolDataClass:
    name: str
    country: str
    city: str
    degrees: str
    website: str
    id: int = None

    @classmethod
    def from_instance(cls, school:"School"):
        return cls(
            name=school.name,
            country=school.country,
            city=school.city,
            degrees=school.degrees,
            website=school.website
        )

def create_school(sch:"SchoolDataClass"):
    instance = School(
        name=sch.name,
        country=sch.country,
        city=sch.city,
        degrees=sch.degrees,
        website=sch.website
    )
    instance.save()

    return SchoolDataClass.from_instance(instance)

def update_sch(id, data):
    try:
        school = School.objects.get(id=id)
        school.name = data["name"]
        school.country = data["country"]
        school.city = data["city"]
        school.degrees = data["degrees"]
        school.website = data["website"]

        school.save()

        return school
    except School.DoesNotExist:
        return response.Response(status=status.HTTP_404_NOT_FOUND)

@dataclasses.dataclass
class ScholarshipDataClass:
    title: str
    description: str
    benefit: str
    link: str
    school: str
    id: int = None

    @classmethod
    def from_instance(cls, ship:"Scholarship"):
        return cls(
            title=ship.title,
            description=ship.description,
            benefit=ship.benefit,
            link=ship.link,
            school=ship.school
        )

def create_scholarship(ship:"ScholarshipDataClass"):
    instance = Scholarship(
        title=ship.title,
        description=ship.description,
        benefit=ship.benefit,
        link=ship.link,
        school=ship.school
    )
    instance.save()

    return ScholarshipDataClass.from_instance(instance)

def update_scholarship(id, data):
    try:
        schship = Scholarship.objects.get(id=id)
        schship.title = data["title"]
        schship.description = data["description"]
        schship.benefit = data["benefit"]
        schship.link = data["link"]
        schship.school = data["school"]

        schship.save()

        return schship
    except Scholarship.DoesNotExist:
        return response.Response(status=status.HTTP_404_NOT_FOUND)


@dataclasses.dataclass
class ReviewDataClass:
    description: str
    rating: int
    school_id: ScholarshipDataClass = None
    user_id: UserDataClass = None
    id: int = None

    @classmethod
    def from_instance(cls, review:"Review"):
        return cls(
            school_id=review.school_id,
            user_id=review.user_id,
            description=review.description,
            rating=review.rating
        )

def create_review(school, user,review:"ReviewDataClass"):
    instance = Review(
        school_id=school,
        user_id=user,
        description=review.description,
        rating=review.rating
    )
    instance.save()

    return ReviewDataClass.from_instance(instance)


def update_review(id, data):
    try:
        review = Review.objects.get(id=id)
        review.description = data["description"]
        review.rating = data["rating"]

        review.save()

        return review
    except Review.DoesNotExist:
        return response.Response(status=status.HTTP_404_NOT_FOUND)
    

@dataclasses.dataclass
class CountryDataClass:
    name: str
    id: int = None

    @classmethod
    def from_instance(cls, country:"Country"):
        return cls(
            name=country.name
        )

def create_country(country:"CountryDataClass"):
    instance = Country(
        name=country.name,
    )
    instance.save()

    return CountryDataClass.from_instance(instance)


@dataclasses.dataclass
class CityDataClass:
    name: str
    country: CountryDataClass
    id: int = None

    @classmethod
    def from_instance(cls, city:"City"):
        return cls(
            name=city.name,
            country=city.country.name

        )

def create_city(country, city:"CityDataClass"):
    instance = City(
        name=city.name,
        country=country
    )
    instance.save()

    return CityDataClass.from_instance(instance)

def process_city_data(data):
    country_name = data.get('country')
    country = get_object_or_404(Country, name=country_name)
    data['country'] = country
    return data