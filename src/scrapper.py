from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime


def config_firefox():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("-headless")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()), options=firefox_options
    )

    return driver


def config_chrome():
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
        driver = config_chrome()

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
        driver = config_chrome()

        url = "https://twitter.com"

        driver.get(url)
        xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[1]/div'
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
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


def explore():
    try:
        driver = config_chrome()

        url = "https://twitter.com"
        driver.get(url)

        xpath_content = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[2]/div/span"
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath_content))
        )
        element = driver.find_element(By.XPATH, xpath_content)
        # element.screenshot(f"src/images/explore{datetime.now().timestamp()}.png")
        content = element.text

        # xpath_image='/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div/div/div/div/a/div/div[2]/div/img'
        # element = driver.find_element(By.XPATH, xpath_image)
        # element.screenshot(f"src/images/explore{datetime.now().timestamp()}.png")
        # print(element.text)

        # xpath_user='/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/div/a/div/div[1]/span/span'
        # element = driver.find_element(By.XPATH, xpath_user)
        # element.screenshot(f"src/images/explore{datetime.now().timestamp()}.png")
        # print(element.text)

        # xpath_arroba='/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/a/div/span'
        # element = driver.find_element(By.XPATH, xpath_arroba)
        # element.screenshot(f"src/images/explore{datetime.now().timestamp()}.png")
        # print(element.text)

        return content

    except Exception as e:
        print(f"Error {e}")
    finally:
        driver.quit()

    return "No funciona"


def search_user(user):
    contenido = ""
    try:
        driver = config_chrome()

        url = f"https://twitter.com/{user}"
        driver.get(url)
        xpath = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div"
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

        xpath = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[3]/div/div"
        element = driver.find_element(By.XPATH, xpath)
        contenido = element.text
        print(f"Contenido: {contenido}")

    except Exception as e:
        print(e)
    finally:
        driver.close()
    return contenido


def search_tweet(user_name, status):
    contenido = ""
    try:
        driver = config_chrome()

        url = f"https://twitter.com/{user_name}/status/{status}"
        driver.get(url)
        xpath = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[2]/div/div/span"
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

        element = driver.find_element(By.XPATH, xpath)
        contenido = element.text
        print(f"Contenido: {contenido}")

    except Exception as e:
        print(e)
    finally:
        driver.close()
    return contenido


if __name__ == "__main__":
    pagina_principal()
