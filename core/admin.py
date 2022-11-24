from django.contrib import admin
from core import models as core_models


class UserProfile(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "mobile_number",
        "user_roll",
        "gender",
    ]


class ProductDetails(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "price",
        "image",
    ]


class CartDetails(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
    ]


class AddressesDetails(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
        "full_name",
        "mobile_number",
        "pincode",
        "city",
        "state",
        "address_type",
    ]


admin.site.register(core_models.User, UserProfile)
admin.site.register(core_models.Product, ProductDetails)
admin.site.register(core_models.Cart, CartDetails)
admin.site.register(core_models.Addresses, AddressesDetails)
