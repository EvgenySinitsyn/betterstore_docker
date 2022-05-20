from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import KeysValues
from datetime import datetime
from .serializers import JsonResponseSerializer, JsonResponse
import json


@api_view(['POST'])
def create_kye_value(request, KEY):
    if request.method == 'POST':
        KeysValues.objects.create(KEY=KEY, VALUE=json.loads(request.body.decode('utf-8')),
                                  unix_time=int(datetime.now().timestamp()))
        return Response(data={'status': status.HTTP_200_OK})


@api_view(['GET'])
def show_value(request, KEY):
    if request.method == 'GET':
        try:
            item = KeysValues.objects.get(KEY=KEY)
            value = item.VALUE
            unix_time = item.unix_time
        except Exception:
            value = None
            unix_time = None
        json_response = JsonResponse(value=value, timestamp=unix_time)
        serializer = JsonResponseSerializer(json_response)
        return Response(data=serializer.data)


@api_view(['DELETE'])
def delete_item(request, KEY):
    if request.method == 'DELETE':
        try:
            item = KeysValues.objects.get(KEY=KEY)
            item.delete()
            return Response()
        except Exception:
            raise exceptions.APIException("There is no item in the database with this key!")

