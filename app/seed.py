from faker import Faker
import random
from .models import *

fake=Faker()

def create_marks(n):
    student_obj=student.objects.all()
    for i in student_obj:
        subjects=subject.objects.all()
        for j in subjects:
            subjectmarks.objects.create(
                student=i,
                subject=j,
                marks=random.randint(0,100),
            )
    

def seed(n=10)->None:
    try:
        for i in range(0,n):
            dpt = Department.objects.all()
            ranndomindex=random.randint(0,len(dpt)-1)
            department=dpt[ranndomindex]
            student_id=f'stu-{random.randint(100,999)}'
            student_name=fake.name()
            student_email=fake.email()
            student_age=random.randint(20,30)
            student_address=fake.address()
            student_id_obj=studentid.objects.create(student_id=student_id)
            student_obj=student.objects.create(
                
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
            )

    except Exception as e:
        print(e)
        
        
