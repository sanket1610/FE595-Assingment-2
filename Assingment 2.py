import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

name = []
purpose = []


def webscraper():
    for i in range(50):
        resp = requests.get("http://18.207.92.139:8000/random_company")
        soup = BeautifulSoup(resp.content, "html.parser")
        item = soup.find_all("li")
        for i in range(len(item)):
            if item[i].get_text().split()[0] == "Name:":
                name.append(item[i].get_text()[6:])

        for i in range(len(item)):
            if item[i].get_text().split()[0] == "Purpose:":
                purpose.append(item[i].get_text()[9:])
        time.sleep(1)


if __name__ == "__main__":
    webscraper()
    df = pd.DataFrame({"Name": name, "Purpose": purpose})
    df.to_csv("napu")
