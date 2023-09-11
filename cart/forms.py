from django import forms


# add to cart forms
class AddToCartProductForm(forms.Form):
    quantity_choices = [(i, str(i)) for i in range(1, 31)]

    quantity = forms.TypedChoiceField(choices=quantity_choices, coerce=int)

    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)
