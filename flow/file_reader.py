#Leer y escribir de los archivos *.txt

#Read and write from the *.txt files

from os import system

#Rutas, preferentemente las rutas absolutas de acceso a los archivos de texto
#Paths, preferably Absolute paths to the text files
palabrasPath = "../flow/palabras.txt" #Dónde se guarden las palabras - Storage of the words
vocabularioPath = "../flow/nuevoVocab.txt" #El archivo para añadir nuevas palabras - To add new words
txtEditor = "gedit" #Coloque aquí el nombre de su editor de *.txt
                    #Para uso general se puede usar <vim>
                    #En Distribuciones de Linux se pueden usar <gedit>, <nano>, etc
                    #Para Windows use <notepad>
                    #Para MacOS use <open -a TextEdit>

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


def getPalabras(): #Todas las palabras ya aprendidas - All the already stored words
    f = open(palabrasPath)

    lectura = f.readlines()
    f.close()

    palabras = []
    numPalabras = 0

    for linea in lectura: 
        if linea.strip() == "": break
        palabras.append(linea.strip())
        numPalabras+=1

    return palabras 


def addPalabras(): #Añadir un texto para nuevo vocabulario - Use a text to add new vocabulary
    try:
        #Preposiciones en español - Spanish prepositions
        preposiciones = ["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "en", 
                        "entre", "hacia", "hasta", "para", "por", "según", "sin", "sobre", "tras"]


        ##El programa obtiene todas las palabras ya guardadas - Already stored words:
        vocabulario = getPalabras()

        ##Abrimos el documento para escribir sobre él - Make the document of words writable
        vocabularioW = open(palabrasPath, "w")


        ##Que el usuario coloque su texto - Input of the text
        system(txtEditor+" "+vocabularioPath) #Cambie gedit por su editor de texto predilecto - Change gedit for your preferred text editor program

        #Se abre el texto que puso el usuario - Read input
        entrada = open(vocabularioPath, "r")
        lectura = entrada.readlines()
        entrada.close()

        #Se añaden las nuevas palabras a la lista - Selecting new words
        for linea in lectura: 
            linea = cleanLine(linea)
            palabras = linea.split()
            for palabra in palabras: 
                if palabra not in vocabulario and palabra not in preposiciones: vocabulario.append(str(palabra))

        #Escribimos la lista en el documento - Saving new words
        for palabra in vocabulario: vocabularioW.write(palabra+"\n")
        vocabularioW.close()

        ##Se limpia el texto de nuevoVocab - Cleaning the input file for further use
        formato = open(vocabularioPath, "w")
        formato.write("\n...Borre este texto y pegue el texto escogido, guarde y cierre.")
        formato.close()
        return True

    except: return False


def addPalabra(palabra): #Añadir una única palabra - Adding a single word
    try: 
        vocabulario = getPalabras()

        ##Abrimos el documento para escribir sobre él: 
        vocabularioW = open(palabrasPath, "w")

        if palabra not in vocabulario: vocabulario.append(palabra)
        for palabra in vocabulario: vocabularioW.write(palabra +"\n")
        vocabularioW.close()
        return True
    except: 
        return False


def removePalabra(palabra): #Borrando una palabra si está en el documento de texto - Deleting a word if stored in the .txt
    vocabulario = getPalabras() 
    try: 
        vocabulario.remove(palabra)
        vocabularioW = open(palabrasPath, "w")
        for palabra in vocabulario: vocabularioW.write(palabra +"\n")
        vocabularioW.close()
        return True
    except: return False


def findRimas(final, original): #Encontrar rimas con terminación especificada - Find specific rimes according to the end
    rimas = []
    palabras = getPalabras()
    for palabra in palabras: 
        if palabra[-len(final):]== final and palabra != original: rimas.append(palabra)
    return rimas


def findAli(inicio): #Futura adición de encontrar aliteraciones - Later update to find aliterations
    aliteraciones = []
    palabras = getPalabras()
    for palabra in palabras: 
        if palabra[:len(inicio)+1] == inicio: aliteraciones.append(palabra)

