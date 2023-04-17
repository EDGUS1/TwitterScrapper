from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


def configFirefox():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("-headless")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()), options=firefox_options
    )

    return driver


def configChrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--start-maximized")

    prefs = {"profile.managed_default_content_settings.images": 2}

    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )

    return driver


def consultar(cadena_busqueda):
    contenido = ""
    try:
        driver = configChrome()

        url = f"https://twitter.com/search?q={cadena_busqueda}&src=typeahead_click"
        driver.get(url)
        path = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[1]/a'
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    path,
                )
            )
        )

        contenido = element.text
        print(f"Contenido: {contenido}")

    except Exception as e:
        print(e)
    finally:
        driver.close()
    return contenido


def pagina_principal():
    try:
        driver = configChrome()

        url = "https://twitter.com/?lang=es"

        driver.get(url)
        path = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[2]/div/div/div/h2/div[2]/span'
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, path))
        )

        clase = element.get_dom_attribute("class")
        element.screenshot("src/images/home.png")
        contenido = element.text
        print(clase, contenido, sep="\n")

        element = driver.find_element(By.TAG_NAME, "body")
        element.screenshot("src/images/full_page.png")

    except Exception as e:
        print(e)
    finally:
        driver.quit()


def tendencias():
    try:
        driver = configChrome()

        url = "https://twitter.com/?lang=es"
        driver.get(url)
        path = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[2]/div/div/div/h2/div[2]/span'
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    path,
                )
            )
        )

        xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div'

        element = driver.find_element(By.XPATH, xpath)
        element.screenshot("src/images/tendencias.png")

        hijos = element.find_elements(By.XPATH, "./child::*")

        cadena = ""
        for e in hijos:
            subhijos = e.find_elements(By.XPATH, "./child::*")
            if len(subhijos[0].find_elements(By.XPATH, "./child::*")) > 0:
                for ee in subhijos:
                    ss = ee.find_elements(By.XPATH, "./child::*")
                    cadena += ss[0].text

        return cadena

    except Exception as e:
        print(f"Error {e}")
    finally:
        driver.quit()

    return ""


if __name__ == "__main__":
    print(tendencias())
