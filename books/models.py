from django.db import models
# from accounts.models import UserAccount

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=125)
    auther = models.CharField(max_length=125)
    mode = models.CharField(max_length=11, default="public")
    tag = models.CharField(max_length=75)
    book_cover = models.ImageField(upload_to="media/book_covers", blank=True)
    description = models.CharField(max_length=500, blank=True)
    # user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
