from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://www.sportspunter.com/sports-betting/soccer/england/premier-league")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

matches = soup("a")


# Find all <td> tags, then find the <table> inside, followed by <tbody>, <tr>, and <td>
for td in soup.find_all('table'):
    # Find the table inside the <td>
    table = td.find('tbody')
    if table:
        # Find the <tbody> inside the <table>
        tbody = table.find('tr')
        if tbody:
            # Find all <tr> tags inside the <tbody>
            for tr in tbody.find_all('a'):
                for link in tr.find_all('a'):
                    print(f"Found link: {link.get('href')}, Text: {link.get_text(strip=True)}")