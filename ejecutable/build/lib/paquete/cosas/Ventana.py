from gi.repository import Gtk, Gdk

UI_INFO = """
<ui>
  <toolbar name='ToolBar'>
    <toolitem action='FileNewStandard' />
  </toolbar>
</ui>
"""


class MyVentanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Taller de coches para DI")
        self.set_default_size(10, 10)
        self.set_border_width(10)
        # Caja contenedora
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)
        # Paquete de coches
        self.box_coches = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=200)
        self.label1 = Gtk.Label("Esto son coches")

        self.box_coches.pack_start(self.label1, False, False, 0)
        # Paquete de clientes
        self.box_clientes = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=300)
        self.label2 = Gtk.Label("Esto son clientes")

        self.box_clientes.pack_start(self.label2, False, False, 0)
        # Creamos un stack(movimiento de caja)
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(500)

        self.stack.add_titled(self.box_coches, "coches", "Coches")
        self.stack.add_titled(self.box_clientes, "clientes", "Clientes")

        self.stack_switcher = Gtk.StackSwitcher()
        self.stack_switcher.set_stack(self.stack)
        # Creamos Tool bar
        action_group = Gtk.ActionGroup("my_tool_bar")
        self.add_acciones_al_tool_bar(action_group)
        manejador_ui = self.create_ui_manager()
        manejador_ui.insert_action_group(action_group)
        self.toolbar = manejador_ui.get_widget("/ToolBar")
        # Caja para la ToolBar
        self.box_tool_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.box_tool_bar.pack_start(self.toolbar, False, False, 0)
        # Paquete Coche
        # Se añaden los paquetes a la caja
        self.box.pack_start(self.stack_switcher, False, False, 0)
        self.box.pack_start(self.box_tool_bar, False, False, 0)
        self.box.pack_start(self.stack, False, False, 0)

    def add_acciones_al_tool_bar(self, action_group):
        action_new = Gtk.Action("FileNewStandard",
                                "_New",
                                "Create a new file",
                                Gtk.STOCK_NEW)
        action_new.connect("activate", self.nuevo_vehiculo)
        action_group.add_action_with_accel(action_new, None)

    def create_ui_manager(self):
        uimanager = Gtk.UIManager()

        # Throws exception if something went wrong
        uimanager.add_ui_from_string(UI_INFO)

        # Add the accelerator group to the toplevel window
        accelgroup = uimanager.get_accel_group()
        self.add_accel_group(accelgroup)
        return uimanager

    def nuevo_vehiculo(self, widget):
        import view.NuevoCoche

    def cerrar(self, widget):
        Gtk.main_quit()


window = MyVentanaPrincipal()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
