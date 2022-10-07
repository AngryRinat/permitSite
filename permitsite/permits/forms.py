from django import forms
from permits.models import Permit
from re import match

rus_number = '/^[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}\d{2,3}$/ui'


class PermitCreateForm(forms.ModelForm):
    class Meta:
        model = Permit
        fields = ['car_number']


    def clean(self):
        super(PermitCreateForm, self).clean()
        car_number = self.cleaned_data.get('car_number')
        if len(car_number)>9:
            self._errors['car_number'] = self.error_class([
                'Номер не соответствует стандарту'])

        return self.cleaned_data