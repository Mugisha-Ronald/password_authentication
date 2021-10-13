from django.db.models import Q # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User,VehiclesTypes
from django.core.exceptions import ValidationError

from mapbox_location_field.models import LocationField
from uuid import uuid4



#from django.contrib.auth.hashers import make_password
from phonenumber_field.modelfields import PhoneNumberField

from django.core.validators import RegexValidator

ONLY_CHARS = RegexValidator(r'^[a-zA-Z]*$', "only characters allowed")

class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    first_name = serializers.CharField(
        required=True,
        validators = [ONLY_CHARS]
        )

    last_name = serializers.CharField(
        required=True,
        validators = [ONLY_CHARS]
        )

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    phone_number = PhoneNumberField()

    status_choices = (
        ("A","Active"),
        ("I","Inactive")
    )
    status = serializers.ChoiceField(choices = status_choices )


    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'password',
            'status',
            
        )

class UserLoginSerializer(serializers.ModelSerializer):
    # to accept either username or email
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True,
        required=True,style={'input_type': 'password', 'placeholder': 'Password'})
    token = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        # user,email,password validator
        email = data.get("email", None)
        password = data.get("password", None)
        if not email and not password:
            raise ValidationError("Details not entered.")
        user = None
        # if the email has been passed
        if '@' in email:
            user = User.objects.filter(
                Q(email=email) &
                Q(password=password)
                ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(email=email)
        else:
            user = User.objects.filter(
                Q(email=email) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(email=email)
        if user.ifLogged:
            raise ValidationError("User already logged in.")
        user.ifLogged = True
        data['token'] = uuid4()
        user.token = data['token']
        user.save()
        return data

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'token',
        )

        read_only_fields = (
            'token',
        )

class UserLogoutSerializer(serializers.ModelSerializer):
    token = serializers.CharField()
    status = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        token = data.get("token", None)
        print(token)
        user = None
        try:
            user = User.objects.get(token=token)
            if not user.ifLogged:
                raise ValidationError("User is not logged in.")
        except Exception as e:
            raise ValidationError(str(e))
        user.ifLogged = False
        user.token = ""
        user.save()
        data['status'] = "User is logged out."
        return data

    class Meta:
        model = User
        fields = (
            'token',
            'status',
        )




class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclesTypes
        fields = '__all__'