import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


                                                #ja vēlas citus parametrus
minCena = input("ievadiet minimālo cenu: ")
maxCena = input("ievadiet minimālo cenu: ")
minGads = input("ievadiet minimālo vecumu: ")
maxGads = input("ievadiet minimālo vecumu: ")

print("1. Benzīns, 2. Benzīns/gāze, 3. Dīzelis, 4. Hybrid, 5. Elekstriskais")
dzinejs = input("ievadiet dzinēja tipu skaitrli: ")
if dzinejs =="1":
    dzinejs =="Benzīns"
elif dzinejs == "2":
    dzinejs = "Benzīns/gāze"
elif dzinejs == "3":
    dzinejs = " Dīzelis"  
elif dzinejs == "4":
    dzinejs = "Hybrid" 
elif dzinejs == "5":
    dzinejs = " Elekstriskais" 
else: print("kļūda, neeksistē")
dzinejs = dzinejs.lstrip().rstrip()

karba = input("ievadiet 1, ja vēlaties automātu un 2, ja vēlaties manuālu): ")
if karba == 1:
    karba = "Automāts"
else: karba = "Manuāla"
karba = karba.lstrip().rstrip()

print("1. Apvidus, 2. Hečbeks, 3. Kabriolets, 4. Mikroautobuss,")
print("5. Minivens, 6. Pikaps, 7. Sedans, 8. Kupeja, 9. Universāls ")
tips = input("ievadiet auto tipa skaitli: ")
if tips == "1":
    tips =="Apvidus"
elif tips == "2":
    tips = "Hečbeks"
elif tips == "3":
    tips = "Kabriolets"  
elif tips == "4":
    tips = "Mikroautobuss" 
elif tips == "5":
    tips = "Minivens" 
elif tips == "6":
    tips = "Pikaps" 
elif tips == "7":
    tips = "Sedans" 
elif tips == "8":
    tips = "Kupeja"    
elif tips == "9":
    tips = "Universāls" 
else: print("kļūda, neeksistē")  
tips = tips.lstrip().rstrip()

#minCena = 2000
#maxCena = 4000
#minGads = 2000
#maxGads = 2020
#dzinejs = "Dīzelis"
#karba = "Manuāla"
#tips = "Kupeja"

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.ss.lv/lv/transport/cars/"
driver.get(url)
time.sleep(2)

#minimālās cenas atzīmēšana
find = driver.find_element(By.ID, "f_o_8_min")
find.send_keys(minCena)
#minimālās cenas atzīmēšana
find = driver.find_element(By.ID, "f_o_8_max")
find.send_keys(maxCena)

#minimālā gada atzīmēšana
find = driver.find_element(By.XPATH, "//select[@name='topt[18][min]']")
find.click()
find = driver.find_element(By.XPATH, f"//select[@name='topt[18][min]']/option[text()='{minGads}']")
find.click()
#maksimālā gada atzīmēšana
find = driver.find_element(By.XPATH, "//select[@name='topt[18][max]']")
find.click()
find = driver.find_element(By.XPATH, f"//select[@name='topt[18][max]']/option[text()='{maxGads}']")
find.click()

#dzinēja izvēle
find = driver.find_element(By.XPATH, "//select[@name='opt[34]']")
find.click()
find = driver.find_element(By.XPATH, f"//select[@name='opt[34]']/option[text()='{dzinejs}']")
find.click()

#ātruma kārbas izvēle
find = driver.find_element(By.XPATH, "//select[@name='opt[35]']")
find.click()
find = driver.find_element(By.XPATH, f"//select[@name='opt[35]']/option[text()='{karba}']")
find.click()

#tipa izvēle
find = driver.find_element(By.XPATH, "//select[@name='opt[32]']")
find.click()
find = driver.find_element(By.XPATH, f"//select[@name='opt[32]']/option[text()='{tips}']")
find.click()


input()