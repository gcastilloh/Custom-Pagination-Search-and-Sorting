# Basado en:

Django REST Framework Tutorial - Custom Pagination, Search & Sorting using MySQL

https://www.youtube.com/watch?v=YMbSyWjCpI4&ab_channel=ScalableScripts

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
