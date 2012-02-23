# -*- coding: utf-8 -*-

from django import forms
from django.contrib.comments.forms import CommentForm

class pCMSCommentForm(CommentForm):
    name = forms.CharField(label=u"Όνομα", max_length=50)
    email = forms.EmailField(label=u"Email",required=False)
