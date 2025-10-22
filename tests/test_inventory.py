from selenium.webdriver.common.by import By
from selenium import webdriver

# PRE-ENTREGA 4:
# Verificar que el título de la página de inventario sea correcto

def test_inventory(login_in_driver):
    try:
        driver = login_in_driver
        assert driver.title == "Swag Labs"

    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()
