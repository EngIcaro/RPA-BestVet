#%%
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time,requests 
#%%
qtd_products = 5
web_driver_path = '/opt/WebDriver/bin/chromedriver'
all_products = []
#%%
def set_up_chrome(web_driver_path):
    driver = Chrome(executable_path=web_driver_path)
    driver.maximize_window()
    time.sleep(1)
    
    return driver


def get_image_url(url_path):
    element_url = driver.find_element_by_xpath(url_path)
    text_url = element_url.get_attribute("src")
    first_url = text_url[0:43]
    aux_url = text_url[43:].split("/")
    middle_url = aux_url[0]+'/large'
    last_url = ""
    for i in range (2, len(aux_url)):
        last_url = "/" + aux_url[i]

    return first_url+middle_url+last_url

def append_new_product(name_xpath, initial_xpath, end_xpath, subscriber_xpath,sale_xpath,url_path):
    new_product = {}
    
    new_product['name']                 = driver.find_element_by_xpath(name_xpath).text
    
    try:
        new_product['initial_value']    = driver.find_element_by_xpath(initial_xpath).text
    except NoSuchElementException:
        new_product['initial_value']    = "Não possui"
    
    new_product['end_value']            = driver.find_element_by_xpath(end_xpath).text

    new_product['subscriber_value']     = driver.find_element_by_xpath(subscriber_xpath).text

    try:
        new_product['sale']             = driver.find_element_by_xpath(sale_xpath).text
    except NoSuchElementException:
        new_product['sale']             = "Não tem promoção"


    new_product['url']                  = get_image_url(url_path)

    return new_product
#%%

driver = set_up_chrome(web_driver_path)
driver.get("https://bestvet.petlove.com.br/cachorro?results_per_page="+str(qtd_products)+"&sort=8&page=1")
time.sleep(1)
for i in range(1, qtd_products+1):

    all_products.append(append_new_product('//*[@id="shelf-loop"]/div['+str(i)+']/div/a[1]/h3',
                                           '//*[@id="shelf-loop"]/div['+str(i)+']/div/a[2]/div[1]/span',
                                           '//*[@id="shelf-loop"]/div['+str(i)+']/div/a[2]/div[1]/div[2]',
                                           '//*[@id="shelf-loop"]/div['+str(i)+']/div/a[2]/div[1]/div[3]',
                                           '//*[@id="shelf-loop"]/div['+str(i)+']/div/a[2]/div[1]/div[1]',
                                           '//*[@id="shelf-loop"]/div['+str(i)+']/a/div[1]/div/img'))





#%%
element_url = driver.find_element_by_xpath('//*[@id="shelf-loop"]/div[1]/a/div[1]/div/img')
text_url = element_url.get_attribute("src")
full_url = ""
first_url = text_url[0:43]
aux_url = text_url[43:].split("/")
middle_url = aux_url[0]+'/large'
last_url = ""
for i in range (2, len(aux_url)):
    last_url = "/" + aux_url[i]

full_url = first_url+middle_url+last_url
#%%
reponse = requests.get(full_url)
if reponse.status_code == 200:
    with open(f"search{1}.jpg","wb") as file:
        file.write(reponse.content)
#%%
# Texto  01: //*[@id="shelf-loop"]/div[1]/div/a[1]/h3
# Texto  02: 
# Imagem 01: 
# Imagem 02: 
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
