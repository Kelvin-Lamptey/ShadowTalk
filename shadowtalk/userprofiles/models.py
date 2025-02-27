from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator

class University(models.Model):
    name = models.CharField(max_length=200, unique=True)
    abbreviation = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Universities"

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    school = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
        null=True,
        blank=True
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
        null=True,
        blank=True
    )
    last_active = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=instance) 