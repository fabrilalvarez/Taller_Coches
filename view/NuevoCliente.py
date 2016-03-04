from gi.repository import Gtk, Gdk
import bd.InsertCliente


class MyNuevoCliente(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Taller de coches para DI")
        self.set_default_size(300, 100)
        self.set_border_width(10)

        # Caja contenedora
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        # Paquete Fila1
        self.row1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.row1.set_border_width(5)
        self.entry1 = Gtk.Entry()
        self.entry1.set_text("DNI")
        self.label1 = Gtk.Label("DNI", xalign=0)

        self.row1.pack_start(self.label1, True, True, 0)
        self.row1.pack_start(self.entry1, True, True, 0)

        # Paquete Fila2
        self.row2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.row2.set_border_width(5)
        self.entry2 = Gtk.Entry()
        self.entry2.set_text("Nombre")
        self.label2 = Gtk.Label("Nombre", xalign=0)

        self.row2.pack_start(self.label2, True, True, 0)
        self.row2.pack_start(self.entry2, True, True, 0)

        # Paquete Fila3
        self.row3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.row3.set_border_width(5)
        self.entry3 = Gtk.Entry()
        self.entry3.set_text("Apellidos")
        self.label3 = Gtk.Label("Apellidos", xalign=0)

        self.row3.pack_start(self.label3, True, True, 0)
        self.row3.pack_start(self.entry3, True, True, 0)

        # Paquete Fila4
        self.row4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.boton_aceptar = Gtk.Button.new_with_label("Aceptar")
        self.boton_aceptar.connect("clicked", self.on_boton_aceptar_clicked)
        self.boton_cancelar = Gtk.Button.new_with_label("Cancelar")
        self.boton_cancelar.connect("clicked", self.on_boton_cancelar_clicked)

        self.row4.pack_start(self.boton_aceptar, True, True, 0)
        self.row4.pack_start(self.boton_cancelar, True, True, 0)

        # Label de verificacion
        self.verificado = Gtk.Label("Insertado")
        color = Gdk.color_parse('chartreuse3')
        rgba = Gdk.RGBA.from_color(color)
        self.verificado.override_background_color(0, rgba)

        # Se añaden las filas a la caja
        self.box.pack_start(self.row1, False, False, 0)
        self.box.pack_start(self.row2, False, False, 0)
        self.box.pack_start(self.row3, False, False, 0)
        self.box.pack_start(self.row4, False, False, 0)

        bd.InsertCliente.MyCliente()

    def on_boton_aceptar_clicked(self, button):
        print(self.entry1.get_text(), " ", len(self.entry1.get_text()))
        print(self.entry2.get_text(), " ", len(self.entry2.get_text()))
        print(self.entry3.get_text(), " ", len(self.entry3.get_text()))
        if len(self.entry1.get_text()) > 0 and len(self.entry2.get_text()) > 0:
            bd.InsertCliente.MyCliente().crearCliente(self.entry1.get_text(),
                                                self.entry2.get_text(),
                                                self.entry3.get_text())
            self.verificado.set_visible(True)
            self.box.pack_start(self.verificado, False, False, 0)
        else:
            print("Comprueba los campos vacíos")

    def on_boton_cancelar_clicked(self, button):
        self.entry1.set_text("")
        self.entry2.set_text("")
        self.entry3.set_text("")
        self.box.remove(self.verificado)

def lanzar():
    window = MyNuevoCliente()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()
