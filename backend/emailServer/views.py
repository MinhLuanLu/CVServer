from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .emailServer import sendEmail



@api_view(['POST'])
def EmailServer(res):

    if res.method == 'POST':
        Name = res.data.get('Name')
        Email = res.data.get('Email')
        Subject = res.data.get('Subject')
        Message = res.data.get('Message')

        message = f'Name: {Name}\nEmail:{Email}\n\n{Message}'
       
        print(sendEmail(Subject, message))
        return Response({'message': "Message sent successfully!" }, status=status.HTTP_200_OK)
    
    return Response({'message': 'error'}, status=status.HTTP_400_BAD_REQUEST)