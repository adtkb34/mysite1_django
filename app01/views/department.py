from django.shortcuts import render, redirect

from app01 import models
from app01.utils.form import departmentAddModelForm


def department_list(request):
    search_data = request.GET.get("q", '')
    context = {}
    if search_data:
        context['title__contains'] = search_data
    queryset = models.Department.objects.filter(**context)
    return render(request, 'department_list.html', {'queryset': queryset, 'query': search_data})


def department_add(request):
    context = {
        'title': '新增部门',
    }
    if request.method == 'GET':
        form = departmentAddModelForm()
        context['form'] = form
        return render(request, 'change.html', context)
    form = departmentAddModelForm(data=request.POST)
    context['form'] = form
    if form.is_valid():
        form.save()
        return redirect('/department/list/')
    return render(request, 'change.html', context)


def department_delete(request, nid):
    models.Department.objects.filter(id=nid).delete()
    return redirect('/department/list/')


def department_edit(request, nid):
    row_object = models.Department.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/department/list/')
    context = {
        'title': '编辑部门名称',
    }
    if request.method == 'GET':
        form = departmentAddModelForm(instance=row_object)
        context['form'] = form
        return render(request, 'change.html', context)
    form = departmentAddModelForm(instance=row_object, data=request.POST)
    context['form'] = form
    if form.is_valid():
        form.save()
        return redirect('/department/list/')
    return render(request, 'change.html', context)
