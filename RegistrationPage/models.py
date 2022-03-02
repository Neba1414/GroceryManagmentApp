from django.db import models
import uuid

class Project(models.Model):
    name = models.CharField(max_length = 100)
    email = models.TextField(null = True, blank = False)
    password = models.CharField(max_length = 2000, null = True, blank = False)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
