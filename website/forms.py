from django import forms
from .models import UserProfile, Posting

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio', 'occupation', 'age'] #just added profile picture field 28/8/2024
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ['content']
        labels = {
            'content': '',   #removes the "content" placeholder beside the form
        }
        
    content = forms.CharField(widget=forms.Textarea, required=True)