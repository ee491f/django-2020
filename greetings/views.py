from django.views import generic
from django.urls import reverse_lazy
from .models import Greeting

# Create your views here.
from django.http import HttpResponse

class IndexView(generic.ListView):
    template_name = 'greetings/index.html'
    context_object_name = 'greeting_list'

    def get_queryset(self):
        """Return the all greetings."""
        return Greeting.objects.all()

class CreateView(generic.edit.CreateView):
    print("hi")
    template_name = 'greetings/create.html'
    model = Greeting
    fields = ['message']
    success_url = reverse_lazy('greetings:index') # more robust than hardcoding to /greetings/; directs user to index view after creating a greeting