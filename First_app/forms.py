from django import forms
from django.contrib.auth.models import User
from First_app.models import  UserProfileInfo


class FormName(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.ChoiceField(widget=forms.HiddenInput, required=False)

    def clean_botcatcher(self):

        botcatcher = self.cleaned_data['botcatcher']
        if(len(botcatcher) > 0):
            raise forms.ValidationError("gotcha bot!")
        return botcatcher


class NewFormUser(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')