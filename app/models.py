from django.db import models

class Department(models.Model):
    department= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    class Meta:
        ordering=['department']
class studentid(models.Model):
    student_id=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.student_id
    
class student(models.Model):
    department=models.ForeignKey(Department,related_name="depart",on_delete=models.CASCADE)
    student_id=models.OneToOneField(studentid,related_name="studentid",on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering=["student_name"]
        verbose_name="student"

class subject(models.Model):
    subject_name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name


class subjectmarks(models.Model):
    std=models.ForeignKey(student,related_name="studentmarks",on_delete=models.CASCADE)
    subject=models.ForeignKey(subject,on_delete=models.CASCADE)
    marks=models.IntegerField()

    def __str__(self) -> str:
        return f'{self.std.student_name} {self.subject.subject_name}'
    class Meta:
        unique_together=['std','subject']