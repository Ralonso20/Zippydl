import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def download_file(driver):
    link = get_download_link(driver)
    filename = get_file_name(link)
    with urllib.request.urlopen(link) as response, open(filename, 'wb') as out_file:
        # Obtén la longitud del archivo para mostrar el progreso de la descarga
        file_size = get_file_length(response)
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


def get_file_length(response):
    # Obtén la longitud del archivo para mostrar el progreso de la descarga
    return int(response.getheader('Content-Length').strip())


def get_file_name(link):
    # Obtén el nombre del archivo desde el enlace
    return link.split('/')[-1]


def get_download_link(driver):
    # Obtén el enlace directo utilizando JavaScript
    return driver.execute_script('return document.getElementById("dlbutton").href')


def click_download_button(driver):
    # Espera hasta que aparezca el botón de descarga y haz clic en él
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'dlbutton')))


def selenium_config():
    # Configura Selenium para utilizar un navegador Firefox
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    return driver


def download_zippyshare(link):
    driver = selenium_config()

    # Abre el enlace en el navegador controlado por Selenium
    driver.get(link)

    click_download_button(driver)

    # Descarga el archivo desde el enlace directo
    download_file(driver)

    # Cierra el navegador controlado por Selenium
    driver.quit()


def get_units(elapsed_time, downloaded):
    units = 'B/s'
    speed = 0

    speed = downloaded / elapsed_time
    if speed > 1024 * 1024:
        speed /= 1024 * 1024
        units = 'MB/s'
    elif speed > 1024:
        speed /= 1024
        units = 'KB/s'

    return units, speed


def show_progress(downloaded, total, start_time):
    """Muestra el progreso de la descarga en la consola."""
    percent = downloaded / total * 100
    elapsed_time = time.time() - start_time
    if elapsed_time > 0:
        units, speed = get_units(elapsed_time, downloaded)
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
