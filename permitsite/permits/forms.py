from django import forms
from permits.models import Permit
from permits.logic import number_validation


class PermitCreateForm(forms.ModelForm):
    class Meta:
        model = Permit
        fields = ['car_number']


    def clean(self):
        super(PermitCreateForm, self).clean()
        car_number = self.cleaned_data.get('car_number')
        if not number_validation(car_number):
            self._errors['car_number'] = self.error_class([
                'Номер не соответствует стандарту'])

        return self.cleaned_data