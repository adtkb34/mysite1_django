
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms

from app01 import models
from app01.utils.encrypt import md5
from app01.utils.bootstrap import BootStrapModelForm


class departmentAddModelForm(BootStrapModelForm):
    class Meta:
        model = models.Department
        fields = ['title']

    def clean_title(self):
        txt_title = self.cleaned_data['title']
        if models.Department.objects.filter(title=txt_title).exists():
            raise ValidationError("该部门已存在")
        return txt_title


class UserModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "confirm_password", "age", 'account', 'create_time', "gender", "depart"]
        widgets = {
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }

    def clean_confirm_password(self):
        confirmPassword = md5(self.cleaned_data.get('confirm_password'))
        password = self.cleaned_data.get('password')
        if password != confirmPassword:
            raise ValidationError(f"密码不一致")
        return password

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return md5(password)


class UserloginModelForm(BootStrapModelForm):
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "code"]
        widgets = {
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }

