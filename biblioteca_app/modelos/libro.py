class Libro:
    """Esta claserepresenta un libro dentro del sistema.
    """

    def __init__(self, titulo, autor, categoria, isbn):
        # Se utiliza una TUPLA para almacenar título y autor
        self.titulo_autor = (titulo, autor)

        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo_autor[0]} | Autor: {self.titulo_autor[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"