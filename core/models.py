from django.db import models
from main.models import BaseModel

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

from main import constant as main_constants


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **other_fields):

        if not email:
            raise ValueError("You must provide an email address")

        email = self.normalize_email(email)
        # normalize means after @ @ExAmPlE.CoM -> @example.com

        user = self.model(email=email)
        user.set_password(password)
        # set_password only creates a hashed password; it doesn't save the value in the database.
        # Call save() to actually save it.

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **other_fields):

        user = self.create_user(email=self.normalize_email(email), password=password)

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    mobile_number = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=main_constants.GENDER)
    user_roll = models.CharField(max_length=80, choices=main_constants.USER_ROLL)
    is_admin = models.BooleanField(default=False)
    # custome user model is_admin field use must be
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"  # django-admin page login through email & password
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name

    def get_user_details(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "mobile_number": self.mobile_number,
            "gender": self.gender,
            "user_roll": self.user_roll,
        }


class Product(BaseModel):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    price = models.PositiveIntegerField()
    image = models.ImageField()

    def get_product_details(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
        }


class Cart(BaseModel):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_ids = models.ManyToManyField(Product)


class Addresses(BaseModel):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    mobile_number = models.PositiveIntegerField()
    pincode = models.PositiveIntegerField()
    address = models.TextField(max_length=1000)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100, choices=main_constants.STATE)
    address_type = models.CharField(max_length=50, choices=main_constants.ADDRESS_TYPE)

    def get_address_details(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "mobile_number": self.mobile_number,
            "pincode": self.pincode,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "address_type": self.address_type,
        }
