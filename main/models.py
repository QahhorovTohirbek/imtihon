from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.title


class About_us(models.Model):
    body = models.TextField()
    img = models.ImageField(upload_to='about_us/')

    def __str__(self) -> str:
        return self.body
    
    class Meta:
        verbose_name_plural = 'About Us'


class Service(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField(upload_to='service/')

    def __str__(self) -> str:
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField(upload_to='blog/')

    def __str__(self) -> str:
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    body = models.TextField()
    is_show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)