from django.db import models

class Editor(models.Model):
    first_name=models.CharField(max_length =30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    phone_number=models.CharField(max_length=10,blank=True)


    def __str__(self):
        return self.first_name

    def save_editor(self):
         self.save()  
          
class Meta:
    ordering=['first_name']   
# try:
#     editor= Editor.objects.get(email ='evanmwenda@gmail.com')
#     print('Editor found')
# except DoesNotExist:
#     print('Editor was not found')

class tags(models.Model):
    name = models.CharField(max_length=30) 

    def __str__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length=60)
    post=models.TextField()
    editor= models.ForeignKey(Editor)
    tags=models.ManyToManyField(tags)
    pud_date =models.DateTimeField(auto_now_add=True)