from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.by import By

# options = Options()
# options.binary_location = r'C:\Users\Piotr.Szczesniak\AppData\Local\Mozilla\firefox.exe'
browser = webdriver.Edge()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

