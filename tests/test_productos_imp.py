
from selenium.webdriver.common.by import By
from selenium import webdriver

# PRE-ENTREGA 5:
# Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)

def test_productos_imp(login_in_driver):
    try:
        driver = login_in_driver

        # Validar que el menú de navegación esté presente
        menu_nav = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu_nav.is_displayed(), "El botón del menú no está visible"

        # Validar que el filtro de productos esté presente
        filtro_prod = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro_prod.is_displayed(), "El filtro de productos no está visible"

        # Validar que el carrito de compras esté presente
        carrito_compra = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        assert carrito_compra.is_displayed(), "El ícono del carrito de compras no está visible"

    except Exception as e:
        print(f"Error en test_productos_imp: {e}")
        raise
    finally:
        driver.quit()