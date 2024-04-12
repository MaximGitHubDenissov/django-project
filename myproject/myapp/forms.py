from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label="Имя")
    description = forms.CharField(label="Описание товара", max_length=200,
                                  widget=forms.Textarea(attrs={'placeholder': 'Описание продукта'}))
    price = forms.DecimalField(label="Цена", max_digits=9, decimal_places=2)
    quantity = forms.IntegerField(label="Количество")
    image = forms.ImageField(label="Загрузите фото товара")
