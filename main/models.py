from django.db import models
import random

class Question(models.Model):
    text = models.CharField(max_length=50)
    answer = models.CharField(max_length=3)
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=7, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.color:
            self.color = self.generate_random_color()
        super().save(*args, **kwargs)
        
    def generate_random_color(self):
        return f"#{random.randint(0, 0xFFFFFF):06x}"
    
    def __str__(self):
        return self.text
