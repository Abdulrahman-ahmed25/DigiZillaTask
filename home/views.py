from django.shortcuts import render
import requests

# Create your views here.
def calculate_distance(request):
    apiKey ="EExkOwIIVe9hg6R0l0Z12ZJrR2tl6"
    # origins = "51.4822656,-0.1933769"
    # destinations="51.4994794,-0.1269979"
    origin = request.POST.get('origin')
    destination=request.POST.get('destination')
    url_for_origin = f"https://api.distancematrix.ai/maps/api/geocode/json?address={origin}&key={apiKey}"
    response1 = requests.get(url_for_origin)
    origin_content = response1.json()['result'][0]['geometry']['location']
    origin_lat = origin_content['lat']
    origin_lng = origin_content['lng']
    # print(origin_lat)
    # print(origin_lng)

    url_for_destination = f"https://api.distancematrix.ai/maps/api/geocode/json?address={destination}&key={apiKey}"
    response2 = requests.get(url_for_destination)
    destination_content = response2.json()['result'][0]['geometry']['location']
    destination_lat = destination_content['lat']
    destination_lng = destination_content['lng']
    # print(destination_lat)
    # print(destination_lng)
    url_distance = f"https://api.distancematrix.ai/maps/api/distancematrix/json?origins={origin_lat},{origin_lng}&destinations={destination_lat},{destination_lng}&key={apiKey}"
    response3 = requests.get(url_distance)
    distance_content = response3.json()['rows'][0]['elements'][0]
    context = {
        'distance': distance_content['distance']['text'],
        'duration' : distance_content['duration']['text'],
        'origin': origin,
        'destination':destination
    }
    return render(request, 'home/calculate_distance.html', context)