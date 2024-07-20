from django.db import models

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    recipes = models.JSONField(default=list)  # Store recipe IDs as a list of integers
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email