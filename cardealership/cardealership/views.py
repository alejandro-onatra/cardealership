# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from cardealership.cardealership.models import Car, Rental
from cardealership.cardealership.serializers import CarSerializer, RentalSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status




@csrf_exempt
@api_view(['GET','POST'])
def car_list( request ):

    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer( cars, many=True )
        return Response( serializer.data )

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CarSerializer( data=data )

        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK )

        return JsonResponse( serializer.errors, status=status.HTTP_404_NOT_FOUND )

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def car_detail( request, pk ):

    try:
        car = Car.objects.get( pk=pk )
    except Car.DoesNotExist:
        return HttpResponse( status=status.HTTP_404_NOT_FOUND )

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CarSerializer(car, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET','POST'])
def rental_list( request ):

    if request.method == 'GET':
        rental = Rental.objects.all()
        serializer = RentalSerializer( rental, many=True )
        return Response( serializer.data, safe=False )

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RentalSerializer( data=data )

        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )

        return Response( serializer.errors, status=status.HTTP_404_NOT_FOUND )

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def rental_detail( request, pk ):

    try:
        rental = Rental.objects.get( pk=pk )
    except Rental.DoesNotExist:
        return HttpResponse( status=status.HTTP_404_NOT_FOUND )

    if request.method == 'GET':
        serializer = RentalSerializer(rental)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RentalSerializer(rental, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        rental.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)