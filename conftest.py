import pytest
from utils import login
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import tempfile
import shutil

# Fixture para el driver
@pytest.fixture
def driver():
    """
    Inicializa Firefox con un perfil temporal limpio para evitar
    guardar contraseñas y notificaciones emergentes.
    """
    # Crear un perfil temporal
    profile_dir = tempfile.mkdtemp()
    options = Options()
    options.set_preference("signon.rememberSignons", False)  # no guardar contraseñas
    options.set_preference("signon.autofillForms", False)    # no autocompletar
    options.set_preference("permissions.default.desktop-notification", 2)  # bloquear notificaciones
    options.set_preference("browser.cache.disk.enable", False)  # opcional: desactivar cache
    options.set_preference("browser.cache.memory.enable", False)

    # Inicializamos el navegador usando solo 'options'
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver

    driver.quit()
    shutil.rmtree(profile_dir)  # eliminar perfil temporal

# Fixture que hace login usando la función de utils.py
@pytest.fixture
def login_in_driver(driver):
    # Ejecuta login antes de cada test.
    login(driver)
    return driver
