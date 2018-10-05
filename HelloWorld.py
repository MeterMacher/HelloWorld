import requests

def scrape_html(url, filename="scraped_page.html"):
    try:
        req = requests.get(url)
        print(req.text)
        f = open("www/" + filename, "w")
        f.write(str(req.text))
        print("URL wurde in Datei geschrieben")
    except Exception as E:
        print(E)
    finally:
        f.close()


if __name__ == "__main__":
    url = "https://www.google.de"
    scrape_html(url)
