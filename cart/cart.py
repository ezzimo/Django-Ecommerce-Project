from decimal import Decimal

from django.conf import settings
from Ecommerce_Store.models import Product


class Cart:
    """
    The base Cart classe, that provide some default functionalities which
    can be inherited or overrided if necessary.
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if settings.CART_SESSION_ID not in request.session:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, qty):
        """
        User's Cart session data: Add, update
        """
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]["qty"] = qty
        else:
            self.cart[product_id] = {"price": str(product.regular_price), "qty": int(qty)}

        self.save()

    def __iter__(self):
        """
        Get the product_id from the session's data and query the product information
        from database
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        """
        Get the cart data and count the number of products
        """
        return sum(item["qty"] for item in self.cart.values())

    def get_total_price(self):
        subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.cart.values())
        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            shipping = Decimal(11.50)

        total = subtotal + Decimal(shipping)
        return total

    def get_sub_total_price(self, product):
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]["total_price"] = str(
                Decimal(self.cart[product_id]["price"]) * self.cart[product_id]["qty"]
            )
        return self.cart[product_id]["total_price"]

    def delete(self, product):
        """
        delete product from session cart data
        """
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def update(self, product, qty):
        """
        Update values in cart session data
        """
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]["qty"] = qty
        self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        # remove session Cart data
        del self.session[settings.CART_SESSION_ID]
        self.save()
