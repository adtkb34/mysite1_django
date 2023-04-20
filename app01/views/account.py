from io import BytesIO
from django.shortcuts import render, redirect, HttpResponse

from app01.models import UserInfo
from app01.utils.code import check_code
from app01.utils.form import UserloginModelForm


def login(request):
    if request.method == 'GET':
        form = UserloginModelForm()
        return render(request, 'login.html', {'form': form})
    form = UserloginModelForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'login.html', {'form': form})
    code = request.session.get('image_code', '')
    user_input_code = form.cleaned_data.pop('code')
    if code.upper() != user_input_code.upper():
        form.add_error("code", "验证码错误")
        return render(request, 'login.html', {'form': form})
    userInfo = UserInfo.objects.filter(**form.cleaned_data).first()
    if userInfo:
        request.session['info'] = {'name': userInfo.name}
        # session可以保存7天
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect('/user/list/')
    form.add_error("password", "用户名或密码错误")
    return render(request, 'login.html', {'form': form})

def image_code(request):
    img, code_string = check_code()

    request.session['image_code'] = code_string

    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())

def logout(request):
    request.session.clear()
    return redirect('/login/')
