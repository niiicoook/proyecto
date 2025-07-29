import sqlite3

def creardb():
    conn = sqlite3.connect("peliculas.db")
    conn.commit()
    conn.close()

def tabla(nombre: str):
    conn = sqlite3.connect("peliculas.db")
    cursor = conn.cursor()

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {nombre}
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT NOT NULL,
        director TEXT,
        year INTEGER,
        UNIQUE(title, director, year)
        )
        """)
    conn.commit()
    conn.close()


def agregar_fila(title: str, director: str, year:int):
    conn = sqlite3.connect("peliculas.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO movies(title, director, year) VALUES(?,?,?)
        """,
        (title, director, year)
    )
    ide = cursor.lastrowid
    conn.commit()
    conn.close()
    return ide

def agregar_varios(movies:list[str, str, int]):
    conn = sqlite3.connect("peliculas.db")
    cursor = conn.cursor()

    cursor.executemany(
        """
        INSERT INTO movies(title, director, year) VALUES(?,?,?)
        """,
        movies
    )
    conn.commit()
    conn.close()

def actualizar(columna: str, dato: int|str, idd: int):
    conn = sqlite3.connect("peliculas.db")
    cursor = conn.cursor()

    cursor.execute(f"UPDATE movies SET {columna} = ? WHERE id = ?", (dato, idd))
    
    conn.commit()
    conn.close()

def seleccionar(columna: str, valor: int|str):
    conn = sqlite3.connect("peliculas.db")
    cursor = conn.cursor()

    accion = f"SELECT * FROM movies WHERE {columna} = ?"
    cursor.execute(accion, (valor,))
    resultado: int|str = cursor.fetchall()

    conn.close()
    return resultado

def eliminar_fila(title: str, director: str, year:int):
    conn = sqlite3.connect("peliculas.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM movies WHERE title = ? AND director = ? AND year = ?
        """,
        (title, director, year)
    )
    conn.commit()
    conn.close()


def borrar():
    conn = sqlite3.connect("peliculas.db")
    cursor = conn.cursor()

    cursor.execute("""DROP TABLE IF EXISTS movies""")
    conn.commit()
    conn.close()


