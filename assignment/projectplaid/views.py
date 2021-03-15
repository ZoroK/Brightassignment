from django.shortcuts import render
from .serializers import UserRegisterSerializer,UserLoginSerializer,PublicExchangeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.


class RegisterUser (APIView):

    def post(self,request):
        serializer= UserRegisterSerializer(data=request.data)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class LoginUser (APIView):

    def post(self,request):
        serializer= UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            return JsonResponse({"message": "User Login Successful"})
        
        return JsonResponse({"message": "User Login Unsuccessful"})


class ExchangePublicToken (APIView):
    def post(self,request):

        serializer_class = PublicExchangeSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)
