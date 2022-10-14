from django import forms

from core.models import Truck, TruckModel


class FindTrucksForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FindTrucksForm, self).__init__(*args, **kwargs)
        self.fields["model"] = forms.ModelChoiceField(
            queryset=TruckModel.objects.all(),
            label="Модель",
            required=False,
            empty_label="Все",
        )
        self.fields["model"].label_from_instance = lambda obj: obj.name
