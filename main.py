import requests
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download_zippyshare(link):
    # Configura Selenium para utilizar un navegador Firefox
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    # Abre el enlace en el navegador controlado por Selenium
    driver.get(link)

    # Espera hasta que aparezca el botón de descarga y haz clic en él
    wait = WebDriverWait(driver, 10)
    dl_button = wait.until(EC.presence_of_element_located((By.ID, 'dlbutton')))

    # Obtén el enlace directo utilizando JavaScript
    direct_link = driver.execute_script('return document.getElementById("dlbutton").href')

    # Descarga el archivo desde el enlace directo
    filename = direct_link.split('/')[-1]
    with urllib.request.urlopen(direct_link) as response, open(filename, 'wb') as out_file:
        # Obtén la longitud del archivo para mostrar el progreso de la descarga
        file_size = int(response.getheader('Content-Length').strip())
        # Inicia la descarga y muestra la información en la consola
        downloaded = 0
        block_size = 1024
        while True:
            data = response.read(block_size)
            if not data:
                break
            downloaded += len(data)
            out_file.write(data)
            show_progress(downloaded, file_size)

    # Cierra el navegador controlado por Selenium
    driver.quit()


def show_progress(downloaded, total):
    """Muestra el progreso de la descarga en la consola."""
    percent = downloaded / total * 100
    speed = downloaded / 1024 / 1024
    print(f'Descargando archivo... {percent:.2f}% completado ({speed:.2f} MB descargados)')


def main():
    # Abre el archivo .txt con los links de zippyshare
    with open('links.txt', 'r') as f:
        links = f.read().splitlines()

    # Descarga cada archivo de Zippyshare en la lista de links
    # for link in links:
    #    download_zippyshare(link)

    download_zippyshare("https://www74.zippyshare.com/v/aW8sY0hc/file.html")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
