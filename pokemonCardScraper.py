#These imports allow for enter keys click(keys) and webdriver which is a chrome instance 
from selenium import webdriver

#Creating a webdriver and loading a website 
driver = webdriver.Chrome()
driver.get("https://www.gamestop.com/toys-games/trading-cards/products/pokemon-trading-card-game-prismatic-evolutions-booster-bundle/418865.html")

#Look for the button to indicate availability 
