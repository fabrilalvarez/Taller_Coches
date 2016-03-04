from gi.repository import Gtk
import sqlite3


class Loggin:
    db = sqlite3.connect("loggin.dat")
    cursor = db.cursor()

    def __init__(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS usuarios (username TEXT PRIMARY KEY ASC, password TEXT)")
        self.db.commit()

    def crearUsuario(self, username, password):
        username_encontrado = []

        for row in self.cursor.execute("SELECT username FROM usuarios"):
            username_encontrado.append(row)

        if ((username in username_encontrado) == False):
            datos = (username, password)
            self.cursor.execute("INSERT INTO usuarios VALUES(?,?)", datos)
        else:
            print("")
            dialog = Gtk.MessageDialog(None,
                                       0,
                                       Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK,
                                       "El nombre de Usuario ya existe, prueba otro.")
            dialog.format_secondary_text("Y esto es un whatTheFuck.")
            dialog.run()

        self.db.commit()

    def verificarDatos(self, username, password):
        user_in_db = self.cursor.execute("SELECT username FROM usuarios WHERE username='"+username+"'")
        for row in user_in_db:
            user_row = row[0]
        pass_in_db = self.cursor.execute("SELECT password FROM usuarios WHERE username='"+username+"'")
        for row in pass_in_db:
            pass_row = row[0]

        if user_row == username and pass_row == password:
             return True
        else:
             return False

    def close(self):
        print("conexion a bd cerrada")
        self.cursor.close()
