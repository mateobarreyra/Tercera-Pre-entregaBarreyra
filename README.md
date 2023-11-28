-creo proyecto desde gitbash.
-creo venv.
-ejecuto en consola: pip install django.
-ejecuto en consola:python manage.py migrate. para crear base de datos.
-ejecuto en consola:python manage.py runserver.para correr el servidor.
-automatizo el archivo de manage.py para que se ejecute como runserver.
-creo carpeta templates.
-creo archivo index.html en templates.
-creo archivo git ignore
-creo repositorio en github
-agrego el directorio de templates en settings.py
-creo la App, utilizando en la consola el codigo: Python manage.py startapp (nombre de la aplicacion)#voy a utilizar Appcoder
-dentro de la carpeta AppCoder/models, creo los modelos de pelicula,serie,tvshow
-en la consola aplico manage.py makemigrations para crear los modelos como codigo html en la base de datos
-desde boostrap descargo la plantilla html pre fabricada
-el archivo index del zip lo utilizo como base.html
-el resto de los archivos se añaden a la carpeta static dentro del directorio de AppCoder
-creo la vista show para mostrar el html en la pagina dentro de la app, y creo un archivo de urls.py dentro de esta.Luego conecto las url de la aplicacion con las url de la carpeta principal.
-dentro del archivo base.html cambio las referencias externas por las referencias internas para poder mostrar la web de mejor forma
-divido dentro de templates la plantilla de html base en la parte de la navegacion y creo una carpeta con la parte dividida.
-en templates creo mi carpeta Appcoder para poder mostar de forma ordenada las vistas
-dentro de la web voy a url de admin para ingresar al panel administrativo
-para acceder al panel administrativo:
en la consola realizo los siguientes comandos:
python manage.py createsuperuser
username=admin
email=admin@admin.com
password=admin
-una vez ingresado para agregar los modelos al panel administrativo
para agregar los modelos al panel
en la carpeta AppCoder/admin.py:
añado los modelos de la siguiente forma-->
importo desde AppCoder.models las clases
admin.sites.register("nombre de la clase a agregar")
-creo el archivo forms en la carpeta Appcoder.
-creo 3 formularios (Pelicula,series,Tvshow) y ademas creo dentro de cada uno una funcion de busqueda
-creo las vistas de los formularios de creacion y busqueda en AppCoder/views.py
-creo las url correspondientes en Appcoder/urls.py
-creo los archivos htpp correspondientes a cada vista en templates/AppCoder
-modifico los div de la seccion del navegador de mi base html, agregando asi 3
 botones de creacion tanto de Peliculas,series y Tvshows.
 ademas agrego 3 botones mas de busqueda de todos los modelos.
 -Automaticamente al crear un nuevo objeto se redirecciona a la pagina en donde se encuentran todos los objetos de esa clase.
