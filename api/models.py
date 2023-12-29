from django.db import models

# Create your models here.


class FormData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self) -> str:
        return f"{self.name} sent {self.subject}"
