from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

# Create your models here.
class DrinkInfo(models.Model):
    name                = models.CharField(max_length=120)
    place_of_origin     = models.CharField(max_length=120, null=True, blank=True)
    description         = models.CharField(max_length=240, null=True, blank=True)
    slug                = models.SlugField(null=True, blank=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

def di_pre_save_reciever(sender, instance, *args, **kwargs):
    print('saving ', instance.name, '...')
    print(instance.timestamp)
    if not instance.slug:
        instance.name = 'Another Title'
        instance.slug = unique_slug_generator(instance)


# def di_post_save_reciever(sender, instance, *args, **kwargs):
#     print('saved ', instance.name, '.')
#     print(instance.timestamp)
#     # if not instance.slug:
#     #     instance.slug = unique_slug_generator(instance)
#     #     instance.save() 

pre_save.connect(di_pre_save_reciever, sender=DrinkInfo)

# post_save.connect(di_post_save_reciever, sender=DrinkInfo)