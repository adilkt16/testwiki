from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    slug=models.CharField(max_length=130)
    born=models.CharField(max_length=255)
    occupation=models.CharField(max_length=255)
    education=models.CharField(max_length=255)
    insta_link=models.CharField(max_length=255)
    main_description = models.TextField()
    career_description=models.TextField()
    image = models.ImageField(upload_to="profile_pics")

    dateTime=models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-dateTime']
    
    def __str__(self):
        # return str(self.name) + " Occupation : " + self.occupation
        return  " Occupation : " + self.occupation
    
    def get_absolute_url(self):
        return reverse('blogs')