
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        if User.USERNAME_FIELD == 'email':
            fields = ('email',)
        else:
            fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ResendActivationEmailForm(forms.Form):
    email = forms.EmailField(
        label='メールアドレス',
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
