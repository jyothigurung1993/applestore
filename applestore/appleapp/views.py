from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import ProductDetails, GenresDetails
import urllib, json
from django.shortcuts import render

def my_view(request):
    return render(request, "appleapp/index.html")

def read_json(json_data):
    json_data = json_data["results"][0]
    app_name = json_data.get("artistName", "")
    description = json_data.get("description", "")
    genres = json_data.get("genres", [])
    version = json_data.get("version", "")
    prices = json_data.get("price", 0.0)

    prod = ProductDetails(app_name=app_name, description=description, version=version, price=float(prices))
    prod.save()
    if genres:
        for genre in genres:
            gen = GenresDetails(name=genre)
            gen.save()
            prod.genres.add(gen)


def retire_json_file(request, product_id):
    product_id = product_id
    url_for_product = "https://itunes.apple.com/lookup"
    if product_id:
        product_url = url_for_product + "?id="+product_id

        response = urllib.request.urlopen(product_url)
        data = json.loads(response.read())

        read_json(data)
        return HttpResponse("Success")


