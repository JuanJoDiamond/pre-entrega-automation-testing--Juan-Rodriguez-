from selenium.webdriver.common.by import By
from selenium import webdriver

# PRE-ENTREGA 3: 
# - Validar login exitoso verificando que se haya redirigido a la página de inventario.

def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver

        assert "/inventory.html" in driver.current_url, "No se redirgio al inventario"

    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    finally:
        driver.quit()
    




