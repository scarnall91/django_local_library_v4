from django.shortcuts import render, get_object_or_404
from django.views import generic
from input.models import Resort, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
from input.forms import UpdateResort

# Create your views here.

def index(request):
    num_resorts = Resort.objects.all().count()
    num_choices = Choice.objects.count()
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_resorts':num_resorts,
        'num_choices':num_choices,
        'num_visits':num_visits,
    }
    return render(request,'index.html',context=context)

class ResortListView(generic.ListView):
    model = Resort

class ResortDetailView(generic.DetailView):
    model = Resort

def update_resort(request, pk):
    resort = get_object_or_404(resort,pk=pk)
    if request.method == 'POST':
        form = UpdateResort(request.POST)
        if form.is_valid():
            resort.beginner = form.cleaned_data['beginner']
            resort.save()
            return HttpResponseRedirect(reverse('updated'))
    else:
        beginner_current = 0.1
        form = UpdateResort(initial={'beginner':beginner_current})

    context = {
        'form':form,
        'resort':resort,
    }

    return render(request, 'input/update_resort.html', context)