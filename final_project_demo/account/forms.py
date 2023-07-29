from django import forms
from django.core.exceptions import ValidationError

from account.models import EmployerUser, JobSeekerUser


class EmployerRegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = EmployerUser
        fields = ['email', 'company_name', 'website']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise ValidationError('hasła nie są takie same')
        return cleaned_data

class JobSeekerRegisterForm(EmployerRegisterForm):
    class Meta:
        model = JobSeekerUser
        fields = ['email', 'name', 'surname']
