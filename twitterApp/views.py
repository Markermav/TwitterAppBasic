from django.http import HttpResponse
from django.shortcuts import render
from .models import Posts

# Create your views here.

# tweets = [
#     {
#     'name': 'Mike',
#     'text' : 'Feeling Good'
# },
# {
#     'name': 'Rishitaki',
#     'text' : 'Feeling Sad'
# }
# ]

def base(request):
    return render (request, 'feed/base.html')


def home(request):
    context = {
        'tweets' : Posts.objects.all()
    }
    return render (request, 'feed/home.html', context)