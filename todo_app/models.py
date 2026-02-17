from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    is_submitted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
