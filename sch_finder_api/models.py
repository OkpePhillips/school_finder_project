from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, middle_name, last_name, email, password=None, is_staff=False, is_superuser=False):
        if not first_name:
            raise ValueError("First name cannot be empty")
        if not middle_name:
            raise ValueError("Middle name cannot be empty")
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
    middle_name = models.CharField(verbose_name="Middle Name", max_length=255)
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
    address = models.CharField(verbose_name="School Address", max_length=1000)
    email = models.EmailField(verbose_name="Contact Email", max_length=255)
    website = models.CharField(verbose_name="Website url", max_length=255)
    phone_number = models.IntegerField(verbose_name="Phone Number")

class Scholarship(models.Model):
    title = models.CharField(verbose_name="Title", max_length=255, unique=True)
    description = models.TextField(verbose_name="Description", max_length=3000)
    benefit = models.CharField(verbose_name="Scholarship Benefits", max_length=255)
    requirement = models.TextField(verbose_name="Application Requirements", max_length=1000)
    link = models.CharField(verbose_name="Link to apply", max_length=255)