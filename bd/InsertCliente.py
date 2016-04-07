from gi.repository import Gtk
import sqlite3


class MyCliente:
    db = sqlite3.connect("tallerBD.dat")
    cursor = db.cursor()

    def __init__(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS clientes (dni TEXT PRIMARY KEY ASC, nombre TEXT, apellido TEXT)")
        self.db.commit()

    def crearCliente(self, dni, nombre, apellido):
        dni_encontrado = []

        for row in self.cursor.execute("SELECT dni FROM clientes"):
            dni_encontrado.append(row)

        if ((dni in dni_encontrado) == False):
            datos = (dni, nombre, apellido)
            self.cursor.execute("INSERT INTO clientes VALUES(?,?,?)", datos)
        else:
            print("")
            dialog = Gtk.MessageDialog(None,
                                       0,
                                       Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK,
                                       "El cliente ya existe, comprueba los dni.")
            dialog.format_secondary_text("Y esto es un whatTheFuck.")
            dialog.run()

        self.db.commit()

    def selectALL(self):
        datos_encontrados = []
        for row in self.cursor.execute("SELECT * FROM clientes"):
            datos_encontrados.append([row[0], row[1], row[2]])
            # print("clientes 1: "+row[0])
            # print("clientes 2: "+row[1])
            # print("clientes 3: "+row[2])
        return datos_encontrados

    def borrar(self, dni):
        self.cursor.execute("DELETE * FROM clientes WHERE dni = '" + dni + "'")

    def close(self):
        print("conexion a bd cerrada")
        self.cursor.close()
