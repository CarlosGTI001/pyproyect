from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = "https://ytlarge.com/youtube/monetization-checker/"



# Configuración de Selenium con un navegador (Chrome o Firefox)
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)

# Espera a que la página se cargue completamente (puedes ajustar este tiempo)
driver.implicitly_wait(10)

# Encuentra el elemento de la imagen usando Selenium
img_element = driver.find_element_by_xpath("//img[@id='capt']")  # Ajusta el XPath según la imagen

# Obtiene el atributo src de la imagen
if img_element:
    img_src = img_element.get_attribute("src")
    print("URL de la imagen:", img_src)
else:
    print("No se encontró la URL de la imagen.")

# Cierra el navegador después de terminar
driver.quit()
