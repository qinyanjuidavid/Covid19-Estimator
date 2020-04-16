from django.forms import ModelForm
from myapp.models import Covid19


class Covid19Form(ModelForm):
    class Meta:
        model=Covid19
        fields=("__all__")
