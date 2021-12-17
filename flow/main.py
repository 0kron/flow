from file_reader import addPalabra, addPalabras, findRimas
from silabas import s_silabas, s_tonica, fonemas_con, fonemas_aso, cat_palabra
from term_avanzada import coloredPrint, tcolor, listedPrint
from os import system

def formatoRimas(palabra):
    palabra = palabra.lower()
    sil = []
    sil = s_silabas(palabra) #Acá metes una palabra en las paréntesis
    tonica = s_tonica(sil)
    out = " ".join(sil)
    finalSimple = "".join(sil[len(sil)-1])
    finalCon = fonemas_con(sil, tonica)
    finalAso = fonemas_aso(sil)

    tipoPalabra = cat_palabra(tonica, sil)


    coloredPrint("\n\nPalabra dividida silábicamente: \n\n\t"+out, tcolor.CYAN)
    coloredPrint(f"\nLa palabra es: {tipoPalabra}", tcolor.GREEN)
    coloredPrint("\n[1] Final de rima consonante: "+ finalCon, tcolor.BLUE)
    coloredPrint("[2] Final de rima simple: "+finalSimple, tcolor.BLUE)
    coloredPrint("[3] Final de rima asonante: "+finalAso, tcolor.BLUE)
    print("\n")
    return [finalCon, finalSimple, finalSimple]

choice = ""#Acción del usuario

#Menú de la aplicación
while choice != "quit": 
    
    #Imprimimos el menú de acciones
    system("clear") #Puede tener cambios con respecto a que OS se está utilizando
    coloredPrint("\nFlow by 0miKron", tcolor.PURPLE)
    coloredPrint("\nMenú principal de acciones: ", tcolor.BOLD)
    coloredPrint("\t[1] Encontrar rima de una palabra", tcolor.GREEN)
    coloredPrint("\t[2] Añadir nueva palabra al vocabulario.", tcolor.CYAN)
    coloredPrint("\t[3] Añadir nuevo texto al vocabulario.", tcolor.BLUE)
    coloredPrint("\t[quit] Salir.", tcolor.RED)
    choice = input(": ").lower()

    if choice == "1": #Encontrar rimas
        system("clear")
        coloredPrint("\tEncontrar Rimas\n", tcolor.GREEN)
        palabra = input(tcolor.PURPLE +"Palabra: "+tcolor.ENDC)
        finales = formatoRimas(palabra)
        choice = input(tcolor.PURPLE+"Tipo de Rima: "+tcolor.ENDC)
        
        if choice == "quit": 
            break
        
        elif choice == "1": #Rima Consonante
            rimas = findRimas(finales[0])
            listedPrint(rimas)
            choice = input(tcolor.PURPLE+"Volver al menú o salir [m/s]: "+tcolor.ENDC).lower()
            if choice == "s": 
                choice = "quit"
                
        elif choice == "2": #Rima Simple
            rimas = findRimas(finales[1])
            listedPrint(rimas)
            choice = input(tcolor.PURPLE+"Volver al menú o salir [m/s]: "+tcolor.ENDC).lower()
            if choice == "s": 
                choice = "quit"
                            
        elif choice == "3": #Rima Asonante
            rimas = findRimas(finales[2])
            listedPrint(rimas)
            choice = input(tcolor.PURPLE+"\nVolver al menú o salir [m/s]: "+tcolor.ENDC).lower()
            if choice == "s": 
                choice = "quit"

    elif choice == "2": #Añadir palabra al vocabulario
        system("clear")

        coloredPrint("\tAñadir palabra al vocabulario", tcolor.CYAN)
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
        
    elif choice == "3": #Añadir texto al vocabulario
        system("clear")

        if addPalabras():
                coloredPrint("\n\t-Operación Exitosa-", tcolor.GREEN)
        else: coloredPrint("\n\t-Operación Fallida-", tcolor.RED)
        
        #Salimos de la función
        choice = input(tcolor.PURPLE+"\nVolver al menú o salir [m/s]: "+tcolor.ENDC).lower()
        if choice == "s": 
            choice = "quit"
    
    #El else no es necesario, puesto que si no entiende, el menú se reinicia

system("clear")
coloredPrint("\n\nNos vemos pronto, vaquero...\n", tcolor.REVERSE)