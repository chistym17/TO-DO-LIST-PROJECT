from django.db import models


class taskmodel(models.Model):
    task_title=models.CharField(max_length=30,default='')
    task_description=models.CharField(max_length=30)
    is_completed=models.BooleanField(default=False)