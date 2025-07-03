from django.shortcuts import render
import random
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from django.core.cache import cache


import pdb

######################## Admin #######################
class AdminRegisterView(APIView):
    def get(self,request, pk=None):
        # # pdb.set_trace()
        # print(request)
        if pk:
            employee = AdminRegister.objects.get(pk=pk)
            serializer = AdminRegisterSerializer(employee)
            return Response(serializer.data)
        else:
            employees = AdminRegister.objects.all()
            serializer = AdminRegisterSerializer(employees, many=True)
        return Response(serializer.data)
    
    def post(self, request):

        # pdb.set_trace()
        # print(request)
        serializer = AdminRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self, pk):
        Attend = AdminRegister.objects.get(pk=pk)
        Attend.delete()
        return Response(status=400)
    
    def put(self, request, pk=None):
        # print(request)
        # pdb.set_trace()
        Attend = AdminRegister.objects.get(pk=pk)
        serializer = AdminRegisterSerializer(Attend, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    
class AdminLoginView(APIView):
    def post(self, request):
        if request:
            login_phone = request.data.get('username')
            login_password = request.data.get('password')
            user = AdminRegister.objects.get(username=login_phone,password=login_password)
            if user:
                return Response({'msg':'Login Successfully','Admin':user.id})
            else:
                return Response({'msg':'invalid credentials'})
            

####################### UserRegister #######################
class UserRegisterView(APIView):
    def get(self,request, pk=None):
        # # pdb.set_trace()
        # print(request)
        if pk:
            employee = UserRegister.objects.get(pk=pk)
            serializer = UserRegisterSerializer(employee)
            return Response(serializer.data)
        else:
            employees = UserRegister.objects.all()
            serializer = UserRegisterSerializer(employees, many=True)
        return Response(serializer.data)
    
    def post(self, request):

        # pdb.set_trace()
        # print(request)
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self, pk):
        Attend = UserRegister.objects.get(pk=pk)
        Attend.delete()
        return Response(status=400)
    
    def put(self, request, pk=None):
        # print(request)
        # pdb.set_trace()
        Attend = UserRegister.objects.get(pk=pk)
        serializer = UserRegisterSerializer(Attend, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    
class UserLoginView(APIView):
    def post(self, request):
        if request:
            login_phone = request.data.get('username')
            login_password = request.data.get('password')
            user = UserRegister.objects.get(username=login_phone,password=login_password)
            print(user,'************')
            if user:
                return Response({'msg':'Login Successfully','Admin':user.id})
            else:
                return Response({'msg':'invalid credentials'})
            

####################### Book #######################
class BookView(APIView):
    def get(self,request, pk=None):
        # # pdb.set_trace()
        # print(request)
        if pk:
            employee = Book.objects.get(pk=pk)
            serializer = BookSerializer(employee)
            return Response(serializer.data)
        else:
            employees = Book.objects.all()
            serializer = BookSerializer(employees, many=True)
        return Response(serializer.data)
    
    def post(self, request):

        # pdb.set_trace()
        # print(request)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self, pk):
        Attend = Book.objects.get(pk=pk)
        Attend.delete()
        return Response(status=400)
    
    def put(self, request, pk=None):
        # print(request)
        # pdb.set_trace()
        Attend = Book.objects.get(pk=pk)
        serializer = BookSerializer(Attend, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    

            

####################### BookRecord #######################
class BookRecordView(APIView):
    def get(self,request, pk=None):
        # # pdb.set_trace()
        # print(request)
        if pk:
            employee = BookRecord.objects.get(pk=pk)
            serializer = BookRecordSerializer(employee)
            return Response(serializer.data)
        else:
            employees = BookRecord.objects.all()
            serializer = BookRecordSerializer(employees, many=True)
        return Response(serializer.data)
    
    def post(self, request):

        # pdb.set_trace()
        # print(request)
        serializer = BookRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self, pk):
        Attend = BookRecord.objects.get(pk=pk)
        Attend.delete()
        return Response(status=400)
    
    def put(self, request, pk=None):
        # print(request)
        # pdb.set_trace()
        Attend = BookRecord.objects.get(pk=pk)
        serializer = BookRecordSerializer(Attend, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

            
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
