## install ChromeDriver first

from selenium import webdriver

# Configuration du WebDriver (par exemple, Chrome)
driver = webdriver.Chrome()

# Ouvrir la page Indeed
driver.get('https://fr.indeed.com')

# Fermer le navigateur
driver.quit()
