from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def config():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("-headless")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

    return driver

def consultar(cadena_busqueda):
    contenido=''
    try:
        driver = config()

        url=f'https://twitter.com/search?q={cadena_busqueda}&src=typeahead_click'
        driver.get(url)
        
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[1]/a')))

        contenido = element.text
        print(f"Contenido: {contenido}")

    except Exception as e:
        print(e)
    finally:
        driver.close()
    return contenido

def pagina_principal():
    try:
        driver = config()

        url="https://twitter.com/?lang=es"
        driver.get(url)

        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[2]/div/div/div/h2/div[2]/span')))
        
        clase = element.get_dom_attribute("class")
        element.screenshot('home.png')
        contenido = element.text
        
        print(clase, contenido, sep='\n')

    except Exception as e:
        print(e)
    finally:
        driver.quit()

if __name__ == "__main__":
    pagina_principal()