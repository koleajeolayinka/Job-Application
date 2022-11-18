from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        # exclude=['first_name']
        labels = {
            'first_name': _('Enter first name'),
            'last_mame': _('Enter last name'),
            'email': _('Enter email')
        }
        error_messages = {
            'first_name': {
                'required': _('Your first name is required')
            },
            'last_name': {
                'required': _('Your last name is required')
            },
            'email': {
                'required': _('Your email is required')
            }
        }

    # first_name = forms.CharField(max_length=100, required=False, validators=[])
    # last_name = forms.CharField(max_length=100, required=False )
    # email = forms.EmailField(max_length=100, required=False)

    def cleaned_firstname(self):
        data = self.cleaned_data['first_name']
        if ',' in data:
            raise forms.ValidationError("invalid first name")
        return data
