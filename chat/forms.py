from django.forms import Form, CharField, TextInput


class ComposeForm(Form):
    message = CharField(
            widget=TextInput(
                attrs={"class": "form-control"}
                )
            )
