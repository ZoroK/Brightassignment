from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist


class UserRegisterSerializer (serializers.Serializer):
    email= serializers.EmailField(max_length=50)
    password= serializers.CharField(max_length=10)


    class Meta:
        model= User
        fields = ['email','password']

    def validate(self,data):
        email= data.get("email",None)

        password= data.get("password",None)

        if not email or not password :
            raise ValidationError("No Data")

        if User.objects.filter(email=email).exists():
            raise ValidationError("User already present")


        return super().validate(data)

    def create(self,data):
        return User.objects.create(**data)


        # isuser= None

        # try:
        #     isuser = User.objects.get(email=email)
        #     raise ValidationError("User already present")

        # except ObjectDoesNotExist:

class UserLoginSerializer (serializers.Serializer):
    email= serializers.EmailField(max_length=50)
    password= serializers.CharField(max_length=10)


    def validate(self,data):
        email= data.get("email",None)
        password= data.get("password",None)

        if not email and not password:
            raise ValidationError('Details not entered.')

        try:
            user= User.objects.get(email=email,password=password)

            if user.logged_in:
                raise ValidationError("User Already Logged")
            user.logged_in=True
            return data

        except:
            raise ValidationError("Login Details not correct")



    class Meta:
        model= User
        fields = ['email','password']




class PublicExchangeSerializer (serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    public_token = serializers.CharField()

    def validate(self, data):
        email=None
        publictoken=None

        email=data.get('email')
        publictoken=data.get('public_token')

        if not email or not publictoken:
            raise ValidationError('Invalid Details')

        user= None
        try:
            user= User.objects.get(email=email)


        except Exception:
            raise ValidationError('Something went wrong try again..')


        try:
            response = get_access_token.delay(public_token)
            user.access_token = response['access_token']
            user.item_id= response['item_id']
            user.save()

        except Exception:
            raise ValidationError('Sorry could not perform the operation')

        return exchange_response