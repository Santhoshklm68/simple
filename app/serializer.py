from rest_framework import serializers
from app.models import Employee

class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        # fields = ['emp_name', 'designation', 'phone_number']
        fields = '__all__'