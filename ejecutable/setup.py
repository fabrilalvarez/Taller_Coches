from distutils.core import setup

files = ['cosas/**']
setup(
    name="Taller de fran",
    version="1.0",
    description="Taller hecho para DI",
    author="Fran",
    author_email="fabrilalvarez@danielcastelao.org",
    url="url del proyecto",
    packages = ['paquete'],
    package_data = {'paquete':files},
    scripts = ['lanzador'],
    py_modules=['lanzador'],
    long_description="""descripcion larga guuuauuuuu""",
)