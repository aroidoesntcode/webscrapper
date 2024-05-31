import requests
from bs4 import BeautifulSoup
import json

# URL of the Filmfare page for Bollywood movies from 2018
url = "https://www.filmfare.com/awards/filmfare-awards-2019/films-list-2018"

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all movie containers
movie_storage = soup.find_all("div", class_="list-text")

# Create a list to store the movie data
movies = []
for container in movie_storage:
    title_tag = container.find("a")
    if title_tag:
        title = title_tag.get_text(strip=True)
        year = 2018
        movies.append({"title": title, "year": year})

# Debug print to check if movies were extracted
print("Extracted Movies:", movies)

# Check if any movies were extracted
if not movies:
    print("No movies were extracted. Please check the class name or the structure of the webpage.")
else:
    # Save the movie data to a JSON file
    try:
        with open("bolly_movies2018.json", "w", encoding="utf-8") as file:
            json.dump(movies, file, indent=4, ensure_ascii=False)
        print("Data saved to bolly_movies2018.json")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
