from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name*"}
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email*"}
        )
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Your Comments*"}
        )
    )

    year = forms.DateField(
        widget=forms.SelectDateWidget(attrs={"class": "form-select"})
    )
