# Introducción

Este programa ha sido diseñado para ayudar a agilizar la descarga de un listado de links de Zippyshare, este programa te permite automatizar este proceso y descargar todos los archivos de forma rápida y eficiente.

Con este programa, podrás ingresar una lista de links de Zippyshare y el programa se encargará de descargar todos los archivos correspondientes de forma automática.

EL objetivo era crear un programa que sea sencillo de usar y que sin muchas complicaciones de instalación resolviera este problema.

# Ejecución del programa y uso

Para utilizar el programa se puede realizar el proceso de **Instalación** o ejecutar el archivo **zippydl.exe**, en el mismo directorio que se guarde el archivo zippydl.exe o se tenga el código del programa, se debe guardar un fichero .txt con el siguiente nombre: "links.txt".
![ejemplo2](/assets/ej2.png)

El archivo debe contener todos los links que queramos descargar.

![ejemplo](/assets/ejtxt.png)

Si no hay ningún problema se debería abrir una ventana mostrando la siguiente información:

![ejemplo3](/assets/ej3.png)

Una vez finalizado podremos cerrar la terminal:

![ejemplo4](/assets/ej4.png)

# Instalación

1. Instalación de Python:
   Si aún no tienes Python instalado en tu computadora, debes descargar e instalar la última versión de Python desde la página oficial de Python ([https://www.python.org/downloads/](https://www.python.org/downloads/)). Sigue las instrucciones del instalador para completar la instalación.
2. Instalación de pip:
   Pip es un gestor de paquetes de Python que te permitirá instalar todas las dependencias necesarias para este proyecto. Si no tienes pip instalado, puedes descargar el archivo get-pip.py desde el sitio oficial ([https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py)) y ejecutarlo en la línea de comandos con el siguiente comando: `python get-pip.py`
   Instalacion virtualenv:
   Instala `virtualenv` con el siguiente comando: `pip install virtualenv`
3. Creación y ejecución del entorno:
   Crea un nuevo entorno virtual con el siguiente comando: `virtualenv mi_entorno`
   Dirijete a la carpeta de tu entorno virtual:

   Windows: `virtualenv\Scripts\activate.bat`

   MacOS/Linux: `source virtualenv/bin/activate`

4. Instalación de los requerimientos:
   Una vez que tienes el entorno virtual activado, debes instalar los requerimientos del proyecto. En la línea de comandos, ejecuta el siguiente comando: `pip install -r requirements.txt`

# Dependencias

1. **Selenium==4.8.2:**
   Selenium es una herramienta de automatización de navegador web que permite interactuar con páginas web de forma programática. En este proyecto, se utiliza Selenium para automatizar la descarga de archivos de Zippyshare.
2. **urllib3==1.26.4:**
   urllib3 es una biblioteca de Python que proporciona una interfaz de bajo nivel para trabajar con HTTP y HTTPS. En este proyecto, se utiliza urllib3 para descargar los archivos de Zippyshare.
3. **PyInstaller:**
   PyInstaller es una herramienta que permite empaquetar proyectos de Python en un archivo ejecutable que puede ser distribuido en diferentes sistemas operativos. En este proyecto, se utiliza PyInstaller para crear un archivo ejecutable que pueda ser utilizado en diferentes sistemas operativos sin necesidad de tener Python instalado.

   El comando utilizado en el proceso fue el siguiente:

   ```
   pyinstaller -c -F -i icon.ico --name zippydl --add-data "requirements.txt;." main.py
   ```

# Licencia

Este proyecto no está licenciado y se proporciona "tal cual" sin garantía de ningún tipo, expresa o implícita. Este código fue creado con fines de estudio y práctica, y no se apoya para la utilización de prácticas maliciosas ni venta del código. Los usuarios son responsables de utilizar este código de manera responsable y de acuerdo con las leyes y regulaciones locales. El autor de este proyecto no será responsable de ningún uso indebido del código.
