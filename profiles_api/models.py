from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """
    Manager for user profiles
    """
    def create_user(self,email,name,password=None):
        """
        Create a new user profile
        """
        if not email:
            raise ValueError("Users most have an email address")

        email=self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """
        Create and save a superuser with the given details
        """
        user = self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff = True
        user.save(using=self.db)

        return user


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model for users in the system
    """
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    #Authentication fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #Create a user profile manager
    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    #Create a method to retrive the full name of the user
    def get_full_name(self):
        """
        Retrive full name of the user
        """
        return self.name

    def get_short_name(self):
        """
        Retrive the short name of the user
        """
        return self.name

    def __str__(self):
        """
        Return string representation of the user
        """
        return self.email
