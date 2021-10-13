from django.db import models
import datetime as dt


class Location(models.Model):
    location = models.CharField(max_length =60)

    def __str__(self):
        return self.location
    def save_location(self):
        self.save()


class Category(models.Model):
    category = models.CharField(max_length =60)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()
    

class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    image_path = models.ImageField(upload_to = 'articles/', null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

    def save_editor(self):
        self.save()