from django.http import JsonResponse


def index(request,city_name):
    zip_code= "12345"
    return JsonResponse({"city_name": city_name, "zip_code": zip_code})