# Examen
Examen de automatizacion

Requisitos previos
Antes de ejecutar el script, asegúrate de tener los siguientes requisitos:

1. - Instalar Python 3.13.1: El script está escrito en Python 3. Asegúrate de tener Python instalado en tu sistema.

2. - Instalar Selenium: Selenium es una herramienta de automatización de navegadores. Para instalarla, ejecuta el siguiente comando:

  pip install selenium

3. - Instalar WebDriver: Este script utiliza ChromeDriver para controlar Google Chrome. Asegúrate de descargar e instalar ChromeDriver compatible con la versión de tu navegador. Puedes encontrarlo en el siguiente enlace:
Descargar ChromeDriver

Una vez descargado, asegúrate de agregar el archivo chromedriver a tu PATH o especificar la ruta completa en el código. (Esto puede ser opcional ya que en mi caso no se requirio pero en caso de que no permita anexo el paso)

Pasos para ejecutar el código

1. - Clona o descarga el archivo: Si aún no lo tienes, guarda el código proporcionado en un archivo .py, por ejemplo, examen.py.
2. - Configura el WebDriver: Si no tienes ChromeDriver en tu PATH, edita la siguiente línea para incluir la ruta completa de tu chromedriver:
     driver = webdriver.Chrome(executable_path="ruta_a_tu_chromedriver") ("Igual opcional en mi caso tampoco se requirio este paso").
3. - Ejecuta el script: Abre una terminal o línea de comandos y navega al directorio donde guardaste el archivo examen.py. Luego ejecuta el siguiente comando:
  python mercadolibre_automatizado.py
4. - Proceso de ejecución: El script hará lo siguiente:

        Abrirá la página de Mercado Libre.
        Seleccionará México como país.
        Buscará "playstation 5".
        Clicará en "Nuevo" en los filtros de productos.
        Filtrará por "Distrito Federal" en la ubicación.
        Ordenará los productos por "Mayor precio".
        Extraerá el nombre y precio de los primeros 5 productos.
        Durante el proceso, se imprimirán los nombres y precios de los productos en la consola.

5. - Cerrar el navegador: El script pedirá que presiones Enter para cerrar el navegador una vez que se haya completado la extracción de datos.
