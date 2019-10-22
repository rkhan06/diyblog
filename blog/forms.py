from django import forms
from django.forms import ModelForm, Textarea
from blog.models import Comment


class blogComment(forms.Form):
    blog_comment = forms.CharField(widget=forms.Textarea(
        attrs={'style': 'height : 50px; width : 400px',
               'placeholder': 'Enter Your comment'}),
        error_messages={
        'required': 'Please enter a comment'},
        label='',
        max_length=500)

    def clean_data(self):
        return self.cleaned_data['blog_comment']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': Textarea(attrs={'cols': 7, 'rows': 2}),
        }
