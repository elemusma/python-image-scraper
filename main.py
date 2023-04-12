import requests
from bs4 import BeautifulSoup
import os

# Make a directory for the images to be saved
if not os.path.exists('APCs'):
    os.makedirs('APCs')

# Send a GET request to the webpage
url = 'https://www.ems-wi.com/apcs/'
response = requests.get(url)

# Parse the webpage content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the divs with class 'bdt-gallery-thumbnail'
divs = soup.find_all('div', {'class': 'bdt-gallery-thumbnail'})

# Loop through each div and find the image source and title
for div in divs:
    img_src = div.find('img')['src']
    filename = img_src.split('/')[-1]
    
    # Save the image to the 'APCs' directory with the original filename
    with open(f"APCs/{filename}", "wb") as f:
        f.write(requests.get(img_src).content)
