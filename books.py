import requests
import csv

url = "https://openlibrary.org/search.json?q=python"

response = requests.get(url)
data = response.json()

books = data["docs"][:20]

with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Author", "Year"])

    for book in books:
        title = book.get("title", "Unknown")
        author = book.get("author_name", ["Unknown"])[0]
        year = book.get("first_publish_year", "Unknown")

        writer.writerow([title, author, year])

print("books.csv ساخته شد!")
