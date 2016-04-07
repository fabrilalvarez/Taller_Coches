import os.path
from gi.repository import Gtk, Gdk
from reportlab.lib.styles import getSampleStyleSheet
import view.NuevoCoche
import view.NuevoCliente
import bd.InsertCoche
import bd.InsertCliente
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

UI_INFO = """
<ui>
  <toolbar name='ToolBar'>
    <toolitem action='FileNewStandard' />
    <toolitem action='FileShowAll' />
    <toolitem action='Factura' />
    <toolitem action='Delete' />
    <toolitem action='Help' />
  </toolbar>
</ui>
"""


class MyVentanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Taller de coches para DI")
        self.set_default_size(100, 100)
        self.set_border_width(10)

        # Caja contenedora
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)
        #########################################################################

        # Creamos Tool bar Coche
        action_group = Gtk.ActionGroup("my_tool_bar_1")
        self.add_acciones_al_tool_bar(action_group,
                                      self.nuevo_coche,
                                      self.rellenarTreeViewCoches,
                                      self.impresion,
                                      self.delete,
                                      self.help)
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
        column2 = Gtk.TreeViewColumn("marca", renderer1, text=1)
        column3 = Gtk.TreeViewColumn("km", renderer1, text=2)
        self.tree1.append_column(column1)
        self.tree1.append_column(column2)
        self.tree1.append_column(column3)

        self.box_coches.pack_start(self.box_tool_bar_coche, False, False, 0)
        self.box_coches.pack_start(self.tree1, False, False, 0)
        #########################################################################

        # Creamos Tool bar Cliente
        action_group = Gtk.ActionGroup("my_tool_bar_B")
        self.add_acciones_al_tool_bar(action_group,
                                      self.nuevo_cliente,
                                      self.rellenarTreeViewClientes,
                                      self.impresion,
                                      self.delete,
                                      self.help)
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
        column2 = Gtk.TreeViewColumn("Nombre", renderer2, text=1)
        column3 = Gtk.TreeViewColumn("Apellido", renderer2, text=2)
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

    def add_acciones_al_tool_bar(self, action_group, metodo0, metodo1, metodo2, metodo3, metodo4):
        action_new1 = Gtk.Action("FileNewStandard", "_New", "Create a new file", Gtk.STOCK_NEW)
        action_new1.connect("activate", metodo0)

        action_fileshowall = Gtk.Action("FileShowAll", "_Show", "Show All", Gtk.STOCK_FIND)
        action_fileshowall.connect("activate", metodo1)

        action_factura = Gtk.Action("Factura", "_Factura", "Factura", Gtk.STOCK_PRINT)
        action_factura.connect("activate", metodo2)

        action_delete = Gtk.Action("Delete", "_Delete", "Delete", Gtk.STOCK_CLEAR)
        action_delete.connect("activate", metodo3)

        action_help = Gtk.Action("Help", "_Help", "Help", Gtk.STOCK_HELP)
        action_help.connect("activate", metodo4)

        action_group.add_action(action_new1)
        action_group.add_action(action_fileshowall)
        action_group.add_action(action_factura)
        action_group.add_action(action_delete)
        action_group.add_action(action_help)

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

    def help(self, widget):
        print("heyyy... pringao necesitas ayuda? JODETE!")

    def delete(self, widget):
        print("eres un flipao que vas a borrar")

    def rellenarTreeViewCoches(self, widget):
        model = Gtk.ListStore(str, str, int)
        for row in bd.InsertCoche.MyCoche().selectALL():
            print(row[0], row[1], row[2])
            model.append([row[0], row[1], row[2]])

        self.model1 = model
        self.tree1.set_model(self.model1)
        # self.box_clientes.pack_start(self.tree1, False, False, 0)

    def rellenarTreeViewClientes(self, widget):
        model = Gtk.ListStore(str, str, str)
        for row in bd.InsertCliente.MyCliente().selectALL():
            print(row[0], row[1], row[2])
            model.append([row[0], row[1], row[2]])

        self.model2 = model
        self.tree2.set_model(self.model2)
        # self.box_clientes.pack_start(self.tree2, False, False, 0)

    def cerrar(self, widget):
        Gtk.main_quit()

    def impresion(self, widget):
        # cabecera
        hojaEstilo = getSampleStyleSheet()

        guion = []

        cabecera = hojaEstilo['Heading4']
        cabecera.pageBreakBefore = 0
        cabecera.KepWithNext = 0  # Empezar pagina en blanco o no
        cabecera.backColor = colors.deepskyblue

        parrafo = Paragraph("Taller de coches", cabecera)

        guion.append(parrafo)
        guion.append(Spacer(0, 20))

        # cuerpo
        estilo = hojaEstilo['BodyText']

        cadena = "informacion de los clientes\n"

        tabla = []
        for row in bd.InsertCliente.MyCliente().selectALL():
            tabla.append(row)

        tablaa = Table(tabla)

        parrafo2 = Paragraph(cadena, estilo)

        guion.append(parrafo2)
        guion.append(tablaa)
        guion.append(Spacer(0, 20))

        # añadir imagen
        imagen = "../Taller_Coches/imagenes/clientes_img.jpeg"
        imagen_logo = Image(os.path.realpath(imagen), width=100, height=50)
        guion.append(imagen_logo)

        doc = SimpleDocTemplate("clientes.pdf", pagesize=A4, showBoundary=1)

        doc.build(guion)
        print("pdf creado")


def lanzar():
    window = MyVentanaPrincipal()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()
