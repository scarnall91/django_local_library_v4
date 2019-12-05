from django import forms
from django.core.exceptions import  ValidationError
from django.utils.translation import ugettext_lazy

class UpdateResort(forms.Form):
    beginner = forms.IntegerField(help_text="Enter the new setting (minimum 0.1 max 0.9).")

    def clean_update_int(self):
        data = self.cleaned_date['beginner']
        #Check if the number is above 0 and below 1
        if data < 0 or data >=1:
            raise ValidationError(_('Invalid number - must be between 0 and 1'))
        return data

