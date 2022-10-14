from django import forms

from core.models import Truck


class FindTrucksForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FindTrucksForm, self).__init__(*args, **kwargs)
        self.fields["side_number"] = forms.ModelChoiceField(
            queryset=Truck.objects.all(),
            label="Бортовой номер",
            required=False,
            empty_label="Все",
        )
