#! /usr/bin/env python
from cassandra.cluster import Cluster
import uuid
cluster = Cluster()
session = cluster.connect('deathstar')
#session.set_keyspace('users') #para cambiar de keyspace
rows = session.execute('SELECT * FROM members')
for user_row in rows:
    print user_row.id, user_row.apellido, user_row.nombre
#Trabajo con parametros
session.execute(
    """
    INSERT INTO members (id, apellido, nombre)
    VALUES (%s, %s, %s)
    """,
    (uuid.uuid1(), "John", "O'Reilly")
)
