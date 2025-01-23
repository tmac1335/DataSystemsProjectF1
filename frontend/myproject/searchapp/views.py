from django.shortcuts import render
import requests

def search_view(request):
    response_data = None  # To hold the response from the external server
    if request.method == 'POST':
        query = request.POST.get('query', '')  # Get the query from the form
        if query:
            try:
                # Send POST request to the external URL
                url = "http://127.0.0.1:5000/"
                payload = {"query": query}
                response = requests.post(url, json=payload)  # Send JSON body
                response_data = response.json()  # Parse the response as JSON
            except requests.exceptions.RequestException as e:
                response_data = {"error": str(e)}  # Handle any request errors

    return render(request, 'searchapp/search.html', {"response": response_data})

def login(request):
    return render(request, 'searchapp/login.html')