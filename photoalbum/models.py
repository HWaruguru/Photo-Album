from django.db import models
import datetime as dt


class Location(models.Model):
    location = models.CharField(max_length =60)

    def __str__(self):
        return self.location
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(location=value)


class Category(models.Model):
    category = models.CharField(max_length =60)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(category=value)
    

class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    image_path = models.ImageField(upload_to = 'images/', null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(category__category__icontains=category)
        return images

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location__icontains=location)
        return images
    