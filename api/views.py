from unittest import result
from django.db import connection
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .models import Usersv2
from .serializers import Usersv2Serializer,Usersv2SerializerRangeFollowers

# Create your views here.
@api_view(['GET'])
def range_followers(request):
    min_value = request.data['min']
    max_value = request.data['max']
    if min_value is None or max_value is None:
        return Response({"error": "min and max are required"},status=status.HTTP_400_BAD_REQUEST)
    
    min_value,max_value = int(min_value), int(max_value)
    with connection.cursor() as cursor:
        cursor.execute('select * from get_range_of_followers(%s,%s);',[min_value, max_value]) # get_range_of_followers es una funcion
        users = cursor.fetchall()
        colums = [col[0] for col in cursor.description] # Obtener nombres de columnas
        users_dict = [dict(zip(colums,row)) for row in users] # Convertir en lista de diccionarios
    serializer = Usersv2SerializerRangeFollowers(users_dict, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def emails_by_domain(request):
    with connection.cursor() as cursor:
        cursor.execute('select * from count_emails_by_domain();') # count_emails_by_domain es una funcion
        result = cursor.fetchall()
        colums = [col[0] for col in cursor.description] # Obtener nombres de columnas
        results_dict = [dict(zip(colums,row)) for row in result] # Convertir en lista de diccionarios
    return Response(results_dict, status=status.HTTP_200_OK)

@api_view(['PUT'])
def reset_followers_followings(request):
    username = request.data['username'].strip()
    
    if username is None or not username:
        return Response({"error":"userna is required"},status=status.HTTP_400_BAD_REQUEST)
    
    with connection.cursor() as cursor:
        cursor.execute('CALL reset_followers_following(%s);',[username]) #reset_followers_following es un procedimiento
    
    user = Usersv2.objects.filter(username=username)
    
    serializer = Usersv2Serializer(user, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_followers_followings(request):
    follower_username = request.data['follower_username'].strip()
    followed_username = request.data['followed_username'].strip()
    
    if follower_username is None or not follower_username:
        return Response({"error":"follower_username is required"},status=status.HTTP_400_BAD_REQUEST)
    
    if followed_username is None or not followed_username:
        return Response({"error":"followed_username is required"},status=status.HTTP_400_BAD_REQUEST)
    
    Usersv2.objects.p_follow_user(follower_username,followed_username)

    
    return Response(status=status.HTTP_200_OK)
