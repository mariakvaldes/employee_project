from rest_framework import serializers
from attendance.models import Attendance, Performance
from employees.serializers import EmployeeSerializer
from employees.models import Employee

class AttendanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Attendance
        fields = '__all__'

class PerformanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Performance
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        fields = '__all__'
