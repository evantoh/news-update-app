from django.db import models
import datetime as dt
from django.contrib.auth.models import User


class tags(models.Model):
    name = models.CharField(max_length=30) 

    def __str__(self):
        return self.name
# model to save the subscribers to the database
class NewsLetterRecipients(models.Model):
    name=models.CharField(max_length =30)
    email= models.EmailField()


from tinymce.models import HTMLField
class Article(models.Model):
    title=models.CharField(max_length=60)
    post=HTMLField()
    editor= models.ForeignKey(User)
    tags=models.ManyToManyField(tags)
    pub_date =models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/', null=True)

    @classmethod
    def today_news(cls):
        today=dt.date.today()
        news=cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls,date):
        news=cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news


class MoringaMerch(models.Model):
    name=models.CharField(max_length=40)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=20)