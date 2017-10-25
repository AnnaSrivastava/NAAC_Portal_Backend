from django.db import models

# Create your models here.
from employee.models import Employee


class Subject(models.Model):
    name = models.CharField(verbose_name = "Subject Name",max_length=100)
    code = models.CharField(verbose_name = "Subject Code",max_length=100)
    credit = models.IntegerField(verbose_name = "Credit")

    class Meta:
        db_table = 'subject'

    class Meta:
        db_table = 'subject'


class SubjectsTaken(models.Model):
    employee = models.ForeignKey(to=Employee , verbose_name='Employee ID')
    subjects = models.ManyToManyField(to=Subject)
    year = models.CharField(verbose_name = "Year",max_length=4)
    school = models.CharField("School",max_length=100)

    class Meta:
        db_table = 'subjects_taken'
