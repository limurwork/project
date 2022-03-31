from .models import EmployeeDetails, Mart
from django.forms import ModelForm, TextInput


class Marta(ModelForm):
    class Meta:
        model = Mart
        fields = ['Addres_Hause', 'Namber_Apartmens', 'ownership', 'Name','Date_Of_Birth', 'Place_Of_Birth', 'Dokument_Right','personal_account','Size_Apartment',]
        widgets = {
            'Addres_Hause': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите Текст'
            }),
            'Namber_Apartmens': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите Текст'
            }),
            'ownership': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите Дату'
            }),
            'Name': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите Дату'
            }),
            'Date_Of_Birth': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите Дату'
            }),
            'Place_Of_Birth': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите Текст'
            }),
            'Dokument_Right': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите Текст'
            }),
            'personal_account': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите Текст'
            }),
            'Size_Apartment': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите Текст'
            }),

        }

class Detalis(ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = ['Contract', 'subject_contract', 'date_contract', 'end_contract', 'href_cloud',]
        widgets = {
            'Contract': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите Текст'
            }),
            'subject_contract': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите Текст'
            }),
            'date_contract': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите Дату'
            }),
            'end_contract': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите Дату'
            }),
            'href_cloud': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите Текст'
            }),

        }