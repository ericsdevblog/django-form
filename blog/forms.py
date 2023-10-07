from django import forms
from django.contrib.auth.models import User
from .models import Tag, Post


# class PostForm(forms.Form):
#     title = forms.CharField(
#         max_length=255,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "mb-4 p-2 w-full bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300"
#             }
#         ),
#     )
#     content = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 "class": "mb-4 p-2 w-full bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300"
#             }
#         ),
#     )
#     image = forms.ImageField(
#         widget=forms.ClearableFileInput(
#             attrs={
#                 "class": "mb-4 p-2 w-full bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300"
#             }
#         ),
#     )
#     is_published = forms.BooleanField(
#         required=False,
#         widget=forms.CheckboxInput(attrs={"class": "mb-4"}),
#     )
#     user = forms.ModelChoiceField(
#         queryset=User.objects.all(),
#         widget=forms.Select(
#             attrs={
#                 "class": "mb-4 p-2 w-full bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300"
#             }
#         ),
#     )
#     tags = forms.ModelMultipleChoiceField(
#         queryset=Tag.objects.all(),
#         widget=forms.SelectMultiple(
#             attrs={
#                 "class": "mb-4 p-2 w-full bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300"
#             }
#         ),
#     )


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "image", "is_published", "tags", "user"]
