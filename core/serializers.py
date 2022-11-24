from rest_framework import serializers

from core import models as core_models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.User
        fields = (
            "first_name",
            "last_name",
            "email",
            "mobile_number",
            "gender",
            "user_roll",
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.Product
        fields = ("user_id", "name", "price", "image")


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.Cart
        fields = ("user_id", "product_ids")


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.Addresses
        fields = (
            "user_id",
            "full_name",
            "mobile_number",
            "pincode",
            "address",
            "city",
            "state",
            "address_type",
        )
