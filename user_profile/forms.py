from django.forms import ModelForm

from user_profile.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'gender', 'email', 'phone', 'birth_date']