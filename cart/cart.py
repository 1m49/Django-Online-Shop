class Cart:
    # Initialize the cart
    def __int__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    # add product to cart
    def add(self, product, quantity=1):
        product_id = str(product.id)

        if product.id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session.modified = True
