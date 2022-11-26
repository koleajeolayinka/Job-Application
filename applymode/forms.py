from django import forms
from applybank.models import ApplyForm
from django.utils.translation import gettext_lazy as _


class ApplyForms(forms.ModelForm):
    class Meta:
        model = ApplyForm
        fields = '__all__'
        # exclude=['first_name']
        labels = {
            'submit_CV': _('Submit Resume/CV'),
            'first_name': _('Enter first name'),
            'last_name': _('Enter last name'),
            'email': _('Enter email'),
            'phone': _('Enter your phone number'),
            'current_company': _('Enter your current company'),
            'linkedin': _('Linkedin'),
            'github': _('Github URL'),
            'twitter': _('Twitter'),
            'portfolio': _('Portfolio'),
            'cover_letter': _('Cover Letter'),
            'Gender': _('Gender '),
            'race': _('Race'),
            'veteran_status': _('Enter your veteran status')
        }
        error_messages = {
            'submit_CV': {
                'required': _('Your Resume/CV is required ')
            },
            'first_name': {
                'required': _('Your first name is required')
            },
            'last_name': {
                'required': _('Your last name is required')
            },
            'email': {
                'required': _('Your email is required')
            },
            'phone': {
                'required': _('Your phone number is required')
            },
            'current_company': {
                'required': _('Your Current Company name is required')
            },
            'linkedin': {
                'required': _('Confirm your linkedin URL')
            }
        }

    # first_name = forms.CharField(max_length=100, required=False, validators=[])
    # last_name = forms.CharField(max_length=100, required=False )
    # email = forms.EmailField(max_length=100, required=False)

    # def cleaned_firstname(self):
    #     data = self.cleaned_data['first_name']
    #     if ',' in data:
    #         raise forms.ValidationError("invalid first name")
    #     return data
