from django.http import JsonResponse


def index(request,zip_code):
    city_name = "test city name"
    return JsonResponse({"city_name": city_name, "zip_code": zip_code})