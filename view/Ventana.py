from gi.repository import Gtk, Gdk
import view.NuevoCoche
import view.NuevoCliente
import bd.InsertCoche
import bd.InsertCliente

UI_INFO = """
<ui>
  <toolbar name='ToolBar'>
    <toolitem action='FileNewStandard' />
    <toolitem action='FileShowAll' />
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
        #########################################################################

        # Creamos Tool bar Coche
        action_group = Gtk.ActionGroup("my_tool_bar_1")
        self.add_acciones_al_tool_bar_coche(action_group)
        manejador_ui = self.create_ui_manager()
        manejador_ui.insert_action_group(action_group)
        self.toolbarCoche = manejador_ui.get_widget("/ToolBar")

        # Caja para la ToolBarCoche
        self.box_tool_bar_coche = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.box_tool_bar_coche.pack_start(self.toolbarCoche, False, False, 0)

        # Paquete de coches
        self.box_coches = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)

        # TreeView
        self.model1 = Gtk.ListStore(str, str, int)
        self.tree1 = Gtk.TreeView(self.model1)

        # TreeViewColumn
        renderer1 = Gtk.CellRendererText()
        column1 = Gtk.TreeViewColumn("matricula", renderer1, text=0)
        column2 = Gtk.TreeViewColumn("marca", renderer1, text=0)
        column3 = Gtk.TreeViewColumn("km", renderer1, text=0)
        self.tree1.append_column(column1)
        self.tree1.append_column(column2)
        self.tree1.append_column(column3)

        self.box_coches.pack_start(self.box_tool_bar_coche, False, False, 0)
        self.box_coches.pack_start(self.tree1, False, False, 0)
        #########################################################################

        # Creamos Tool bar Cliente
        action_group = Gtk.ActionGroup("my_tool_bar_B")
        self.add_acciones_al_tool_bar_cliente(action_group)
        manejador_ui = self.create_ui_manager()
        manejador_ui.insert_action_group(action_group)
        self.toolbarCliente = manejador_ui.get_widget("/ToolBar")

        # Caja para la ToolBarCliente
        self.box_tool_bar_cliente = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.box_tool_bar_cliente.pack_start(self.toolbarCliente, False, False, 0)

        # Paquete de clientes
        self.box_clientes = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)

        # TreeView
        self.model2 = Gtk.ListStore(str, str, str)
        self.tree2 = Gtk.TreeView(self.model2)

        # TreeViewColumn
        renderer2 = Gtk.CellRendererText()
        column1 = Gtk.TreeViewColumn("DNI", renderer2, text=0)
        column2 = Gtk.TreeViewColumn("Nombre", renderer2, text=0)
        column3 = Gtk.TreeViewColumn("Apellido", renderer2, text=0)
        self.tree2.append_column(column1)
        self.tree2.append_column(column2)
        self.tree2.append_column(column3)

        self.box_clientes.pack_start(self.box_tool_bar_cliente, False, False, 0)
        self.box_clientes.pack_start(self.tree2, False, False, 0)
        #########################################################################

        # Creamos un stack(movimiento de caja)
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(500)

        self.stack.add_titled(self.box_coches, "coches", "Coches")
        self.stack.add_titled(self.box_clientes, "clientes", "Clientes")

        self.stack_switcher = Gtk.StackSwitcher()
        self.stack_switcher.set_stack(self.stack)
        #########################################################################

        # Se añaden los paquetes a la caja
        self.box.pack_start(self.stack_switcher, False, False, 0)
        self.box.pack_start(self.stack, False, False, 0)

    def add_acciones_al_tool_bar_coche(self, action_group):
        action_new1 = Gtk.Action("FileNewStandard","_New","Create a new file",Gtk.STOCK_NEW)
        action_new1.connect("activate", self.nuevo_coche)

        action_fileshowall = Gtk.Action("FileShowAll", "_Show", "Show All", Gtk.STOCK_FIND)
        action_fileshowall.connect("activate", self.rellenarTreeViewCoches)

        action_group.add_action_with_accel(action_new1, None)
        action_group.add_action(action_fileshowall)

    def add_acciones_al_tool_bar_cliente(self, action_group):
        action_new1 = Gtk.Action("FileNewStandard","_New","Create a new file",Gtk.STOCK_NEW)
        action_new1.connect("activate", self.nuevo_cliente)

        action_fileshowall = Gtk.Action("FileShowAll", None, None, Gtk.STOCK_FIND)
        action_fileshowall.connect("activate", self.rellenarTreeViewClientes)

        action_group.add_action_with_accel(action_new1, None)
        action_group.add_action(action_fileshowall)

    def create_ui_manager(self):
        uimanager = Gtk.UIManager()

        # Throws exception if something went wrong
        uimanager.add_ui_from_string(UI_INFO)

        # Add the accelerator group to the toplevel window
        accelgroup = uimanager.get_accel_group()
        self.add_accel_group(accelgroup)
        return uimanager

    def nuevo_coche(self, widget):
        view.NuevoCoche.lanzar()

    def nuevo_cliente(self, widget):
        view.NuevoCliente.lanzar()

    def rellenarTreeViewCoches(self, widget):
        model = Gtk.ListStore(str, str, int)
        for row in bd.InsertCoche.MyCoche().selectALL():
            print(row[0],row[1],row[2])
            model.append([row[0],row[1],row[2]])

        self.model1 = model
        self.tree1.set_model(self.model1)
        # self.box_clientes.pack_start(self.tree1, False, False, 0)

    def rellenarTreeViewClientes(self, widget):
        model = Gtk.ListStore(str, str, str)
        for row in bd.InsertCliente.MyCliente().selectALL():
            print(row[0],row[1],row[2])
            model.append([row[0],row[1],row[2]])

        self.model2 = model
        self.tree2.set_model(self.model2)
        # self.box_clientes.pack_start(self.tree2, False, False, 0)

    def cerrar(self, widget):
        Gtk.main_quit()


def lanzar():
    window = MyVentanaPrincipal()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()
