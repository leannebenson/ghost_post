from django import forms
from ghost_app.models import Boast_Roast


class PostForm(forms.ModelForm):
   class Meta:
       model = Boast_Roast
       fields = ['content', 'post_type']