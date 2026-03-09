
from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    """Clase que contiene la lógica.
    """

    def __init__(self):

        # DICCIONARIO de libros
        # clave: ISBN
        # valor: objeto Libro
        self.libros = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # SET para IDs únicos
        self.ids_usuarios = set()

    # -------------------------
    # LIBROS

    def añadir_libro(self, titulo, autor, categoria, isbn):

        if isbn in self.libros:
            print("El libro ya existe.")
            return

        libro = Libro(titulo, autor, categoria, isbn)

        self.libros[isbn] = libro

        print("Libro añadido correctamente.")

    def quitar_libro(self, isbn):

        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # -------------------------
    # USUARIOS

    def registrar_usuario(self, nombre, id_usuario):

        if id_usuario in self.ids_usuarios:
            print("El usuario ya existe.")
            return

        usuario = Usuario(nombre, id_usuario)

        self.usuarios[id_usuario] = usuario
        self.ids_usuarios.add(id_usuario)

        print("Usuario registrado correctamente.")

    def baja_usuario(self, id_usuario):

        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # -------------------------
    # PRÉSTAMOS
    
    def prestar_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]

        usuario.libros_prestados.append(libro)

        del self.libros[isbn]

        print("Libro prestado correctamente.")

    def devolver_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]

        for libro in usuario.libros_prestados:

            if libro.isbn == isbn:

                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro

                print("Libro devuelto correctamente.")
                return

        print("El usuario no tiene ese libro.")

    # -------------------------
    # BUSQUEDAS

    def buscar_por_titulo(self, titulo):

        for libro in self.libros.values():
            if libro.titulo_autor[0].lower() == titulo.lower():
                print(libro)

    def buscar_por_autor(self, autor):

        for libro in self.libros.values():
            if libro.titulo_autor[1].lower() == autor.lower():
                print(libro)

    def buscar_por_categoria(self, categoria):

        for libro in self.libros.values():
            if libro.categoria.lower() == categoria.lower():
                print(libro)

    # -------------------------
    # LIBROS PRESTADOS

    def listar_libros_usuario(self, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]

        if not usuario.libros_prestados:
            print("El usuario no tiene libros prestados.")
            return

        for libro in usuario.libros_prestados:
            print(libro)