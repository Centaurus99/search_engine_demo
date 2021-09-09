from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.db.models import Q
import time

from .models import Video, User, Comment


class VideoList(generic.ListView):
    model = Video
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_range'] = range(max(1, context['page_obj'].number - 3), min(
            context['page_obj'].paginator.num_pages + 1, context['page_obj'].number + 4))
        context['h1'] = '视频列表'
        context['h2'] = '共 {} 条视频'.format(Video.objects.count())
        context['title'] = 'bilibili 数码区视频列表'
        return context


class UpList(generic.ListView):
    model = User
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_range'] = range(max(1, context['page_obj'].number - 3), min(
            context['page_obj'].paginator.num_pages + 1, context['page_obj'].number + 4))
        context['h1'] = 'UP 列表'
        context['h2'] = '共 {} 名 UP 主'.format(User.objects.count())
        context['title'] = 'bilibili 数码区UP列表'
        return context


class VideoDetail(generic.DetailView):
    model = Video


class UpDetail(generic.ListView):
    template_name = 'searcher/user_detail.html'
    paginate_by = 8

    def get(self, request, *args, **kwargs):
        self._pk = self.kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Video.objects.filter(owner=self._pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_range'] = range(max(1, context['page_obj'].number - 3), min(
            context['page_obj'].paginator.num_pages + 1, context['page_obj'].number + 4))
        context['pk'] = self._pk
        context['object'] = User.objects.get(mid=self._pk)
        return context


class VideoSearch(generic.ListView):
    template_name = 'searcher/video_list.html'
    paginate_by = 8

    def setup(self, request, *args, **kwargs):
        self.__time = time.time()
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.search = self.request.GET.get('search')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Video.objects.filter(Q(title__contains=self.search) | Q(desc__contains=self.search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_range'] = range(max(1, context['page_obj'].number - 3), min(
            context['page_obj'].paginator.num_pages + 1, context['page_obj'].number + 4))
        self.__time = time.time() - self.__time
        context['search_time'] = round(self.__time, 4)
        context['h1'] = '视频搜索'
        context['h2'] = '在 {} 秒内找到 {} 条 "{}" 相关视频'.format(
            context['search_time'], context['page_obj'].paginator.count, self.search)
        context['title'] = '{} 相关视频搜索结果'.format(self.search)
        return context


class UpSearch(generic.ListView):
    template_name = 'searcher/user_list.html'
    paginate_by = 8

    def setup(self, request, *args, **kwargs):
        self.__time = time.time()
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.search = self.request.GET.get('search')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return User.objects.filter(Q(name__contains=self.search) | Q(sign__contains=self.search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_range'] = range(max(1, context['page_obj'].number - 3), min(
            context['page_obj'].paginator.num_pages + 1, context['page_obj'].number + 4))
        self.__time = time.time() - self.__time
        context['search_time'] = round(self.__time, 4)
        context['h1'] = 'UP 搜索'
        context['h2'] = '在 {} 秒内找到 {} 名 "{}" 相关 UP 主'.format(
            context['search_time'], context['page_obj'].paginator.count, self.search)
        context['title'] = '{} 相关UP主搜索结果'.format(self.search)
        return context
