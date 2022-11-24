from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from core import models as core_models


class CustomJWTSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {"email": "", "password": attrs.get("password")}

        user_obj = core_models.User.objects.filter(email=attrs.get("email")).first()

        if user_obj.is_active:
            credentials["email"] = user_obj.email

        return super().validate(credentials)
