from rest_framework import serializers
from .models import Vacancy, Employee

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"
        read_only_fields = ("id", "created_at", "is_active","user")



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ('user',)
