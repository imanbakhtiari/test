from django.shortcuts import render
import requests

def advice(request):
  # Make a GET request to the API
  url = "https://api.adviceslip.com/advice"
  response = requests.get(url)
  
  # Check for successful response
  if response.status_code == 200:
    data = response.json()
    advice_text = data["slip"]["advice"]
  else:
    advice_text = "Error: Could not retrieve advice."

  # Render the template with the advice text
  context = {"advice": advice_text}
  return render(request, "advice.html", context)


def dad_joke(request):
  # API endpoint URL
  url = "https://icanhazdadjoke.com/"
  headers = {"Accept": "application/json"}

  # Make a GET request with headers
  response = requests.get(url, headers=headers)

  # Check for successful response
  if response.status_code == 200:
    joke_data = response.json()
    dad_joke = joke_data["joke"]
  else:
    dad_joke = "Error: Could not retrieve a joke."

  # Render template with joke
  context = {"dad_joke": dad_joke}
  return render(request, "dad_joke.html", context)

def next_spacex_launch(request):
  # SpaceX API endpoint URL
  url = "https://api.spacexdata.com/v4/launches/next"

  # Make a GET request
  response = requests.get(url)

  # Check for successful response
  if response.status_code == 200:
    launch_data = response.json()
    mission_name = launch_data["name"]
  else:
    mission_name = "Error: Could not retrieve launch data."

  # Render template with mission name
  context = {"mission_name": mission_name}
  return render(request, "next_spacex_launch.html", context)


def random_cat_image(request):
  # Cat API endpoint URL
  url = "https://api.thecatapi.com/v1/images/search"
  headers = {"x-api-key": "YOUR_API_KEY"}  # Replace with your API key

  # Make a GET request with headers
  response = requests.get(url, headers=headers)

  # Check for successful response
  if response.status_code == 200:
    image_data = response.json()
    image_url = image_data[0]["url"]
  else:
    image_url = "Error: Could not retrieve image."

  # Render template with image URL
  context = {"image_url": image_url}
  return render(request, "random_cat_image.html", context)