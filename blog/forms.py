from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm, widgets

from blog.models import Post
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model   = Post
        fields  = '__all__'
        labels = {'photo:':"",'title:':"Title:"}

        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control',"style":' margin-bottom: 20px'}),
            'content':forms.Textarea(attrs={'class':'form-control',"style":" margin-bottom: 20px"}),
        }