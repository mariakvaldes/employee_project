from django.core.management.base import BaseCommand
from employees.models import Employee, Department
from attendance.models import Attendance, Performance
from faker import Faker
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = "Seed database with fake employee data"

    def handle(self, *args, **kwargs):
        fake = Faker()
        departments = [Department.objects.create(name=fake.bs()) for _ in range(5)]

        for _ in range(50):
            dept = random.choice(departments)
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                date_joined=fake.date_between(start_date='-2y', end_date='today'),
                department=dept
            )
            for _ in range(10):
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_this_year(),
                    status=random.choice(['Present', 'Absent', 'Late'])
                )
                Performance.objects.create(
                    employee=emp,
                    rating=random.randint(1, 5),
                    review_date=fake.date_this_year()
                )
