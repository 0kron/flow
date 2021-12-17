from file_reader import addPalabra, addPalabras, findRimas, removePalabra
from silabas import s_silabas, s_tonica, fonemas_con, fonemas_aso, cat_palabra
from term_avanzada import coloredPrint, tcolor, listedPrint
from os import system

def formatoRimas(palabra): #Format of the rhymes menu
    palabra = palabra.lower()
    sil = []
    sil = s_silabas(palabra) #Obtener la separación silábica - Get the syllabic separation
    tonica = s_tonica(sil) #Obtener la sílaba tónica - Get the tonic syllable
    out = " ".join(sil)

    #Obtener los distintos finales para los tipos de rima - Get the different ends for the different rhymes
    finalSimple = "".join(sil[len(sil)-1])
    finalCon = fonemas_con(sil, tonica)
    finalAso = fonemas_aso(sil)

    tipoPalabra = cat_palabra(tonica, sil)

    #Hay trés tipos de rimas principales en el español
    #   * La rima CONSONANTE - coinciden todos los fonemas desde las vocales tónicas
    #   * La rima SIMPLE - coinciden todos los fonemas de la última sílaba
    #   * La rima ASONANTE - coinciden todos los fonemas desde la primera vocal de la última sílaba

    coloredPrint("\n\nPalabra dividida silábicamente: \n\n\t"+out, tcolor.CYAN)
    coloredPrint(f"\nLa palabra es: {tipoPalabra}", tcolor.GREEN)
    coloredPrint("\n[1] Final de rima consonante: "+ finalCon, tcolor.BLUE)
    coloredPrint("[2] Final de rima simple: "+finalSimple, tcolor.BLUE)
    coloredPrint("[3] Final de rima asonante: "+finalAso, tcolor.BLUE)
    print("\n")
    return [finalCon, finalSimple, finalSimple] #Lisra de los finales - List of the ends


def main():
    choice = ""#Acción del usuario - User input

    #Menú de la aplicación - Program menu
    while choice != "quit": 
    
        #Imprimimos el menú de acciones
        system("clear") #Puede tener cambios con respecto a que OS se está utilizando
        coloredPrint("\nFlow by 0miKron", tcolor.PURPLE)
        coloredPrint("\nMenú principal de acciones: ", tcolor.BOLD)
        coloredPrint("\t[1] Encontrar rima de una palabra.", tcolor.GREEN)
        coloredPrint("\t[2] Añadir nueva palabra al vocabulario.", tcolor.CYAN)
        coloredPrint("\t[3] Añadir nuevo texto al vocabulario.", tcolor.BLUE)
        coloredPrint("\t[4] Quitar palabra del vocabulario.", tcolor.ORANGE)
        coloredPrint("\t[quit] Salir.", tcolor.RED)
        choice = input(": ").lower()

        if choice == "1": #Encontrar rimas - Find rhymes
            system("clear")
            coloredPrint("\tEncontrar Rimas\n", tcolor.GREEN)
            palabra = input(tcolor.PURPLE +"Palabra: "+tcolor.ENDC)
            finales = formatoRimas(palabra)
            choice = input(tcolor.PURPLE+"Tipo de Rima: "+tcolor.ENDC)
            
            if choice == "quit": 
                break
            
            elif choice == "1": #Rima Consonante - Consonant Rhymes
                rimas = findRimas(finales[0])
                    
            elif choice == "2": #Rima Simple - Simple Rhymes
                rimas = findRimas(finales[1])
                                
            elif choice == "3": #Rima Asonante - Assonant Rhymes
                rimas = findRimas(finales[2])
            
            print(tcolor.CYAN)
            listedPrint(rimas) #Imprimir las rimas - Print Rhymes
            print(tcolor.ENDC)
            choice = input(tcolor.PURPLE+"\nVolver al menú o salir [m/s]: "+tcolor.ENDC).lower()
            if choice == "s": 
                choice = "quit"

        elif choice == "2": #Añadir palabra al vocabulario - Add single word to the vocabulary
            system("clear")

            coloredPrint("\tAñadir palabra al vocabulario\n", tcolor.CYAN)
            palabra = input(tcolor.PURPLE +"Palabra: "+tcolor.ENDC).lower()

            #Confirmamos la palabra
            choice = input(f"La palabra: {tcolor.GREEN+palabra+tcolor.ENDC} está bien escrita? [s/n]: ").lower()
            if choice == "s":

                if addPalabra(palabra):
                    coloredPrint("\n\t-Operación Exitosa-", tcolor.GREEN)
                else: coloredPrint("\n\t-Operación Fallida-", tcolor.RED)

                #Salimos de la función
                choice = input(tcolor.PURPLE+"\nVolver al menú o salir [m/s]: "+tcolor.ENDC).lower()
                if choice == "s": 
                    choice = "quit"
            
        elif choice == "3": #Añadir texto al vocabulario - Add text to the vocabulary
            system("clear")

            if addPalabras():
                    coloredPrint("\n\t-Operación Exitosa-", tcolor.GREEN)
            else: coloredPrint("\n\t-Operación Fallida-", tcolor.RED)
            
            #Salimos de la función
            choice = input(tcolor.PURPLE+"\nVolver al menú o salir [m/s]: "+tcolor.ENDC).lower()
            if choice == "s": 
                choice = "quit"        

        elif choice == "4": #Quitar palabra del vocabulario - 
            system("clear")

            coloredPrint("\tQuitar palabra del vocabulario\n", tcolor.CYAN)
            palabra = input(tcolor.PURPLE +"Palabra: "+tcolor.ENDC).lower()

            #Confirmamos la palabra
            choice = input(f"La palabra: {tcolor.GREEN+palabra+tcolor.ENDC} está bien escrita? [s/n]: ").lower()
            if choice == "s":

                if removePalabra(palabra):
                    coloredPrint("\n\t-Operación Exitosa-", tcolor.GREEN)
                else: coloredPrint("\n\t-Operación Fallida-", tcolor.RED)

                #Salimos de la función
                choice = input(tcolor.PURPLE+"\nVolver al menú o salir [m/s]: "+tcolor.ENDC).lower()
                if choice == "s": 
                    choice = "quit"
        
        #El else no es necesario, puesto que si no entiende, el menú se reinicia

    system("clear")
    coloredPrint("\n\nNos vemos pronto, vaquero...\n", tcolor.REVERSE)


if __name__ == "__main__": 
    main()