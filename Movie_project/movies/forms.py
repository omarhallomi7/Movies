# movies/forms.py
from django import forms
from .models import Review

# Review form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']

    RATING_CHOICES = [(i, i) for i in range(6)]  # Rating choices from 0 to 5

    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.Select)