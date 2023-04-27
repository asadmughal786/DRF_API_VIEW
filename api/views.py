from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# @api_view()
# def hellow_world(request):
#     return Response({'msg':'Get method working By default'})

# @api_view(['GET'])
# def hellow_world(request):
#     return Response({'msg':'Get method working By default'})

# @api_view(['GET','POST'])
# def hellow_world(request):
#     if request.method == "GET":
#         return Response({'msg':'GET method working By default'})
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'POST method working',"data":request.data})




