from django import forms
from posts.models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'post',
            'content',
        ]
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': '코멘트를 입력해주세요',
                'class': 'comment__textarea'
            })
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'content',
        ]
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': '게시할 내용을 입력해주세요',
                'class': 'comment__textarea'
            })
        }