from selenium import webdriver
from selenium.webdriver.common.by import By
import data_filter

def immoweb_scrapping(url):
    if("projet" in url):
        return None
    my_dict = dict()

    tab = url.split("/")
    my_dict["id"] = tab[-1]
    my_dict["Locality"] = tab[7].capitalize()

    driver = webdriver.Chrome()
    driver.get(url)

    title = driver.find_element(By.XPATH, "//h1[@class='classified__title']").text

    if(title.find("à vendre")>-1) :
        my_dict["Type of sale"] = "à vendre"
        my_dict.update(data_filter.get_properties(title.replace(" à vendre", "")))
    elif(title.find("à louer")>-1) :
        my_dict["Type of sale"] = "à louer"
        my_dict.update(data_filter.get_properties(title.replace(" à louer", "")))
    else :
        my_dict["Type of sale"] = None

    my_dict["Price"] = driver.find_element(By.XPATH, "//p[@class='classified__price']//span[@class='sr-only']").text

    for key, value in zip(driver.find_elements(By.XPATH, "//th[@class='classified-table__header']"), driver.find_elements(By.XPATH, "//td[@class='classified-table__data']")):
        my_dict[key.text.replace("\n", "")] = value.text.replace("\n", "")

    driver.close()

    return data_filter.immoweb_filter(my_dict)

links = ['https://www.immoweb.be/fr/annonce/villa/a-vendre/uccle/1180/10110650', 'https://www.immoweb.be/fr/annonce/maison/a-vendre/bruxelles/1120/10306539', 'https://www.immoweb.be/fr/annonce/maison-de-maitre/a-vendre/jette/1090/10212075', 'https://www.immoweb.be/fr/annonce/projet-neuf-maisons/a-vendre/woluwe-saint-pierre/1150/10303909', 'https://www.immoweb.be/fr/annonce/maison/a-vendre/woluwe-saint-pierre/1150/10306388', 'https://www.immoweb.be/fr/annonce/maison/a-vendre/woluwe-saint-lambert/1200/10306389', 'https://www.immoweb.be/fr/annonce/maison/a-vendre/molenbeek-saint-jean/1080/10303905', 'https://www.immoweb.be/fr/annonce/maison/a-vendre/woluwe-saint-pierre/1150/10294916', 'https://www.immoweb.be/fr/annonce/maison-bel-etage/a-vendre/jette/1090/10293277', 'https://www.immoweb.be/fr/annonce/maison/a-vendre/uccle/1180/10292832', 'https://www.immoweb.be/fr/annonce/maison/a-vendre/brussels/1000/10292629', 'https://www.immoweb.be/fr/annonce/immeuble-a-appartements/a-vendre/bruxelles/1000/10206439', 'https://www.immoweb.be/fr/annonce/maison/a-vendre/evere/1140/10096540']
my_list = list()

for link in links :
    my_list.append(immoweb_scrapping(link))

print(my_list)