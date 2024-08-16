from django import forms
from .models import UserProfile, Posting

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'occupation', 'age']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ['content']
        
    content = forms.CharField(widget=forms.Textarea, required=True)