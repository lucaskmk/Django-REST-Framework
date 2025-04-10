from django.db import models
#python manage.py runserver  
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Nome da tag (único)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, blank=True)  # Relação Many-to-Many com Tag
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}. {self.title}"