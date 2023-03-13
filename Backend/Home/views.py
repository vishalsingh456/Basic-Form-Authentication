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
        if len(phone) <10:
            return Response({"data":[], "msg":"Phone"}, status=status.HTTP_400_BAD_REQUEST)


        subject, from_email, to = 'Stack Fusion', 'stackfusiontest@gmail.com', data['email']
        text_content = 'Here is your content.'
        html_content = f"""<h1>
            Name : {data['name']}
            Email: {data['email']}
            Phone: {data['phone']}
            D.O.B: {data['dob']}
        </h1>"""
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        print(msg.send())
        serializer = UserSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data, "msg":"User saved successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"data":[], "msg":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)