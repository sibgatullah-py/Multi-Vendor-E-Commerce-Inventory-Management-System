from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer): # Show user .
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            # Not including password right now cause it needs better understanding 
            "email",
            "role",
        )
            
class RegisterSerializer(serializers.ModelSerializer): # Create new user.
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            
        )
        # This does not hash the password , it only changes how serializer treats the field 
        # By this the serializer won't give the password when returning data 
        extra_kwargs = {
            "password": {
                "write_only":True
            }
        }