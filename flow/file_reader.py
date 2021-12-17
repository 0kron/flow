#Leer y escribir de un archivo .txt en python
from os import system

def cleanLine(linea): 
    linea = linea.replace("?", "")
    linea = linea.replace(",", "")
    linea = linea.replace(".", "")
    linea = linea.replace("¿", "")
    linea = linea.replace("!", "")
    linea = linea.replace("¡", "")
    linea = linea.replace(";", "")
    linea = linea.replace(":", "")
    linea = linea.replace("'", "")
    linea = linea.replace('"', '')
    linea = linea.replace("/", "")
    linea = linea.replace("(", "")
    linea = linea.replace(")", "")
    return linea.lower()


def getPalabras():
    f = open("kronPy/rimas/palabras.txt")

    #limpiarReader = lambda lista: for elemento in lista elemento.replace("\n", "") and elemento.replace(" ", "")
    lectura = f.readlines()
    f.close()

    palabras = []
    numPalabras = 0

    for linea in lectura: 
        if linea.strip() == "": break
        palabras.append(linea.strip())
        numPalabras+=1

    return palabras


def addPalabras(): 
    try:
        #Preposiciones en español
        preposiciones = ["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "en", 
                        "entre", "hacia", "hasta", "para", "por", "según", "sin", "sobre", "tras"]


        ##El programa obtiene todas las palabras ya guardadas:
        vocabulario = getPalabras()

        ##Abrimos el documento para escribir sobre él: 
        vocabularioW = open("kronPy/rimas/palabras.txt", "w")


        ##Que el usuario coloque su texto:
        system("gedit /home/kron/Documents/kronDev/kronPy/rimas/nuevoVocab.txt")

        #Se abre el texto que puso el usuario
        entrada = open("/home/kron/Documents/kronDev/kronPy/rimas/nuevoVocab.txt", "r")
        lectura = entrada.readlines()
        entrada.close()

        #Se añaden las nuevas palabrasa la lista: 
        for linea in lectura: 
            linea = cleanLine(linea)
            palabras = linea.split()
            for palabra in palabras: 
                if palabra not in vocabulario and palabra not in preposiciones: vocabulario.append(str(palabra))

        #Escribimos la lista en el documento: 
        for palabra in vocabulario: vocabularioW.write(palabra+"\n")
        vocabularioW.close()

        ##Se limpia el texto de nuevoVocab
        formato = open("kronPy/rimas/nuevoVocab.txt", "w")
        formato.write("\n...Borre este texto y pegue el texto escogido, guarde y cierre.")
        formato.close()
        return True

    except: return False


def addPalabra(palabra): 
    try:
        vocabulario = getPalabras()

        ##Abrimos el documento para escribir sobre él: 
        vocabularioW = open("kronPy/rimas/palabras.txt", "w")

        if palabra not in vocabulario: vocabulario.append(palabra)
        for palabra in vocabulario: vocabularioW.write(palabra +"\n")
        vocabularioW.close()
        return True
    except: 
        return False


def removePalabra(palabra): 
    vocabulario = getPalabras() 
    try: 
        vocabulario.remove(palabra)
        vocabularioW = open("kronPy/rimas/palabras.txt", "w")
        for palabra in vocabulario: vocabularioW.write(palabra +"\n")
        vocabularioW.close()
    except: pass


def findRimas(final): 
    rimas = []
    palabras = getPalabras()
    for palabra in palabras: 
        if palabra[-len(final):] == final: rimas.append(palabra)
    return rimas


def findAli(inicio): #Futura adición de encontrar aliteraciones
    aliteraciones = []
    palabras = getPalabras()
    for palabra in palabras: 
        if palabra[:len(inicio)+1] == inicio: aliteraciones.append(palabra)

