from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.db.models import F
from django.urls import reverse

from .models import Position, Candidate

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'votes/index.html'
    context_object_name = 'position_list'

    def get_queryset(self):
        return Position.objects.order_by('-position_power')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['candidate_list'] = Candidate.objects.all().order_by('position')
        return context

def vote(request, position_id):
    position = get_object_or_404(Position, pk=position_id)
    try:
        selected_candidate = position.candidate_set.get(pk=request.POST['candidate'])
    except (KeyError, Candidate.DoesNotExist):
        # Redisplay the voting form
        return render(request, 'votes/index.html', {
            'position': position,
            'error_message': "You didn't select a candidate.",
        })
    else:
        selected_candidate.votes = F('votes') + 1
        selected_candidate.save()
        return HttpResponseRedirect(reverse('votes:index'))