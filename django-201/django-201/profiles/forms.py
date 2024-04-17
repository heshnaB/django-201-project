from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile  
        fields = ['username', 'bio', 'image']
        
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username
        
    def save(self, commit=True):
        profile = super(ProfileEditForm, self).save(commit=False)
        new_username = self.cleaned_data.get('username')
        new_bio = self.cleaned_data.get('bio')
        new_image = self.cleaned_data.get('image')
        

        
        if new_username and new_username != profile.user.username:
            profile.user.username = new_username
            profile.user.save() 
        # Update profile bio
        profile.bio = new_bio

        # Update profile image
        if new_image:
            profile.image = new_image

        # Save changes
        if commit:
            profile.save()
        return profile
      