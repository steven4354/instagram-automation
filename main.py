import requests
from bs4 import BeautifulSoup


def get_profile_links(search_term):
  # Replace spaces in the search term with %20, which is the URL-encoded version of a space character
  search_term = search_term.replace(' ', '%20')
  # Use requests to send a GET request to the Instagram search page with the search term
  response = requests.get(
    f'https://www.instagram.com/explore/tags/{search_term}/')
  # Use BeautifulSoup to parse the HTML of the search page

  print("response ", response.text)

  with open('site.html', 'w') as file:
    # Write the string to the file
    file.write(response.text)

  soup = BeautifulSoup(response.text, 'html.parser')
  # Find all the anchor tags that link to profile pages
  profile_tags = soup.find_all('a', {'class': 'yCE8d'})
  # Extract the profile links from the anchor tags
  profile_links = [tag['href'] for tag in profile_tags]
  return profile_links


def get_profile_image(profile_link):
  # Use requests to send a GET request to the profile page
  response = requests.get(f'https://www.instagram.com{profile_link}')
  # Use BeautifulSoup to parse the HTML of the profile page
  soup = BeautifulSoup(response.text, 'html.parser')
  # Find the meta tag that contains the profile image URL
  image_tag = soup.find('meta', {'property': 'og:image'})
  # Extract the profile image URL from the meta tag
  profile_image_url = image_tag['content']
  return profile_image_url


profile_links = get_profile_links("Trent Hedge")
print(profile_links)
