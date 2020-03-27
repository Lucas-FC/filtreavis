import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--verbose')

#Permet d'excuter le navigateur pour visiter la page TripAdvisor choisi

browser = webdriver.Chrome("D:/webdrivers/chromedriver.exe")
browser.get("https://www.tripadvisor.fr/Hotel_Review-g1373030-d1372921-Reviews-Alpha_hotel-Bouafle_Yvelines_Ile_de_France.html") 
sleep(5)

#Dérouler les avis, pour les scrapper en entier

plus = browser.find_element_by_xpath("//*/div/div[3]/div[4]/div[2]/div[3]/div[1]")
plus.click()
sleep(3)

#Extraire le txt des avis de la page

links = browser.find_elements_by_class_name("cPQsENeY")
print(links)
for value in links:
    print(value.text)
       
for value in links:
   links = str(value.text)

#Liste de mots clefs pour trier les avis négatifs (à améliorer).

avis = links.find('nul') and links.find('mauvais') and links.find('pas propre') and links.find('sale')

#Algorithme pas encore au point pour filtrer en fonction des mots clefs ci-dessus

for avis in range(10, 0):
    while avis == -1:
        continue 
if avis != -1:
    print('Commentaire négatif détecté')

if avis == -1:
    print("Commentaire normal")
else:
    print("Commentaire négatif détecté")

print(avis) #Affiche la valeur des avis (-1 ou placement du mots clefs detecté).

browser.quit()
