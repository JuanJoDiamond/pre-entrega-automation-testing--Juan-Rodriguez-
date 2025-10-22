from selenium.webdriver.common.by import By
import time

# PRE-ENTREGA 1: 
# - Automazion del Login.

# Función para iniciar sesión en la aplicación de prueba
# Sirve para iniciar sesión en la aplicación web de prueba utilizando Selenium WebDriver.
# Esto se utiliza como inicio del resto de las pruebas que necesitan un usuario autenticado.

# PRE-ENTREGA 2:
# - Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
def login(driver):
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Esperar 2 segundos para asegurar que la página cargue
    time.sleep(2)

    # Evitamos que el driver se cierre inmediatamente, para que las pruebas puedan continuar
    # driver.quit()