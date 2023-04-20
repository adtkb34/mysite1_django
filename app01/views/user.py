from django.shortcuts import render, redirect

from app01 import models
from app01.utils.form import UserModelForm


def user_list(request):
    context = {}
    search_data = request.GET.get('q', '')
    if search_data:
        context['name__contains'] = search_data
    queryset = models.UserInfo.objects.filter(**context)
    return render(request, 'user_list.html', {'queryset': queryset})


def user_add(request):
    context = {
        'title': '新建用户'
    }
    if request.method == 'GET':
        form = UserModelForm()
        context['form'] = form
        return render(request, 'change.html', context)
    form = UserModelForm(data=request.POST)
    context['form'] = form
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'change.html', context)


