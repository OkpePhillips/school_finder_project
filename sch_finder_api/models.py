from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name,email,middle_name=None, password=None, is_staff=False, is_superuser=False):
        if not first_name:
            raise ValueError("First name cannot be empty")
        if not last_name:
            raise ValueError("Last name cannot be empty")
        if not email:
            raise ValueError("Email name cannot be empty")
        
        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.middle_name = middle_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save()

        return user


class User(AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    middle_name = models.CharField(verbose_name="Middle Name", max_length=255, null=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    password = models.CharField(max_length=255)
    current_degree = models.CharField(max_length=255, default=None, null=True)
    gender = models.CharField(max_length=255, default=None, null=True)
    nationality = models.CharField(max_length=255, default=None, null=True)
    dob = models.DateField(default=None, null=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

class School(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255, unique=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    degrees = models.CharField(verbose_name="Degrees Awarded", max_length=600)
    website = models.CharField(verbose_name="Website url", max_length=255)
    rating = models.DecimalField(
        verbose_name="Rating",
        max_digits=2,
        decimal_places=1,
        default=0,
        editable=False
    )
    image = models.ImageField(verbose_name="School Image", upload_to="school_images/", null=True, blank=True)

    def update_rating(self):
        reviews = self.review_set.all()
        if reviews:
            total_ratings = sum(review.rating for review in reviews)
            self.rating = total_ratings / reviews.count()
        else:
            self.rating = 0
        self.save()

class Scholarship(models.Model):
    title = models.CharField(verbose_name="Title", max_length=255, unique=True)
    description = models.TextField(verbose_name="Description", max_length=3000)
    benefit = models.CharField(verbose_name="Scholarship Benefits", max_length=255)
    link = models.CharField(verbose_name="Link to apply", max_length=255)


class Review(models.Model):
    school_id = models.ForeignKey('School', verbose_name="School", on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Description", max_length=3000)
    rating = models.IntegerField(verbose_name="Rating")


class Country(models.Model):
    """ Country Table """
    name = models.CharField(verbose_name="Country Name", max_length=255, unique=True)


class City(models.Model):
    """ City Table """
    name = models.CharField(verbose_name='City Name', max_length=200, unique=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='cities')
