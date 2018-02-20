from django.test import TestCase
import datetime as dt
from .models import Editor,tags,Article
# Create your tests here.


class EditorTestClass(TestCase):
    # set up method
    def setUp(self):
        self.evans=Editor(first_name='evans',last_name='mwenda',email='evanmwenda@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.evans,Editor))

        # testing save method
    def test_save_method(self):
        self.evans.save_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors) > 0)




class ArticleTestClass(TestCase):

    def setUp(self):
        # creating a new editor and saving it
        self.evans=Editor(first_name='evans',last_name='mwenda',email='evanmwenda@gmail.com')
        self.evans.save_editor()

        # creating a new tag and saving it
        self.new_tag=tags(name='testing')
        self.new_tag.save()

        # creating a new article and saving i
        self.new_article = Article(title='test Article',post='this is a random test post',editor=self.evans)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)


    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news=Article.today_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date='2017-03-17'
        date = dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        news_by_date=Article.days_news(date)
        self.assertTrue(len(news_by_date)==0)
