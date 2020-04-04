from bs4 import BeautifulSoup
from tabulate import tabulate
import matplotlib.pyplot as plt
import pandas as pd
import requests

page=requests.get("https://www.mohfw.gov.in/")
soup=BeautifulSoup(page.content,"html.parser")
state=soup.find(id="state-data")
# print(state)
result=state.find_all(class_="container")
# print(result[0])
print(result[0].find(class_="table table-striped").get_text())

print()

sno=[item.find(class_="table table-striped").get_text() for item in result]
sno=[item.find(class_="table table-striped").get_text() for item in result]
sno=[item.find(class_="table table-striped").get_text() for item in result]
sno=[item.find(class_="table table-striped").get_text() for item in result]
print(sno)

