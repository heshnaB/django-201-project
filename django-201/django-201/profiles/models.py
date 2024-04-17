from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField

class Post(models.Model):
    text = models.CharField(max_length=100, blank=False, null=False)
    image = ImageField()
    
    def __str__(self):
        return self.text

class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = ImageField(upload_to='profiles', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    username = models.CharField(max_length=150, unique=True, default="")
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a new Profile() object when a Django User is created."""
    if created:
        username = instance.email.split('@')[0]  # Extract username from email
        counter = 1
        # Check if the generated username already exists
        while Profile.objects.filter(username=username).exists():
            username = instance.email.split('@')[0] + str(counter)
            counter += 1
        Profile.objects.create(user=instance, username=username)
    else:  # If the user already exists, ensure the username is unique
        if not instance.profile.username:
            username = instance.email.split('@')[0]  # Extract username from email
            counter = 1
            # Generate unique username if needed
            while Profile.objects.filter(username=username).exists():
                username = instance.email.split('@')[0] + str(counter)
                counter += 1
            instance.profile.username = username
            instance.profile.save()