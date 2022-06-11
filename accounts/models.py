from django.db import models
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.
class UserAccount(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # pip install pillow to use this!
    bio = models.CharField(max_length=300, blank=True)
    profile_pic = models.ImageField(upload_to="media/profile_pics", blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.username

# class LikedGenre(models.Model):
#     genre = models.CharField(max_length=25)
#     users = models.ManyToManyField(UserAccount, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.genre
