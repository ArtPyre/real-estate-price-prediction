from selenium import webdriver
from selenium.webdriver.common.by import By
import data_filter_fr
import data_filter_en

def immoweb_scrapping(url):
    if("projet" in url or "project" in url):
        pass
    else :
        my_dict = dict()
        tab = url.split("/")
        my_dict["id"] = tab[-1]
        my_dict["Locality"] = tab[7].capitalize()

        if(tab[3] == "fr") :
            return immoweb_fr_scrapping(url, my_dict)
        elif(tab[3] == "en") :
            return immoweb_en_scrapping(url, my_dict)
        else :
            pass

def immoweb_fr_scrapping(url, my_dict):

    driver = webdriver.Chrome()
    driver.get(url)

    try :
        title = driver.find_element(By.XPATH, "//h1[@class='classified__title']").text
    except :
        return

    if(title.find("à vendre")>-1) :
        my_dict["Type of sale"] = "à vendre"
        my_dict.update(data_filter_fr.get_properties(title.replace(" à vendre", "")))
    elif(title.find("à louer")>-1) :
        my_dict["Type of sale"] = "à louer"
        my_dict.update(data_filter_fr.get_properties(title.replace(" à louer", "")))
    else :
        my_dict["Type of sale"] = None

    my_dict["Price_attr"] = driver.find_element(By.XPATH, "//p[@class='classified__price']//span[@class='sr-only']").text

    for key, value in zip(driver.find_elements(By.XPATH, "//th[@class='classified-table__header']"), driver.find_elements(By.XPATH, "//td[@class='classified-table__data']")):
        my_dict[key.text.replace("\n", "")] = value.text.replace("\n", "")

    driver.close()

    return data_filter_fr.immoweb_filter(my_dict)

def immoweb_en_scrapping(url, my_dict):

    driver = webdriver.Chrome()
    driver.get(url)

    try :
        title = driver.find_element(By.XPATH, "//h1[@class='classified__title']").text
    except :
        return
    
    if(title.find("for sale")>-1) :
        my_dict["Type of sale"] = "for sale"
        my_dict.update(data_filter_en.get_properties(title.replace(" for sale", "")))
    elif(title.find("for rent")>-1) :
        my_dict["Type of sale"] = "for rent"
        my_dict.update(data_filter_en.get_properties(title.replace(" for rent", "")))
    else :
        my_dict["Type of sale"] = None

    my_dict["Price"] = driver.find_element(By.XPATH, "//p[@class='classified__price']//span[@class='sr-only']").text

    for key, value in zip(driver.find_elements(By.XPATH, "//th[@class='classified-table__header']"), driver.find_elements(By.XPATH, "//td[@class='classified-table__data']")):
        my_dict[key.text.replace("\n", "")] = value.text.replace("\n", "")

    driver.close()

    return data_filter_en.immoweb_filter(my_dict)

'''links = [
    'https://www.immoweb.be/fr/annonce/villa/a-vendre/uccle/1180/10110650', 
    'https://www.immoweb.be/fr/annonce/maison/a-vendre/bruxelles/1120/10306539', 
    'https://www.immoweb.be/fr/annonce/maison-de-maitre/a-vendre/jette/1090/10212075', 
    'https://www.immoweb.be/fr/annonce/projet-neuf-maisons/a-vendre/woluwe-saint-pierre/1150/10303909', 
    'https://www.immoweb.be/fr/annonce/maison/a-vendre/woluwe-saint-pierre/1150/10306388', 
    'https://www.immoweb.be/fr/annonce/maison/a-vendre/woluwe-saint-lambert/1200/10306389', 
    'https://www.immoweb.be/fr/annonce/maison/a-vendre/molenbeek-saint-jean/1080/10303905', 
    'https://www.immoweb.be/fr/annonce/maison-bel-etage/a-vendre/jette/1090/10293277', 
    'https://www.immoweb.be/fr/annonce/maison/a-vendre/brussels/1000/10292629', 
    'https://www.immoweb.be/fr/annonce/immeuble-a-appartements/a-vendre/bruxelles/1000/10206439', 
    'https://www.immoweb.be/fr/annonce/maison/a-vendre/evere/1140/10096540']'''

'''links = [
    'https://www.immoweb.be/en/classified/apartment/for-rent/willebroek/2830/10309521',
    'https://www.immoweb.be/fr/annonce/maison/a-vendre/seraing-ougree/4102/10306386',
    'https://www.immoweb.be/fr/annonce/maison/a-vendre/molenbeek-saint-jean/1080/1033905',
    'https://www.immoweb.be/en/classified/house/for-sale/oupeye/4680/10302566',
    'https://www.immoweb.be/en/classified/house/for-sale/antwerpen/2140/10258718',
    'https://www.immoweb.be/fr/annonce/maison/a-louer/bornem/2861/10310205',
    'https://www.immoweb.be/fr/annonce/maison/a-louer/uccle/1180/10306699'
]'''

links = [
    'https://www.immoweb.be/en/classified/penthouse/for-rent/ixelles/1050/10306706',
    'https://www.immoweb.be/en/classified/apartment/for-rent/willebroek/2830/10309521',
    'https://www.immoweb.be/en/classified/house/for-sale/oupeye/4680/10302566',
    'https://www.immoweb.be/en/classified/house/for-sale/antwerpen/2140/10258718'
]

my_list = list()

for link in links :
    my_list.append(immoweb_scrapping(link))

print(my_list)