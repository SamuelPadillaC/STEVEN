from django.db import models

# Create your models here.


class College(models.Model):
    def __str__(self):
        return self.Name
    Name = models.CharField(max_length=50, null=True)
    Location = models.CharField(max_length=50, null=True)
    Student_Slots = models.PositiveIntegerField(null = True)
    Domain = models.CharField(max_length=50, default="@example.edu")
    ISD_Email = models.EmailField(max_length=100, null=True)


#Inheritance
class ISD(models.Model):
    def __str__(self):
        return self.Name
    college = models.OneToOneField(College, null=True, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, null = True)

class Student(models.Model):
    def __str__(self):
        return self.Name
    college = models.ForeignKey(College, null=True, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, null = True)
    User_Email = models.EmailField(max_length=100, null=True)
    Nationality = models.CharField(max_length=50, null=True)
    Major = models.CharField(max_length=50, default = "Major")
    Language = models.CharField(max_length=50, default = "English")
    Age = models.PositiveIntegerField(null = True)
    #Progress
    