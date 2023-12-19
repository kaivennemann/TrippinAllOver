from django import forms


class BookingCriteriaForm(forms.Form):
    outbound_airport = forms.CharField(label="Outbound Airport", max_length=100)
