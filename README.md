# AutoVet - Sistema de Gestión Veterinaria con IA (Backend)

Repositorio del backend para el Trabajo Final de Grado

---

## Guía de Instalación y Puesta en Marcha

### Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO_BACKEND>
    cd autoVet-Backend
    ```

2.  **Activar el entorno virtual:**
    -   **En macOS o Linux:**
        ```bash
        source venv/bin/activate
        ```
    -   **En Windows:**
        ```bash
        .\windows-venv\Scripts\activate
        ```

3.  **Instalar dependencias:**
    Desde la raíz del proyecto, ejecuta el siguiente comando para instalar todos los paquetes necesarios.
    ```bash
    pip install -r requirements.txt
    ```

### Ejecución de la Aplicación

Para iniciar el servidor de desarrollo del backend, utiliza el siguiente comando:

```bash
python manage.py runserver