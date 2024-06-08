from rest_framework import serializers
from .models import User,FriendRequest
from django.contrib.auth import authenticate,get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['email'] = validated_data['email'].lower()
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        
        email = data.get('email', '').strip().lower()
        password = data.get('password', '')

       
        user = authenticate(username=email, password=password)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Credentials")


class FriendRequestSerializer(serializers.ModelSerializer):
    from_name=serializers.SerializerMethodField()
    class Meta:
        model = FriendRequest
        fields = '__all__'
    
    def get_from_name(self, obj):
        if obj.from_user is not None:
            return obj.from_user.username
        else:
            return None

class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']
