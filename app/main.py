from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import StringIO

# Set the headers to include a User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

url = 'https://www.sportspunter.com/sports-betting/soccer/england/premier-league'
response = requests.get(url, headers=headers)

# Parse the tables using BeautifulSoup and pandas
soup = BeautifulSoup(response.text, 'html.parser')
tables = pd.read_html(StringIO(str(soup)))

#tables is an array of tables, currently holds all the tables for the page above
# have a play around and see what tables represent what


i = 0
for table in tables:
    print(f"table no - '${i}' ",table.dropna(how="all"))
    i+=1
