from django.forms import ModelForm
from .models import M

class motosForm(ModelForm):
    class Meta:
        model = M
        fields = '__all__'