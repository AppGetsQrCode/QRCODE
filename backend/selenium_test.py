from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def iniciar_navegador():

    options = Options()

    # Necessário para rodar em servidor sem interface gráfica
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    return driver


if __name__ == "__main__":

    driver = iniciar_navegador()

    try:
        driver.get("https://www.google.com")

        print("Título:", driver.title)
        print("URL:", driver.current_url)

    finally:
        driver.quit()
