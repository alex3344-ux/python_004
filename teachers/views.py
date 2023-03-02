from django.shortcuts import render, get_object_or_404
from django.utils.crypto import get_random_string

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from  django.urls import reverse_lazy

from .models import Teacher
from .forms import TeacherForm


# Create your views here.

class TeachersViews(LoginRequiredMixin, ListView):
    model = Teacher
    # template_name = 'teachers.html'
    template_name = 'teachers/teachers_list.html'
    context_object_name = 'teachers'

class TeacherViews(TemplateView):
    template_name = "teacher_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {"teacher": get_object_or_404(Teacher, pk=self.kwargs["pk"])}
        return context

class TeachersCreateView(CreateView):
    model = Teacher
    template_name = 'teachers/teachers_form.html'
    success_url = reverse_lazy('mainpage:mainpage')
    form_class = TeacherForm


class TeachersUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    template_name = 'teachers/teachers_form.html'
    success_url = reverse_lazy('teachers:teachers_list')
    form_class = TeacherForm

class TeachersDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'teachers/teachers_confirm_delete.html'
    success_url = reverse_lazy('mainpage:mainpage')