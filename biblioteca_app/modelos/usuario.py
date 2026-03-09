class Usuario:
    """Clase que representa un usuario registrado."""

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

        # LISTA para almacenar los libros prestados
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} | ID: {self.id_usuario}"