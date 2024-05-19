from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Diary
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


@method_decorator(login_required, name='dispatch')
class DiaryPageView(ListView):
    model = Diary
    template_name = "diary.html"
    context_object_name = 'diary'
    ordering = ['-created_at']
    # Later add filter 
    def get_queryset(self):
        # Filter by the current user and public diaries
        return Diary.objects.filter(Q(user=self.request.user) | Q(privacy='public'))
    

@method_decorator(login_required, name='dispatch')
class DiaryDetailView(DetailView):
    model = Diary
    template_name = "diary_detail.html"


@method_decorator(login_required, name='dispatch')
class DiaryCreateView(LoginRequiredMixin,CreateView):
    model = Diary
    template_name = "diary_form.html"
    fields = ['title', 'feeling', 'thoughts_for_the_day', 'expectation', 'reflection', 'gratitude', 'privacy']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class DiaryUpdateView(LoginRequiredMixin, UpdateView):
    model = Diary
    template_name = "diary_form.html"
    fields = ['title', 'feeling', 'thoughts_for_the_day', 'expectation', 'reflection', 'gratitude', 'privacy']

    def dispatch(self, request, *args, **kwargs):
        diary = self.get_object()
        if diary.user != request.user:
            return redirect('diary_list')  # Redirect to diary list page if user is not the author
        return super().dispatch(request, *args, **kwargs)
    

@method_decorator(login_required, name='dispatch')
class DiaryDeleteView(DeleteView):
    model = Diary
    template_name = "diary_confirm_delete.html"

    def dispatch(self, request, *args, **kwargs):
        diary = self.get_object()
        if diary.user != request.user:
            return redirect('diary_list')  # Redirect to diary list page if user is not the author
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return '/diary/'

