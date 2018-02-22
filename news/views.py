from django .http import HttpResponse
import datetime as dt
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
from . models import Article 
#create  your views.
# def welcome(request):
#     return render(request,'welcome.html')
def news_of_day(request):
    date = dt.date.today()
    news = Article.today_news()
    # function to convert date object to find exact day
    return render(request,'all_news/today_news.html',{"date":date,"news":news})



# view function to present news from past days
def past_days_news(request,past_date):
    try:
    # convert data from the String url
        date=dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueEror is thrown
        raise Http404()
        assert   False

    if date == dt.date.today():
        return redirect(news_of_day)

        news = Article.days_news(date)

    return render (request, 'all_news/past_news.html',{"date":date,"news":news})


 
def search_results(request):
    
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all_news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_news/search.html',{"message":message})


def article(request,article_id):
    try:
        article=Article.objects.get(id=article_id)
    except DoesNotExist:
            raise Http404()

    return render(request,"all_news/article.html",{"article":article})   