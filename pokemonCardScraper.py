#These imports allow for enter keys click(keys) and webdriver which is a chrome instance 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

#Creating a webdriver and loading a website 
driver = webdriver.Chrome()
driver.get("https://www.gamestop.com")

#This method locates the search bar by ID, inputs the string containing the search and submits to begin the search 
searchBar = driver.find_element(By.NAME,"q")
searchBar.send_keys("Prismatic Evolutions")
searchBar.submit()


#Locates the item we want by using find element 
#<a class="product-tile-link render-tile-link pdp-link" href="/toys-games/trading-cards/products/pokemon-trading-card-game-prismatic-evolutions-booster-bundle/418865.html" aria-label="Pokemon Trading Card Game: Prismatic Evolutions Booster Bundle" title="Pokemon Trading Card Game: Prismatic Evolutions Booster Bundle" data-gtmdata="{&quot;id&quot;:&quot;418865&quot;,&quot;url&quot;:&quot;/toys-games/trading-cards/products/pokemon-trading-card-game-prismatic-evolutions-booster-bundle/418865.html&quot;,&quot;name&quot;:&quot;Pokemon Trading Card Game: Prismatic Evolutions Booster Bundle&quot;,&quot;productPlatform&quot;:[],&quot;price&quot;:{&quot;base&quot;:&quot;29.99&quot;,&quot;sale&quot;:null,&quot;pro&quot;:&quot;28.49&quot;,&quot;min&quot;:null,&quot;max&quot;:null},&quot;availability&quot;:{&quot;readyToOrder&quot;:null,&quot;available&quot;:false,&quot;preorder&quot;:null,&quot;allowBOPS&quot;:false,&quot;allowSDD&quot;:false,&quot;isDigitalProduct&quot;:false},&quot;releaseDate&quot;:&quot;03/07/2025&quot;,&quot;bopsPromoCalloutSearchTile&quot;:&quot;<div style=\&quot;padding-top: 10px; font-size: 14px;border-top: 1px solid #EEE;\&quot;>\n<strong>Pros, Save $25 When You Buy $250+</strong><br>\nIn&amp;#8209;store or buy online &amp; pick up in&amp;#8209;store\n</div>&quot;,&quot;bopsPromoCalloutSearchTileAlternate&quot;:&quot;&amp;nbsp;&quot;,&quot;bopsPromoAlternate&quot;:null,&quot;badge&quot;:&quot;&quot;,&quot;image&quot;:{&quot;title&quot;:&quot;Pokemon Trading Card Game: Prismatic Evolutions Booster Bundle&quot;,&quot;base&quot;:&quot;https://media.gamestop.com/i/gamestop/20018824/Pokemon-Trading-Card-Game-Prismatic-Evolutions-Booster-Bundle?&quot;},&quot;ratings&quot;:{&quot;percentage&quot;:null,&quot;count&quot;:null},&quot;marketPrice&quot;:null,&quot;gradingProvider&quot;:null,&quot;providerGrade&quot;:null,&quot;mapProPrice&quot;:false}"></a>
driver.find_element(By.CSS_SELECTOR, 'a.product-tile-link render-tile-link pdp-link').click()