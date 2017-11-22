from django.forms import ModelForm, HiddenInput, model_to_dict

from user_profile.models import Profile


def create_populated_profile_form(user):
    try:
        profile = user.profile
        data = model_to_dict(profile, fields=['user', 'avatar', 'bio', 'email', 'gender', 'phone', 'birth_date'])
    except:
        data = {"user": user.id}
    return ProfileForm(initial=data)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        widgets = {'user': HiddenInput()}
        fields = ['user', 'avatar', 'bio', 'gender', 'email', 'phone', 'birth_date']
