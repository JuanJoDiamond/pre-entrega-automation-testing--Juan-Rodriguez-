# 🧪 Proyecto de Testing QA Automation – Pre-entrega Clase 8

## 📌 Propósito del proyecto

Este proyecto forma parte de la **pre-entrega del curso de Testing QA Automation**. El objetivo es aplicar los conocimientos adquiridos hasta la Clase 8, automatizando flujos básicos de navegación web con **Selenium WebDriver** y **Python**.

Se trabajó sobre el sitio [saucedemo.com](https://www.saucedemo.com), una aplicación demo diseñada para prácticas de testing, enfocándose en:

- 🔍 Interacción con elementos web  
- 📌 Estrategias de localización  
- ✅ Validación de estados y navegación

---

## ⚙️ Tecnologías utilizadas

| 🛠️ Herramienta           | 💡 Propósito                                      |
|--------------------------|--------------------------------------------------|
| 🐍 Python                | Lenguaje principal del proyecto                  |
| 🧪 Pytest                | Estructura y ejecución de pruebas                |
| 🕸️ Selenium WebDriver    | Automatización de navegación web                |
| 🔧 Git & GitHub          | Control de versiones y gestión del repositorio  |

---

## 🧭 Casos de prueba implementados

### 🔐 1. Automatización de Login

- ✅ Navegación a la página de login
- ✅ Ingreso de credenciales válidas:
  - Usuario: `standard_user`
  - Contraseña: `secret_sauce`
- ✅ Validación de login exitoso:
  - Redirección a `/inventory.html`
  - Verificación de texto “Products” y “Swag Labs”

**🧾 Criterios mínimos cumplidos:**
- ⏳ Login automatizado con espera explícita  
- 🔍 Validación de URL y elementos clave

---

### 🛍️ 2. Navegación y Verificación del Catálogo

- ✅ Verificación del título de la página de inventario
- ✅ Comprobación de presencia de productos visibles
- ✅ Validación de elementos importantes (menú, filtros, etc.)
- ✅ Listado del nombre y precio del primer producto

**🧾 Criterios mínimos cumplidos:**
- 🏷️ Título correcto  
- 📦 Productos visibles  
- 💲 Información del primer producto listada

---

### 🛒 3. Interacción con Productos

- ✅ Añadir un producto al carrito
- ✅ Verificar incremento del contador del carrito
- ✅ Navegar al carrito de compras
- ✅ Comprobar que el producto añadido esté presente

**🧾 Criterios mínimos cumplidos:**
- 🖱️ Interacción funcional con el carrito  
- 👁️ Validación visual y lógica del producto añadido

---

## 🧰 Instalación de dependencias

1. Clonar el repositorio:
   
   git clone
   
   cd qa-automation-saucedemo
   
   pip install -r requirements.txt

3. Ejecución de pruebas:
Para ejecutar los tests y generar un reporte HTML:


pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html


📄 El archivo reporte.html se generará en el directorio raíz del proyecto, mostrando los resultados detallados de la ejecución.

---

## 📌 Buenas prácticas aplicadas
✅ Commits frecuentes con mensajes descriptivos

✅ Estructura clara y modular del proyecto

✅ Validaciones robustas con espera explícita

✅ Uso de Page Object Model (POM) para mantener el código organizado

## 🙋 Autor
Juanjo Rodriguez 

QA Tester | Python Developer | Explorador de metodologías ágiles 

📧 juanjodiamond@gmail.com


