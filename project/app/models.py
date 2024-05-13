from django.db import models

# Create your models here.
deptment=(
    ('Front End developer','Front End developer'),
    ('Back End Developer','Back End Developer'),
    ('UI designing','UI designing'),
    ('Deployment dep','Deployment dep')
)


class DepartmentModel(models.Model):
    Department=models.CharField(max_length=50, choices=deptment)models.CharField(max_length=50, choices=deptment)
    def __str__(self):
        return self.Department

position=(
    ('Team Member','Team Member'),
    ('Team Leader','Team Leader'),
    ('Manager','Manager'),
    ('FrontEnd Head','FrontEnd Head'),    
    ('BackEnd Head','BackEnd Head'),
    ('Deployment Head','Deployment Head')
)
class Positionmodel(models.Model):
    Position=models.CharField(max_length=50, choices=position)
    def __str__(self):
        return self

class EmployeeModel(models.model):
    Name=models.CharField(max_length=50)
    Department=models.OneToOneField(max_length=50)
    Position=models.OneToOneField(max_length=50)
    JoiningTime=models.DateTimeField()