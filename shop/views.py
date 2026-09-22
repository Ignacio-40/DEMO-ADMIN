from django.shortcuts import render

from django.contrib.auth.models import User
nuevo_usuario = User.objects.create_user(
    username="Juan"
    
)