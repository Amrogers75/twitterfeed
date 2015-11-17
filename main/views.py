from django.shortcuts import render
from django.views.generic.list import ListView
from main.models import Tweets
# Create your views here.


class TweetsListView(ListView):
    model = Tweets
    template_name = 'tweets_list.html'


"""

{% for object in object_list %}

   <h1>{{ object.screen_name }}</h1>

{% endfor %}

"""