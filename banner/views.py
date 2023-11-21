from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.views.decorators.cache import cache_control, never_cache
from app1.models import *
from shopper.models import *
from django.db.models import Q


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def banner(request):
    if "admin" in request.session:
        banner = Banner.objects.all()
        context = {
            "banner": banner,
        }
        return render(request, "banner.html", context)

    else:
        return redirect("admin")


def add_banner(request):
    if "admin" in request.session:
        if request.method == "POST":
            description = request.POST.get("description")
            image = request.FILES.get("image")
            offer_description = request.POST.get("offer_description")
            banner = Banner(
                description=description,
                image=image,
                offer_description=offer_description,
            )
            banner.save()

            return redirect("banner")
        return render(request, "add_banner.html")
    else:
        return redirect("admin")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def edit_banner(request, banner_id):
    if "admin" in request.session:
        try:
            banner = Banner.objects.get(id=banner_id)
        except Banner.DoesNotExist:
            return render(request, "product_not_found.html")

        context = {
            "banner": banner,
        }

        return render(request, "edit_banner.html", context)
    else:
        return redirect("admin")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def update_banner(request, banner_id):
    banner = Banner.objects.get(id=banner_id)

    if request.method == "POST":
        banner.description = request.POST.get("description")
        image = request.FILES.get("image")
        banner.offer_description = request.POST.get("offer_description")

        if image:
            banner.image = image
        banner.save()

        return redirect("banner")
    else:
        context = {
            "banner": banner,
        }
        return render(request, "banner.html", context)


def delete_banner(request, banner_id):
    print(banner_id)
    try:
        banner = Banner.objects.get(id=banner_id)
        banner.delete()
    except Banner.DoesNotExist:
        return render(request, "category_not_found.html")

    return redirect("banner")


@never_cache
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def searchorder(request):
    # Get the 'q' parameter from the GET request
    query = request.GET.get("q", "")
    print(query)

    if query:
        # Perform a case-insensitive search on product names and descriptions
        orders = Order.objects.filter(
            models.Q(user__username__icontains=query)
            | Q(product__product_name__icontains=query)
        )
        # Set search_results to products filtered by the query
        search_results = orders

    context = {
        "orders": orders,
        "search_results": search_results,
    }

    return render(request, "ordersearch.html", context)
