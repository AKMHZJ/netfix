from django import forms
from .models import Service, ServiceRequest

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'field', 'price_per_hour']

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)
        if company:
            if company.field != 'All in One':
                self.fields['field'].choices = [(company.field, company.field)]
                self.fields['field'].initial = company.field
                self.fields['field'].widget.attrs['readonly'] = True


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['address', 'service_hours']
