from django.db import models
import uuid

class Post(models.Model):
    title = models.CharField(max_length=500) #charField has limit wherease textField() don't
    image = models.URLField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)