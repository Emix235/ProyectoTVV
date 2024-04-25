from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'  # Esto incluirá todos los campos del modelo Game en el formulario
