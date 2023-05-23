from django.db import models

# Create your models here.
class Article(models.Model):
    titre= models.CharField(max_length=200)
    contenu= models.TextField()
    image= models.ImageField(upload_to="images", null=True)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
    
class Newsletter(models.Model):
    
    email= models.EmailField()

    def __str__(self):
        return self.email
        

 
