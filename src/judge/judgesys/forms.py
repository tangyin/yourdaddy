from django.forms import ModelForm
from .models import CarJudge

# Create the form class.


class CarJudgeForm(ModelForm):
    class Meta:
        model = CarJudge
        fields = ['series', 'purchase_year', 'mileage']