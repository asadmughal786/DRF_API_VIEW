from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import studentModel
from .serializers import StudentSerializer
from rest_framework import status


# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def studentAPI(request,pk=None):
    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            stu = studentModel.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = studentModel.objects.all()
        students = StudentSerializer(stu, many=True)
        return Response(students.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data Inserted!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        # stu = studentModel.objects.get(pk = request.data.get('id'))
        stu = studentModel.objects.get(pk = pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data Updated Completely!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        # stu = studentModel.objects.get(pk = request.data.get('id'))
        stu = studentModel.objects.get(pk = pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data Updated Partialy!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        stu = studentModel.objects.get(pk = pk)
        stu.delete()
        return Response({'msg':'Student Deleted!'},status=status.HTTP_200_OK)
    
