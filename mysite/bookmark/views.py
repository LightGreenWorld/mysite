from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin


# 1) bookmark_list.html 파일로 자동으로 연결
# 2) object_list를 html 파일로 전달
class BookmarkLV(ListView) :
    model = Bookmark

# 1) bookmark_detail.html 파일로 자동으로 연결
# 2) object를 html 파일로 전달
class BookmarkDV(DetailView) :
    model = Bookmark


#DetailView 상속
# 1) post_detail.html을 자동으로 참조
# 2) object를 post_detail.html에 전달

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')


class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')