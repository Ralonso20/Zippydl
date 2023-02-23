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
import time


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
        start_time = time.time()
        while True:
            data = response.read(block_size)
            if not data:
                break
            downloaded += len(data)
            out_file.write(data)
            show_progress(downloaded, file_size, start_time)

    # Cierra el navegador controlado por Selenium
    driver.quit()


def show_progress(downloaded, total, start_time):
    """Muestra el progreso de la descarga en la consola."""
    percent = downloaded / total * 100
    elapsed_time = time.time() - start_time
    if elapsed_time > 0:
        speed = downloaded / elapsed_time
        units = 'B/s'
        if speed > 1024 * 1024:
            speed /= 1024 * 1024
            units = 'MB/s'
        elif speed > 1024:
            speed /= 1024
            units = 'KB/s'
        print(
            f'\rDescargando archivo... {percent:.2f}% completado ({speed:.2f} {units}, {downloaded / 1024 / 1024:.2f} MB descargados)',
            end=' ')
    else:
        print(f'\rDescargando archivo... {percent:.2f}% completado ({downloaded / 1024 / 1024:.2f} MB descargados)',
              end=' ')


def main():
    # Abre el archivo .txt con los links de zippyshare
    with open('links.txt', 'r') as f:
        links = f.read().splitlines()

    # Descarga cada archivo de Zippyshare en la lista de links
    # for link in links:
    #    download_zippyshare(link)

    download_zippyshare("https://www106.zippyshare.com/v/p71kSAgC/file.html")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
