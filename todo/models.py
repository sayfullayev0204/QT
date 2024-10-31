from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    main_image = models.ImageField(upload_to='images/', null=True, blank=True)  # Asosiy rasm
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    article = models.ForeignKey(Article, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')  # Qo'shimcha rasmlar
