
```md
# Games API

Este es un proyecto de Django REST Framework que gestiona una API para la administración de juegos. La API permite realizar operaciones CRUD sobre los juegos, subir imágenes, y manejar información detallada como título, género, plataforma, fecha de lanzamiento, desarrollador, descripción, calificación, precio, entre otros.

## Instalación

Clona este repositorio y navega al directorio del proyecto:

```bash
git clone https://github.com/JuanFelipe29/games-api
cd games-api
```

### Crear un entorno virtual

Para crear un entorno virtual, sigue los siguientes pasos:

En Linux o macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Esto activará el entorno virtual, donde se instalarán todas las dependencias necesarias para el proyecto.

### Instalar las dependencias

Una vez activado el entorno virtual, instala las dependencias del proyecto con:

```bash
pip install -r requirements.txt
```

## Migraciones de la base de datos

Antes de correr el servidor, necesitas aplicar las migraciones de la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Crear un superusuario

Para acceder al panel de administración de Django, debes crear un superusuario:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones y proporciona un nombre de usuario, correo electrónico y contraseña.

## Correr el servidor de desarrollo

Una vez instaladas las dependencias y aplicadas las migraciones, puedes iniciar el servidor de desarrollo con el siguiente comando:

```bash
python manage.py runserver
```

Esto levantará el servidor en `http://127.0.0.1:8000/`.

## Documentación de la API

La documentación de la API está disponible en los siguientes enlaces:

- **Swagger UI**: Accede a la interfaz gráfica de Swagger en `http://127.0.0.1:8000/swagger/`
- **ReDoc**: Accede a la documentación alternativa en `http://127.0.0.1:8000/redoc/`

Ambas herramientas te permiten explorar y probar los endpoints de la API.

## Uso de la API

La API tiene su versión 1 en la ruta `http://127.0.0.1:8000/api/v1/`. Puedes interactuar con los recursos de la API para crear, leer, actualizar y eliminar juegos. Asegúrate de revisar la documentación de Swagger para conocer todos los endpoints y sus detalles.

### Ejemplo de creación de un juego

Para crear un nuevo juego en la API, puedes enviar una solicitud POST a `http://127.0.0.1:8000/api/v1/games/` con el siguiente JSON como cuerpo de la solicitud:

```json
{
  "title": "The Legend of Zelda: Breath of the Wild",
  "gender": "Aventura",
  "platform": "Nintendo Switch, Wii U",
  "release_date": "2017-03-03",
  "developer": "Nintendo",
  "description": "Un juego de aventura en mundo abierto donde los jugadores exploran el reino de Hyrule.",
  "rating": "E",
  "price": "59.99",
  "image": "http://127.0.0.1:8000/media/games/The_Legend_of_Zelda_Breath_of_the_Wild.jpg"
}
```

### Ejemplo de respuesta al crear un juego

Al enviar correctamente la solicitud POST para crear un nuevo juego, recibirás una respuesta similar a esta:

```json
{
  "id": 1,
  "title": "The Legend of Zelda: Breath of the Wild",
  "gender": "Aventura",
  "platform": "Nintendo Switch, Wii U",
  "release_date": "2017-03-03",
  "developer": "Nintendo",
  "description": "Un juego de aventura en mundo abierto donde los jugadores exploran el reino de Hyrule.",
  "rating": "E",
  "price": "59.99",
  "image": "http://127.0.0.1:8000/media/games/The_Legend_of_Zelda_Breath_of_the_Wild.jpg",
  "created_at": "2024-10-10T00:27:17.973858Z",
  "updated_at": "2024-10-10T00:27:17.973897Z"
}
```

## Requerimientos.txt

El archivo `requirements.txt` incluye todas las dependencias necesarias para este proyecto, entre ellas:

```
Django==5.1
djangorestframework==3.14
drf-yasg==1.20.0
```

Asegúrate de instalar estas dependencias con `pip install -r requirements.txt` antes de ejecutar el proyecto.
```

