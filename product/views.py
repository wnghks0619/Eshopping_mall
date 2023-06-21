
from .models import Product
from django.views.generic.edit import FormView


class ProductRegister(FormView):
    template_name = 'product_register.html'
    success_url = '/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            stock=form.data.get('stock'),
            description=form.data.get('description')
        )
        product.save()
        return super().form_valid(form)

