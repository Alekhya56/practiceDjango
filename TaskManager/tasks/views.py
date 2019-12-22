from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Tasks


def home(request):
    context = {
        'tasks': Tasks.objects.all()
    }
    return render(request, 'tasks/home.html', context)


class TaskListView(ListView):
    model = Tasks
    template_name = 'tasks/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'tasks'
    ordering = ['-date_posted']
    paginate_by = 5


class UserTaskListView(ListView):
    model = Tasks
    template_name = 'tasks/user_tasks.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Tasks.objects.filter(created_by=user).order_by('-date_posted')


class TaskDetailView(DetailView):
    model = Tasks

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Tasks
    fields = ['title', 'content', 'assigned_to', 'priority','state']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tasks
    fields = ['title', 'content','assigned_to','priority','state']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.created_by:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tasks
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.created_by:
            return True
        return False


def about(request):
    return render(request, 'tasks/about.html', {'title': 'About'})
