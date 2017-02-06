from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile

from django.utils import timezone

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = {'username', 'email', 'password'}

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = {'website', 'picture'}

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=Category.name_max_length,
        help_text='Please enter the category name.'
    )

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(
        max_length=Page.title_max_length,
        help_text="Please enter the title of the page."
    )
    url = forms.URLField(
        max_length=Page.url_max_length,
        help_text="Please enter the URL of this page."
    )

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    last_visit = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now())
    first_visit = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now())

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data

    class Meta:
        model = Page
        exclude = ('category',)
