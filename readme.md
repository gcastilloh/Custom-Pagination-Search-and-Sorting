# descripción

Aplicación que implementa mediante Django-REST una API simple para consultar una tabla de datos, 
filtrando, paginando, ordenando y filtrando la información. Todo este proceso se lleva a cabo del lado del backend.

El archivo views.py de la app search contiene la mayor parte del proceso.

# Basado en:

Django REST Framework Tutorial - Custom Pagination, Search & Sorting using MySQL

https://www.youtube.com/watch?v=YMbSyWjCpI4&ab_channel=ScalableScripts

# descripción

La paginación es un proceso común en django, lo mismo el filtrao o la búsqueda, estos procesos
funciona generalmente bien de manera independiente, pero al tratar de integrar todos estos en 
una sola consulta al backend comienzan los problemas. Aqui se presenta una solución sencilla 
al problema. Esta solución no hace uso de la paginación ya integrada en django

# uso

Mediante postman puede hacerse una consulta via rest-framework a las ligas

http://localhost:8000/api/products/backend?s=mark&sort=desc&page=5

o algo parecido para buscar aquellos datos que en cuyo titulo o descripcion contengan la cadena "mark",
además ordenará esos datos descendentemente y entregará la pagina 5

# el comando populate

Un detalle interesante es el uso de el directorio managment dentro de la app search, esto permite 
ejecutar código como si fuera un comando de manage.py, de hecho al escribir:

`python manage.py`

se muestra (solo pongo los ultimos renglones):

```
[rest_framework]
    generateschema

[search]
    populate         <----- 

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
```

de manera que podemos escribir:

`python manage.py populate`

para se ejecutar el script de la funcion populate! (que aqui pobla la base de datos ocn datos aletorios, gracias fake)
