from django.shortcuts import render, redirect, get_object_or_404
from .models import Dsu

def home(request):
    dsu = Dsu.objects.all()
    return render(request, 'home.html', {'Dsu': dsu})

def add_to_cart(request, book_id):
    book = get_object_or_404(Dsu, id=book_id)

    # Retrieve cart from session or create a new one
    cart = request.session.get('cart', {})

    if str(book_id) in cart:
        cart[str(book_id)]['quantity'] += 1  # Increase quantity if exists
    else:
        cart[str(book_id)] = {
            'name': book.name,
            'price': float(book.price),
            'quantity': 1
        }

    request.session['cart'] = cart  # Save the cart to session
    return redirect('cart_view')  # Redirect to cart page

def cart_view(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'cart': cart})

def remove_from_cart(request, book_id):
    """Remove an item from the cart"""
    cart = request.session.get('cart', {})

    if str(book_id) in cart:
        del cart[str(book_id)]  # Remove the item from the cart

    request.session['cart'] = cart  # Save updated cart
    return redirect('cart_view')
