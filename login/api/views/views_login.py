from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string
from email.mime.text import MIMEText
import smtplib

from pymysql import DataError
from main_project import settings

#---------------------------------------------LOGOUT-----------------------------------------------#

from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import generics, status, permissions
#----------------------------------------------EXPIRED---------------------------------------------#

from django.http import HttpResponseRedirect
from datetime import datetime
#---------------------------------------------GENERAL----------------------------------------------#
from login.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from login.api.serializers.serializers_login import CustomTokenObtainPairSerializer
from login.api.serializers.serializers_users import CustomUserSerializer

from django.contrib.auth import authenticate
# from requests import request

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        data = {}
        data["status"] = status.HTTP_400_BAD_REQUEST
        try:
            print(request.data)
            username = request.data.get('username', '')
            password = request.data.get('password', '')
            user = authenticate(username=username,password=password)
            user_intento = User.objects.get(username=request.data['username'])
            login_serializer = self.serializer_class(data=request.data)
            if user_intento.is_active == True:
                if user:
                    if login_serializer.is_valid():
                        user_serializer = CustomUserSerializer(user)
                        data["data"] = {
                            'token': login_serializer.validated_data.get('access'),
                            'refresh-token': login_serializer.validated_data.get('refresh'),
                            'user': user_serializer.data,
                        }
                        data["type"] = "success"
                        data["msg"] = 'Inicio De Sesion Exitosa'
                        data["status"] = status.HTTP_200_OK
                    else:
                        data["status"] = status.HTTP_404_NOT_FOUND
                        raise ValueError('ha ocurrido un error')
                else:
                    raise ValueError("Contraseña no valida.")
            else:
                raise ValueError("Por favor activa tu cuenta.")
        except Exception as e:
            data["type"] = "error"
            data["msg"] = str(e)
        return Response(data, status = data["status"])


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST)
