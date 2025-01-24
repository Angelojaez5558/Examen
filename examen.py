import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar el WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Abrir la página de Mercado Libre
driver.get("https://www.mercadolibre.com")

# Seleccionar México como país
mexico_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "México"))
)
mexico_button.click()
time.sleep(2)
# Buscar "playstation 5"
search_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "nav-search-input"))
)
search_bar.clear()
search_bar.send_keys("playstation 5")
search_bar.send_keys(Keys.RETURN)
time.sleep(2)

# Quitar banner de cookies
accept_cookies_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='action:understood-button']"))
)
accept_cookies_button.click()    
time.sleep(2)
# Esperar a que se carguen los filtros y obtener la lista
listas = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "ui-search-filter-container"))
)

# Aplicar el filtro "Nuevo"
for li in listas:
    try:
        span = li.find_element(By.CLASS_NAME, "ui-search-filter-name")
        if span.text.strip() == "Nuevo":
            enlace = li.find_element(By.TAG_NAME, "a")
            enlace.click()
            break
    except Exception:
        continue
time.sleep(2)
# Aplicar el filtro "Distrito Federal"
ubicacion = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Distrito Federal']/.."))
    )
ubicacion.click()
time.sleep(2)
# Ordenar por "Mayor precio"
ordenar_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "andes-dropdown__trigger"))
)
ordenar_btn.click()
time.sleep(2)
# Seleccionar la opción "Mayor precio"
opciones_menu = WebDriverWait(driver, 10).until( 
    EC.presence_of_element_located((By.CLASS_NAME, "andes-list"))
)
opciones = opciones_menu.find_elements(By.TAG_NAME, "li")
for opcion in opciones:
    if "Mayor precio" in opcion.text:
        opcion.click()
        break

# Obtener los nombres y precios de los primeros 5 productos
productos = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "ui-search-layout__item"))
)
time.sleep(2)
print("\nProductos encontrados:")
for producto in productos[:5]:
    try:
        # Extraer nombre y precio
        nombre = producto.find_element(By.CLASS_NAME, "poly-component__title-wrapper").text
        precio = producto.find_element(By.CLASS_NAME, "poly-price__current").text
        print(f"Producto: {nombre} - Precio: {precio}")
    except Exception as e:
        print(f"No se pudo obtener información de este producto. Error: {e}")
        continue

# Mantener el navegador abierto
input("\nPresiona Enter para cerrar el navegador...")

# Cerrar el navegador
driver.quit()