from django.shortcuts import render

from .forms import AddToCheckout


def checkout(request):
    order_list = request.session.get("order") or []

    if request.method == "POST":
        form = AddToCheckout(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data.get("quantity")
            product_id = form.cleaned_data.get("product_id")
            command = form.cleaned_data.get("command")

            match command:
                case "Add":
                    session_product = request.session[product_id]
                    found_product = next((product for product in order_list
                                          if session_product["name"] == product["name"]),
                                         None)

                    if found_product:
                        found_product["quantity"] = quantity
                    else:
                        order_list.append({**session_product, "quantity": quantity})
                case "DeleteProduct":
                    order_list = [product for product in order_list
                                  if product["product_id"] != product_id]
                case "DeleteAll":
                    order_list = []

        request.session["order"] = order_list
        request.session.modified = True

    order = request.session.get("order") or []
    context = {
        "order": order
    }
    return render(request, "checkout/checkout.html", context)
