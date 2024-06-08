import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the website containing the download button
url = 'https://www.investing.com/55273798-e20b-4fcd-a666-11c62955a5c4'

# Sending a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website
soup = BeautifulSoup(response.content, 'html.parser')

# Find the download button based on its attributes
download_button = soup.find('button', {'class': 'download-button'})

if download_button:
    # Extract the URL associated with the download button
    download_url = download_button.get('data-download-url')

    # If the URL is relative, convert it to absolute URL
    if download_url and not download_url.startswith('http'):
        download_url = urljoin(url, download_url)

    # Send a GET request to download the file
    download_response = requests.get(download_url)

    # Save the file to disk
    with open('downloaded_file.zip', 'wb') as f:
        f.write(download_response.content)

    print("File downloaded successfully!")
else:
    print("Download button not found.")
