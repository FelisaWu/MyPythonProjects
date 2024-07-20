"""
File: webcrawler.py
Name: Felisa Wu
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        table = soup.find_all('td')
        male_num = 0
        female_num = 0
        for i in range(1, len(table)):
            if i % 5 == 3:
                male_num += int(table[i].text.replace(',', ''))
            if i % 5 == 0:
                female_num += int(table[i].text.replace(',', ''))
        print("Male Number:", male_num)
        print('Female Number:', female_num)


if __name__ == '__main__':
    main()
