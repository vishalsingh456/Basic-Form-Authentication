from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMultiAlternatives
from .serializers import *
# Create your views here.


class CreateUser(APIView):
    def post(self, request):
        data = request.data
        phone = data['phone']


        serializer = UserSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data, "msg":"User saved successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"data":[], "msg":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

