from django import forms
from tinymce import TinyMCE
from .models import Post, Comment
from django.contrib.auth.models import User
from .models import *


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return True


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCEWidget( attrs={'required': False, 'cols': 30, 'rows': 10}) )
    overview= forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 25, 'rows': 10}))

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail',
        'categories', 'featured', 'previous_post', 'next_post')


class CommentForm(forms.ModelForm):

    content = forms.CharField(widget=forms.textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('content', )



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('image','email','website','biography')