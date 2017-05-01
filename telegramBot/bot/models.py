from django.db import models


class UserTelegram(models.Model):
    name = models.CharField(max_length=50)
    cod = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Text(models.Model):
    user = models.ForeignKey(UserTelegram)
    text_file = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    user = models.ForeignKey(UserTelegram)
    image_file = models.ImageField(upload_to='uploads')
    created_at = models.DateTimeField(auto_now_add=True)


class Document(models.Model):
    user = models.ForeignKey(UserTelegram)
    document_file = models.FileField(upload_to='uploads')
    created_at = models.DateTimeField(auto_now_add=True)
