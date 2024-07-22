# db models

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,  # functionality for authentication system
    BaseUserManager,
    PermissionsMixin  # functionality for permissions and fields
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address!')
        # defining a new model with email normalization.
        user = self.model(email=self.normalize_email(email), **extra_fields)

        # sets encrypted password using hashing.
        user.set_password(password)

        # save the model into the db.
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # OVERRIDING USERNAME FIELD AS EMAIL FIELD.
    USERNAME_FIELD = 'email'
