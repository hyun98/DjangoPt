from django.shortcuts import render, redirect

# reverse : 함수형에서 사용  reverse_lazy : 클래스형에서 사용
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from accountapp.forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    
@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class AccountUpdateView(CreateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/update.html'
    

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'