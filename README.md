# Sitio Web - Portfolio y Blog 

## Descripción

El proyecto a través de Django combina un portafolio estático con proyectos personales y un blog con publicaciones, categorías, búsqueda, comentarios y cuentas de usuario.

## 17 de Septiembre - Inicialización del proyecto
  - Los primeros días se basaron en entender mejor django.

## 22 de Septiembre - Integrar portafolio
  - Los primeros días se basaron en entender mejor django.
    
## 23 de Septiembre - Vinculación
  - Agregué el blog como aplicación
  - Vincular y definir url
  - Creación simple de un html
  
## 24 de Septiembre
  - Modelos (Post, Category, Comment)
  - Vistas + Templates muy básicos
    
## 30 de Septiembre
  - Agregar archivo styles.css
  - Agregar base.html
  - Implementar que aparezcan posteos
    
## 1 de Octubre
  - Mejora de carta de posteo
  - Modificacion css
    
## 4 de Octubre
  - Agregar modelo Comment
  - Agregar espacio de comentario en cada posteo
  - Comenzar con el sistema de registro/inicio de sesión
  - Sistema de busqueda
  - Agregar vistas blog_search y register
    
## 5 de Octubre
  - Arreglar que se mantenga el modo (claro/oscuro) al navegar por el blog
  - Modificación de inicio de sesion/registro y logout + como se muestra

## 8 de Octubre
  - Agregar imagenes como parte del posteo
  - Modularización de archivos .css
  - Sistema de Paginas/Paginator para los posteos

## Pendientes
  - Sistema de likes
  - Mejora en las imagenes
  - Comentar comentarios
  - Calendario que permita mostrar los posteos de la fecha elegida
  - Dropdown de Categorías --> No me convencía la idea

##  Tecnologías utilizadas

- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite

## Estructura del Proyecto

```text
Website_Django/
├── README.md
└── personalwebsite/
    ├── manage.py
    ├── db.sqlite3
    ├── media/                       # Archivos subidos al blog
    │   └── post/
    ├── mysite/                      # Configuración global del proyecto
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    ├── blog/                        # Aplicación del blog
    │   ├── migrations/              # Cambios de esquema de la base de datos
    │   ├── models.py                # Post, Category y Comment
    │   ├── views.py                 # Inicio, detalle, categorías y búsqueda
    │   ├── forms.py                 # Formulario de comentarios
    │   ├── urls.py                  # Rutas propias del blog
    │   ├── admin.py                 # Modelos disponibles en Django Admin
    │   ├── templates/
    │   │   ├── base.html            # Plantilla compartida del blog
    │   │   ├── blog/                # Plantillas de las páginas del blog
    │   │   └── registration/        # Inicio de sesión
    │   └── static/blog/             # CSS compartido y CSS por página
    └── portfolio/                   # Aplicación del portafolio
        ├── migrations/
        ├── models.py
        ├── views.py
        ├── urls.py
        ├── admin.py
        ├── templates/portfolio/
        │   └── index.html
        └── static/portfolio/
            ├── styles.css
            ├── Salame.png
            ├── pokedex.webp
            └── Music.png
```

## Aplicaciones

- **`portfolio`**: muestra la página principal del portafolio y sus proyectos. Sus imágenes y estilos son archivos estáticos de la aplicación.
- **`blog`**: administra publicaciones, categorías y comentarios. Las imágenes asociadas a publicaciones se guardan bajo `media/post/`; las plantillas y hojas de estilo están dentro de esta aplicación.
- **`mysite`**: configura Django y conecta las rutas de las aplicaciones.

