from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

# Kenny added this on 11/26/21 for customzing what gets returned on logging in
# (obtaining the JWT)
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
         # The default result (access/refresh tokens)
        data = super().validate(attrs)

        # Custom data you want to include upon logging in
        data.update({
            'id': self.user.id,
            'email': self.user.email
        })
        
        # and everything else you want to send in the response
        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'id', 'email']
        depth = 1
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value