Buenas tardes, David Fernando, mi nombres es Juan Herrera soy aspirante a la vacante de Accedo, y esta es la realización de la prueba técnica propuesta para la vacante de Desarrollador web, la cual se nos presentó en la reunion anterior de tuvimos.
Quisiera explicar un poquito de como desarrollé la prueba, utilicé Python en su mayoria, y librerias Python para el uso de funciones para el backend del mismo.
Tambien utilice html5 y css3 para el diseño de las mismas paginas, y algunos atributos jinja2 básicos.

Las dependencias estan remarcadas y comentadas al principio del codigo "App.py", y la instalación de las mismas es muy sencilla. Pero por si fuese necesario, se realiza mediante la Consola del Sistema (CMD) con el siguiente comando:
 
    ||| pip install Flask (Para la instalación de Flask)
    ||| pip install SQLALchemy (Para la instalacion de SQLALchemy)
    ||| pip install Flask-Migrate (Para la instalacion de Flask Migrate)
    ||| pip install flask-login (Para la instalacion de Flask Login)


La base de datos con la cual el aplicativo podrá realizar las consultas y la inserción de nuevos datos está exportada en la ruta
    
    ||| Data/accedo_user.sql

Mediante el aplicativo MyPhpAdmin, se puede dirigir a la sección de Importar, y realizar la importacion necesaria para la base de datos, la cual esta configurada para que realice consultas e inserciones mediante los formularios correspondientes

Entre otras cosas, cabe mencionar que en el codigo "App.py" esta comentado con sugerencias a tener en cuenta al momento de ejecutar el codigo y/o hacer cambios de parametros para su correcto funcionamiento.
Para su ejecución, dirigirse a la consola y ubicarse en el directorio de donde está el archivo Python y poner en la consola
    
    ||| python app.py

Cabe de sugerencia que en el IDE Visual Studio Code (VSC) el proceso se simplifica con solo abrir la carpeta, y abrir una nueva terminal, o en el apartado de esquina superior derecha "Run Code"
    
    ||| CTRL + ALT + N

Con este proceso, debería de correr el programa en un servidor local (-127.0.0.1-) y poder ejecutarse correctamente. 

Muchas gracias por la oportunidad, quedo atento a cualquier inquietud, saludos.