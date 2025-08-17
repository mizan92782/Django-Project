from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Student
from .serializer import StudentSerializer

class ApiCall(APIView):
    #  JWT authentication 
    authentication_classes = [JWTAuthentication]

    # Define per-method permissions
    def get_permissions(self):
        if self.request.method == 'GET':
            # Only authenticated users can GET
            return [IsAuthenticated()]
        elif self.request.method == 'POST':
            # Only authenticated users can POST
            return [IsAuthenticated()]
        elif self.request.method in ['PUT', 'PATCH']:
            # Only authenticated users can update
            return [IsAuthenticated()]
        elif self.request.method == 'DELETE':
            # Only superusers can delete
            from rest_framework.permissions import IsAdminUser
            return [IsAdminUser()]
        return [IsAuthenticated()]

    # GET: list all students
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    # POST: create a new student
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT / PATCH: update a student
    def put(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: delete a student (superuser only)
    def delete(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



''' templates view'''
def home(request):
    return render(request,'home.html')

def login_view(request):
    return render(request, "login.html")