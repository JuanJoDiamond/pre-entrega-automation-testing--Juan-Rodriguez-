from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# PRE-ENTREGA 7:
''' 
° Añadir un producto al carrito haciendo clic en el botón correspondiente
° Verificar que el contador del carrito se incremente correctamente
° Navegar al carrito de compras y comprobar que el producto añadido aparezca correctamente en el carrito'''

def test_inventory(login_in_driver):

    try:
        driver = login_in_driver

        # Añadir un producto al carrito haciendo clic en el botón correspondiente
        compra = driver.find_elements(By.CLASS_NAME, "inventory_item")
        compra[0].find_element(By.TAG_NAME, "button").click()
        time.sleep(5)

        # Verificar que el contador del carrito se haya incrementado a 1
        carrito_contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert carrito_contador == "1", f"El contador del carrito es {carrito_contador}, se esperaba 1"
        print("TEXT OK")
        time.sleep(4)
        
        # Navegar al carrito de compras y comprobar que el producto añadido aparezca correctamente en el carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(4)
        productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(productos_carrito) == 1, f"Hay {len(productos_carrito)} productos en el carrito, se esperaba 1"
        print("CARRITO OK")

    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()
