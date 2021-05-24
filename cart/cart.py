


class Cart():
    """
    The base Cart classe, that provide some default functionalities which
    can be inherited or overrided if necessary.
    """
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, product, qty):
        """
        User's Cart session data: Add, update
        """
        product_id = product.id

        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'qty':int(qty)}

        self.session.modified = True

    def __len__(self):
        """
        Get the cart data and count the number of products
        """
        return sum(item['qty'] for item in self.cart.values())