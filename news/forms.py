# ipmort form module from django
from django import forms
from .models import Article

# creation of newsletter form that allows users to subscribe by creatoion of form class
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['editor','pub_date']
        widget ={
            'tags':forms.CheckboxSelectMultiple(),
        }