from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product, Category
from django.core.mail import send_mail
from .forms import MtmForm
from .models import MtmOrder


def made_to_measure(request):
    """ A view to display the made to measure form """

    products = Product.objects.all()
    garment = request.GET["garment"]

    if "category" in request.GET:
        categories = request.GET["category"].split(",")
        products = products.filter(category__category_name__in=categories)

    context = {
        "products": products,
        "garment": garment,
    }

    return render(request, "made_to_measure/made_to_measure.html", context)


def mtm_form(request, product_id):
    """ A view to display and process the made to measure form """

    product = Product.objects.get(id=product_id)
    mtm_price = product.price * 3

    if request.method == "POST":

        form_data = {
            "order_total": mtm_price,
        }
        for entry in request.POST:
            if entry == "product":
                form_data["product"] = product
            elif entry != "csrfmiddlewaretoken":
                form_data[entry] = request.POST[entry]

        form = MtmForm(form_data)
        form.save()

        return redirect(reverse("products"))
    else:
        garment = request.GET["garment"]
        form = MtmForm()
        tops = ["Shirts", "Jackets", "Coats", "Waistcoats"]
        bottoms = ["Trousers", "Shorts"]

        if garment in tops:
            required_measurements = "tops"
        elif garment in bottoms:
            required_measurements = "bottoms"
        else:
            required_measurements = "both"

    context = {
        "product": product,
        "mtm_price": mtm_price,
        "garment": garment,
        "form": form,
        "required_measurements": required_measurements,
    }

    return render(request, "made_to_measure/mtm_form.html", context)