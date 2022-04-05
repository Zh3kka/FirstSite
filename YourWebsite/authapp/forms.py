from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)

from .models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class UserEditForm(UserChangeForm):
    class Meta:
        fields = (
            "username",
            "first_name",
            "email",
            "password",
            "phone_number",
        )

        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""
            if field_name == "password":
                field.widget = forms.HiddenInput()


class UserRegisterForm(UserCreationForm):
    class Meta:
        fields = (
            "username",
            "first_name",
            "password1",
            "password2",
            "email",
        )
        model = User

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""
