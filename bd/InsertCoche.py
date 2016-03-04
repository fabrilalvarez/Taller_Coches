from gi.repository import Gtk
import sqlite3


class MyCoche:
    db = sqlite3.connect("tallerBD.dat")
    cursor = db.cursor()

    def __init__(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS coches (matricula TEXT PRIMARY KEY ASC, marca TEXT, km INTEGER)")
        self.db.commit()

    def crearCoche(self, matricula, marca, km):
        matricula_encontrada = []

        for row in self.cursor.execute("SELECT matricula FROM coches"):
            matricula_encontrada.append(row)

        if ((matricula in matricula_encontrada) == False):
            datos = (matricula, marca, km)
            self.cursor.execute("INSERT INTO coches VALUES(?,?,?)", datos)
        else:
            print("")
            dialog = Gtk.MessageDialog(None,
                                       0,
                                       Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK,
                                       "El coche ya existe, comprueba las matriculas.")
            dialog.format_secondary_text("Y esto es un whatTheFuck.")
            dialog.run()

        self.db.commit()

    def selectALL(self):
        datos_encontrados = []
        for row in self.cursor.execute("SELECT * FROM coches"):
            datos_encontrados.append([row[0],row[1],row[2]])
            # print("coches 1: "+row[0])
            # print("coches 2: "+row[1])
            # print("coches 3: "+str(row[2]))
        return datos_encontrados

    def close(self):
        print("conexion a bd cerrada")
        self.cursor.close()
