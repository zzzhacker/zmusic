from django.db import models


class Album(models.Model):
    artisit=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    gener=models.CharField(max_length=100)
    album_logo=models.CharField(max_length=100)
    
    def __str__(self):
        return self.album_title+'-'+self.artisit
    
    
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    is_favourite=models.BooleanField(default=False)

    def __str__(self):
        return self.song_title