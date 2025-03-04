from django.shortcuts import render


def product_list(request):
    return render(request, "product_list.html")


def product_detail(request, product_idx: int):
    return render(request, "product_detail.html", {"product_idx": product_idx})
