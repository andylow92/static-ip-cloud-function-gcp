import requests

def get_ip(request):
  """Fetches the external IP address of the Cloud Function."""
  url = "https://api.ipify.org?format=text"  # IP What's My IP service

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for non-200 status codes
    return response.text
  except requests.exceptions.RequestException as e:
    return f"Error: {e}"

# Handle HTTP requests
def hello_http(request):
  """Cloud Function entry point."""
  ip_address = get_ip(request)
  return f"Your Cloud Function IP address (from external service): {ip_address}"
