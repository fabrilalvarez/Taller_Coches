import os,sys

def determina_path():

    try:
        root=__file__
        if os.path.islink(root):
                root=os.path.realpath(root)
        return os.path.dirname(os.path.abspath(root))
    except:
        print("...")
        sys.exit()

def start():
    print("el modulo funciona")
    print(determina_path())
    ficheros = {f for f in os.listdir(determina_path()+ "/cosas")}
    print(ficheros)

if __name__=="__main__":
    print("Decide que tiene que hacer")

