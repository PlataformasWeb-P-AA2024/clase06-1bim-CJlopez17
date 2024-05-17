"""
    Consulta de información en las entidades en la base de datos
"""

from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Autor"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

print(informacion)
# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
for d in informacion:
    print ("El nombre es: %s y al edad es: %d" % (d[0],d[3]))
# Se iteras sobre d para poder impirmir todos las linesa de la base de datos 
# Medinate el %s y %d se le asigna valor a las cadenas de d[0] y d[3]
# Debido a que el for itera sobre cada columna de la base de datos nso va dar la informacion
#    print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
