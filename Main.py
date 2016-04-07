from gi.repository import Gtk
import bd.Loggin
import view.Ventana

UI_INFO = """
<ui>
  <menubar name='MenuBar'>
    <menu action='Archivo'>
      <menuitem action='ArchivoNuevo'/>
    </menu>
  </menubar>
</ui>
"""


class MyMain(Gtk.Window):
    def __init__(self):
        """
        Clase principal MyMAin,
        se crea una barra de menu con la opcion crear nuevo usuario.
        una caja contenedora que contiene 3 paquetes,
        el primer paquete, situado en la parte superior contiene un entry text de usuario y su label.
        el segundo paquete, situado en la parte central contiene un entry text de contraseña y label.
        el tercer paquete, situado en la parte inferior contiene un contiene dos botones, cancelar y aceptar.
        Se conecta en la base de datos.
        """
        Gtk.Window.__init__(self, title="Taller de coches para DI")
        self.set_border_width(40)

        # Barra de menu (menubar)
        action_group = Gtk.ActionGroup("mi_grupo_de_acciones")
        self.add_acciones_al_menu(action_group)
        manejador_ui = self.create_ui_manager()
        manejador_ui.insert_action_group(action_group)
        menubar = manejador_ui.get_widget("/MenuBar")

        # caja contenedora
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=40)
        self.add(self.box)

        # Paquete Norte
        self.north = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=60)
        self.entry1 = Gtk.Entry()
        self.entry1.set_text("usuario")
        self.label1 = Gtk.Label("Usuario", xalign=0)

        self.north.pack_start(self.label1, True, True, 0)
        self.north.pack_start(self.entry1, True, True, 0)

        # Paquete Central
        self.center = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=60)
        self.entry2 = Gtk.Entry()
        self.entry2.set_text("contraseña")
        self.label2 = Gtk.Label("Contraseña", xalign=0)

        self.center.pack_start(self.label2, True, True, 0)
        self.center.pack_start(self.entry2, True, True, 0)

        # Paquete del Sur
        self.south = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=60)
        self.button1 = Gtk.Button.new_with_label("Cancelar")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.button2 = Gtk.Button.new_with_label("Aceptar")
        self.button2.connect("clicked", self.on_button2_clicked)

        self.south.pack_start(self.button1, True, True, 0)
        self.south.pack_start(self.button2, True, True, 0)

        # Caja con paquete Norte,centro y Sur
        self.box.pack_start(self.north, True, True, 0)
        self.box.pack_start(self.center, True, True, 0)
        self.box.pack_start(self.south, True, True, 0)
        self.box.pack_start(menubar, True, True, 0)

        # Conectamos a la base de datos
        bd.Loggin.Loggin()

    def add_acciones_al_menu(self, action_group):
        """
        Se añaden acciones al menu.
        """
        acciones_archivo = Gtk.Action("Archivo", "Archivo", None, None)
        action_group.add_action(acciones_archivo)

        acciones_archivo_nuevo = Gtk.Action("ArchivoNuevo", None, None, Gtk.STOCK_NEW)
        acciones_archivo_nuevo.connect("activate", self.on_button_nuevo_menu_item_clicked)
        action_group.add_action(acciones_archivo_nuevo)

    def create_ui_manager(self):
        uimanager = Gtk.UIManager()

        # Throws exception if something went wrong
        uimanager.add_ui_from_string(UI_INFO)

        # Add the accelerator group to the toplevel window
        accelgroup = uimanager.get_accel_group()
        self.add_accel_group(accelgroup)
        return uimanager

    def on_button1_clicked(self, button):
        """
        Se cierra la aplicacion
        """
        print("Cerrando la aplicación")
        bd.Loggin.Loggin().close()
        Gtk.main_quit()

    def on_button2_clicked(self, button):
        """
        Accede a la base de datos y accede a la nueva ventana
        """
        if bd.Loggin.Loggin().verificarDatos(self.entry1.get_text(), self.entry2.get_text()):
            print("Accediendo... ")
            window.set_visible(False)
            view.Ventana.lanzar()
            bd.Loggin.Loggin().close()

    def on_button_nuevo_menu_item_clicked(self, button):
        """
        Se cra el usuario cuando accedemos al boton nuevo usuario de la menu bar.
        """
        bd.Loggin.Loggin().crearUsuario(self.entry1.get_text(), self.entry2.get_text())
        print("Usuario creado:")
        print("user " + self.entry1.get_text())
        print("pass " + self.entry2.get_text())


window = MyMain()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
