import requests

def check_status(url):
    if not url.startswith("http"):
        url = f"http://{url}"
    
    try:
        response = requests.get(url, timeout=3)
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        # Check the status code
        if response.status_code == 200:
            print("Success (200 OK!)")
        else:
            print("Failed. Check the code for more information.")
    except requests.exceptions.RequestException:
        print("Not connected successfully or request timed out.")

target_url = input("Enter a URL: ")
check_status(target_url)