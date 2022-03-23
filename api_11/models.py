from django.db import models

# Create your models here.


from django.db import models
from django.utils import timezone
 
class Task(models.Model):
    title=models.CharField(max_length=100)
    details=models.TextField()
    responsible_person = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100)
    project_id = models.IntegerField(default=0)
 
    def __str__(self):
        return self.title
