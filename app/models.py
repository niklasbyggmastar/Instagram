from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to="app/img/", default="")
    bio = models.TextField(max_length=300, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    liked_post_list = ArrayField(models.IntegerField(default=0, unique=True) ,size=50, blank=True, default=[])
    following = ArrayField(models.IntegerField(default=0, unique=True), size=500, blank=True, default=[])
    followers = ArrayField(models.IntegerField(default=0, unique=True), size=500, blank=True, default=[])

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Post(models.Model):
    user_name = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    text = models.CharField(max_length=100)
    img = models.ImageField(upload_to="app/img", default="")
    date = models.DateTimeField('date published', default=timezone.now)
    likes = models.IntegerField(default=0)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_name = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    text = models.CharField(max_length=100)
    date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.text
