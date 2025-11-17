from .models import Vacancy, Employee
from rest_framework.views import APIView
from datetime import datetime
from .serializers import VacancySerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status

class VacancyListCreateView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all().order_by("-id")
        title = request.query_params.get("t", None)
        if title:
            vacancies = vacancies.filter(title=title)
        date_obj = request.query_params.get("d", None)
        if date_obj:
            filter_date = datetime.strptime(date_obj, "%Y-%m-%d")
            vacancies = vacancies.filter(created_at__year=filter_date.year, created_at__month=filter_date.month, created_at__day=filter_date.day)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = VacancySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(user=request.user)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class VacancyRetriveUpdateDeleteView(APIView):
    def get(self, request, pk):
        vacancy = Vacancy.objects.filter(id=pk).first()
        if vacancy:
            serializer = VacancySerializer(vacancy)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Vacancy not found!"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        vacancy = Vacancy.objects.filter(id=pk).first()
        if vacancy:
            serializer = VacancySerializer(vacancy, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Vacancy not found"}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        vacancy = Vacancy.objects.filter(id=pk).first()
        if vacancy:
            serializer = VacancySerializer(vacancy, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Post not found"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vacancy = Vacancy.objects.filter(id=pk).first()
        if vacancy:
            try:
                vacancy.delete()
                return Response({"message":"Vacancy deleted"}, status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                return Response({"error":(e)}, status=status.HTTP_400_BAD_REQUEST)
            

class EmployeeListCreateView(APIView):
    def get(self, request):
        employees = Employee.objects.all().order_by("-id")
        profession = request.query_params.get("p", None)
        if profession:
            employees = employees.filter(profession__icontains=profession)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        employee = Employee.objects.filter(id=pk).first()
        if employee:
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Employee not found!"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        employee = Employee.objects.filter(id=pk).first()
        if employee:
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Employee not found!"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        employee = Employee.objects.filter(id=pk).first()
        if employee:
            serializer = EmployeeSerializer(employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Employee not found!"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        employee = Employee.objects.filter(id=pk).first()
        if employee:
            employee.delete()
            return Response({"message": "Employee deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Employee not found!"}, status=status.HTTP_404_NOT_FOUND)
