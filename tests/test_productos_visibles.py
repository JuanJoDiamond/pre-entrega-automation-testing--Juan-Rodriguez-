
from selenium.webdriver.common.by import By
from selenium import webdriver

# PRE-ENTREGA 5:
# Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)

def test_inventory(login_in_driver):
    try:
        driver = login_in_driver

        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No hay productos visibles en la pagina"
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()