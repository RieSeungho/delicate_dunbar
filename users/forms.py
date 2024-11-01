from django import forms
from django.core.exceptions import ValidationError
from users.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={'placeholder': '사용자명 (3자리 이상)', 'class': 'input'}
        ),
    )
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
            attrs={'placeholder': '비밀번호 (4자리 이상)', 'class': 'input'}
        ),
    )

class SignupForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'placeholder': '사용자명 (3자리 이상)',
                'class': 'input',
                'id': 'username'}
        )
    )
    password1 = forms.CharField(
        min_length=4,
        widget=forms.TextInput(
            attrs={
                'placeholder': '비밀번호 (4자리 이상)',
                'class': 'input',
                'id': 'password1'}
        )
    )
    password2 = forms.CharField(
        min_length=4,
        widget=forms.TextInput(
            attrs={
                'placeholder': '비밀번호 확인 (4자리 이상)',
                'class': 'input',
                'id': 'password2'}
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '이메일 (example@email.com)',
                'class': 'input',
                'id': 'email'}
        )
    )
    profile_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={'class' : 'input', 'id': 'profile_image'}
        )
    )
    bio = forms.CharField(max_length=500, required=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"입력한 사용자명({username})은 이미 사용 중입니다")
        return username
    
    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            self.add_error('password2', '비밀번호와 비밀번호 확인란의 값이 다릅니다')

    def save(self):
        username = self.cleaned_data['username']
        password1 = self.cleaned_data['password1']
        email = self.cleaned_data['email']
        profile_image = self.cleaned_data['profile_image']
        bio = self.cleaned_data['bio']
        user = User.objects.create_user(
            username=username,
            password=password1,
            email=email,
            profile_image=profile_image,
            bio=bio
        )
        return user