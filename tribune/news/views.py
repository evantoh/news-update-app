from django .http import HttpResponse
import datetime as dt
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
#create  your views.
def welcome(request):
    return render(request,'welcome.html')
def news_of_day(request):
    date = dt.date.today()
    # function to convert date object to find exact day
    return render(request,'all_news/today_news.html',{"date":date,})
    # day = convert_dates(date)
    # html =f'''
    #     <html>
    #         <body>
    #             <h1> News for {day} {date.day}-{date.month}-{date.year}</h1>
    #         </body>
    #     </html>
    #        '''
    # return HttpResponse(html)

# def convert_dates(dates):
#     #function that gets the weekday number for the date
#     day_number = dt.date.weekday(dates)

#     days = ['monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

#     #returning actual day of the week
#     day = days[day_number]
#     return day

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

    return render (request, 'all_news/past_news.html',{"date":date})


    # day = convert_dates(date)
    # html = f'''
    #     <html>
    #         <body>
    #             <h1>news for {day}{date.day}-{date.month}-{date.year}</h1>
    #         </body>

    #     </html>
    #         '''
    # return HttpResponse(html)
