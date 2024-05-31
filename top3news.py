import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# URL of the LiveMint webpage containing the news articles
url = "https://www.livemint.com/politics/news"

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all news articles
news_articles = soup.find_all("h2", class_="headline")

# Create a list to store the news data
news_items = []
for article in news_articles:
    title_tag = article.find("a")
    if title_tag:
        title = title_tag.get_text(strip=True)
        link = title_tag["href"]
        summary = ""  # Placeholder for summary (replace with actual summary if available)
        news_items.append({"title": title, "link": link, "summary": summary})

# Create the XML structure
root = ET.Element("news")
for item in news_items:
    news_element = ET.SubElement(root, "news_item")
    title_element = ET.SubElement(news_element, "title")
    title_element.text = item["title"]
    link_element = ET.SubElement(news_element, "link")
    link_element.text = item["link"]
    summary_element = ET.SubElement(news_element, "summary")
    summary_element.text = item["summary"]

# Convert XML data to bytes
xml_content = ET.tostring(root, encoding="utf-8")

# Save the XML data to a file
try:
    with open("top_news_livemint.xml", "wb") as file:
        file.write(xml_content)
    print("Data saved to top_news_livemint.xml")
except Exception as e:
    print(f"An error occurred while saving the XML file: {e}")
