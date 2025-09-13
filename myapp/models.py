from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=250,unique=True)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.name} {self.surname}'
    
class Video(models.Model):
    video_title = models.CharField(max_length=200)
    video_description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='video') 
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.video_title