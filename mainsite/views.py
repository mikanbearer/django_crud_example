from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Linkman
from .forms import LinkmanForm

# Create your views here.

# 列表
class LinkmanListView(LoginRequiredMixin, ListView):
    model = Linkman
    template_name = 'mainsite/linkman_list.html'

# 詳細
class LinkmanDetailView(LoginRequiredMixin, DetailView):
    model = Linkman
    template_name = 'mainsite/linkman_detail.html'

# 建立
class LinkmanCreateView(LoginRequiredMixin, CreateView):
    model = Linkman
    form_class = LinkmanForm
    template_name = 'mainsite/linkman_form.html'
    success_url = reverse_lazy('list')

# 更新
class LinkmanUpdateView(LoginRequiredMixin, UpdateView):
    model = Linkman
    form_class = LinkmanForm
    template_name = 'mainsite/linkman_form.html'
    success_url = reverse_lazy('list')

# 刪除
class LinkmanDeleteView(LoginRequiredMixin, DeleteView):
    model = Linkman
    template_name = 'mainsite/linkman_detail.html'
    success_url = reverse_lazy('list')