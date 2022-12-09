from django.contrib.auth.models import AbstractUser
from django.core.exceptions import *
from django.db import models
from django.core.validators import *



def validate_alphabetical_letters(value):
    if not value.isalpha():
        raise ValidationError('Only letters allowed')


class ShoppingCartUser(AbstractUser):
    MAX_LENGTH_GENDER = 15
    MAX_LENGTH_FIRST_NAME = 20
    MIN_LENGTH_FIRST_NAME = 3
    MAX_LENGTH_LAST_NAME = 20
    MIN_LENGTH_LAST_NAME = 3

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Do not show", "Do not show"),
    )

    first_name = models.CharField(max_length=MAX_LENGTH_FIRST_NAME,
                                  validators=[MinLengthValidator(MIN_LENGTH_FIRST_NAME), validate_alphabetical_letters],
                                  null=True, blank=True)
    last_name = models.CharField(max_length=MAX_LENGTH_LAST_NAME,
                                 validators=[MinLengthValidator(MIN_LENGTH_LAST_NAME), validate_alphabetical_letters],
                                 null=True, blank=True)
    email = models.EmailField(unique=True)
    profile_picture = models.URLField(null=True, blank=True)
    gender = models.CharField(max_length=MAX_LENGTH_GENDER, choices=GENDER_CHOICES, null=True, blank=True)
