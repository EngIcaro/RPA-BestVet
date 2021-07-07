#%%
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time 
#%%
qtd_products = 5
#%%
#Or use the context manager
driver = Chrome(executable_path='/opt/WebDriver/bin/chromedriver')
driver.get("https://bestvet.petlove.com.br/cachorro?results_per_page="+str(qtd_products)+"&sort=8&page=1")
driver.maximize_window()
time.sleep(1)
element = driver.find_element_by_xpath('//*[@id="btn-accept-cookie"]')
element.click()
element = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/nav/div/ul/li[1]/a')
element.click()
element = driver.find_element_by_xpath('//*[@id="catalog-desktop"]/div[3]/div/div[2]/div[4]/div/div[2]/div/div[2]/select/option[8]')
element.click() 
elements = driver.find_elements_by_xpath('//div[@id="shelf-loop"]/div')
for item in elements:
    aux = item.find_element_by_xpath('//div/a[1]/h3')
    print(aux.text)
#%%
for i 5:
element_text = driver.find_element_by_xpath('//*[@id="shelf-loop"]/div[1]/div/a[1]/h3')
nome_produto = element_text.text
print(element_text.text)
element_text = driver.find_element_by_xpath('//*[@id="shelf-loop"]/div[1]/div/a[2]/div[1]/span')
valor_inicial = element_text.text
print(element_text.text)
element_text = driver.find_element_by_xpath('//*[@id="shelf-loop"]/div[1]/div/a[2]/div[1]/div[2]')
valor_final = element_text.text
print(element_text.text)
element_text = driver.find_element_by_xpath('//*[@id="shelf-loop"]/div[1]/div/a[2]/div[1]/div[3]')
valor_assinantes = element_text.text
print(element_text.text)

#%%
# Texto  01: //*[@id="shelf-loop"]/div[1]/div/a[1]/h3
# Texto  02: 
# Imagem 01: 
# Imagem 02: 

//*[@id="shelf-loop"]/div[1]/div/a[1]
#%%
driver.execute_script("window.scrollTo(0, 200)") 
time.sleep(2)
elements = driver.find_elements_by_xpath('//*[@id="shelf-loop"]/div')
aux = 1
time.sleep(3)
for item in elements:
    item.screenshot('foo'+str(aux)+'.png')
    time.sleep(2)
    aux+=1

print(aux)
#driver.close()
# %%

/html/body/div[2]/div/div[4]/div/div[2]/div[5]
/html/body/div[2]/div/div[4]/div/div[2]/div[5]/div[1]/a/div[1]
/html/body/div[2]/div/div[4]/div/div[2]/div[5]/div[2]
#%%
driver = Chrome(executable_path='/opt/WebDriver/bin/chromedriver')
driver.get("https://bestvet.petlove.com.br/cachorro?results_per_page="+str(qtd_products)+"&sort=8&page=1")
driver.maximize_window()
time.sleep(1)
element = driver.find_element_by_xpath('//*[@id="btn-accept-cookie"]')
element.click()
element = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/nav/div/ul/li[1]/a')
element.click()
element = driver.find_element_by_xpath('//*[@id="catalog-desktop"]/div[3]/div/div[2]/div[4]/div/div[2]/div/div[2]/select/option[8]')
element.click() 
elements = driver.find_elements_by_xpath('//div[@id="shelf-loop"]/div')
for item in elements:
    aux = item.find_element_by_xpath('//div/a[1]/h3')
    print(aux.text)
