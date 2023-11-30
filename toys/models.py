from django.db import models
from django.db.models import TextChoices

# Create your models here.

class Toy(models.Model):
    class Category(TextChoices):
        DOLL = 'DOLL'
        PUZZLE = 'PUZZLE'
        ELECTRONIC = 'ELECTRONIC'
        GAME = 'GAME'
        BASIC = 'BASIC'

    name = models.CharField(max_length=150, blank=False, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    category = models.CharField(max_length=50, choices=Category.choices, default=Category.BASIC)
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return "{} ({})".format(self.name, self.pk)

    class Meta:
        ordering = ('name',)
