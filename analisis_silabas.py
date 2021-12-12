#Separación Silábica 

vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
vocaFuertes = ["a", "e", "o", "á", "é", "ó", "í", "ú"]
vocaDebiles = ["i", "u"]

consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
consonantesCompuestas = ["bl", "br", "cr", "cl", "ch", "dr", "gr", "gl", "ll",  "kl", "kr", "pr", "pl", "sh" , "fr", "fl", "tl", "tr", "rr"]

def s_silabas(palabra):

    palabra = palabra.lower()
    puntero = 0
    silabas = []          
    
    while puntero + 3 <= len(palabra): 

        if palabra[puntero:puntero+1] in vocaDebiles and palabra[puntero+1:puntero+2] in vocaFuertes: puntero+=1

        elif palabra[puntero:puntero+1] in vocales: 
            if palabra[puntero+1:puntero+3] in consonantesCompuestas: #Si le sigue una consonante compuesta termina de una "pa-la-bra"
                puntero += 1
                silabas.append(palabra[:puntero])
                palabra = palabra[puntero:]
                puntero = 0

            elif palabra[puntero+1:puntero+2] in consonantes and palabra[puntero+2:puntero+3] in vocales: #Si sigue consonante y vocal "Gru-po"
                puntero += 1
                silabas.append(palabra[:puntero])
                palabra = palabra[puntero:]
                puntero = 0

            elif palabra[puntero+1:puntero+2] in consonantes and palabra[puntero+2:puntero+3] in consonantes: #Si siguen dos consonantes termina en la primera consonante "mi-er-da"
                puntero +=2
                silabas.append(palabra[:puntero])
                palabra = palabra[puntero:]
                puntero = 0

            elif palabra[puntero+1:puntero+2] in vocaDebiles: puntero+=1

            elif palabra[puntero+1:puntero+2] in vocaFuertes: 
                puntero+=1
                silabas.append(palabra[:puntero])
                palabra = palabra[puntero:]
                puntero = 0

        else: puntero+=1
    else: 
        puntero = 0
        while puntero < len(palabra)-1:
            if palabra[puntero:puntero+1] in vocaFuertes and palabra[puntero+1:puntero+2] in vocaFuertes: 
                silabas.append(palabra[:puntero+1])
                silabas.append(palabra[puntero+1:])
                break
            else: puntero += 1
        else: silabas.append(palabra)
                
    return silabas

def s_tonica(silabas = [""]):
    i = 0
    while i < len(silabas): 
        for v_acentuada in vocales[5:]: 
            if silabas[i].find(v_acentuada) != -1:  
                return i
        i += 1
    else: 
        final = silabas[len(silabas)-1]
        if final[len(final)-1] in ["n", "s", "a", "e", "i", "o", "u"]: 
            return len(silabas)-2
        else: return len(silabas) - 1

def cat_palabra(i, silabas): 
    if i == len(silabas)-1: return "aguda"
    elif i == len(silabas) -2: return "grave"
    elif i == len(silabas) - 3: return "esdrújula"
    else: return "subesdrújulas"

def ter_consonante(i, silabas):
    return "".join(silabas[i:])

def ter_asonante(silabas): 
    i = 0
    while i<len(silabas[-1]) and silabas[-1][i] not in vocales:
        i+=1
    else: return silabas[-1][i:]

def ter_simple(silabas): 
    return silabas[-1]

def ini_aliteracion(silabas): 
    i = 0
    while i<len(silabas[0]) and silabas[0][i] not in vocales: 
        i+=1
    return silabas[0][:i+1]

def main():

    print("\n\n\t---Programa de separación silábica---")
    palabra = input("\nIngrese su palabra: ")
    sil = []
    sil = s_silabas(palabra) #Acá metes una palabra en las paréntesis
    out = " ".join(sil)
    tipoPalabra = cat_palabra(s_tonica(sil), sil)
    terminacionCon = ter_consonante(s_tonica(sil), sil)
    terminacionAs = ter_asonante(sil)
    terminacionSim = ter_simple(sil)
    iniAliteracion = ini_aliteracion(sil)


    print("\n\nPalabra en sílabas: "+out)
    print("Tipo de palabra: "+tipoPalabra)
    print("\nTerminación de rima asonante: "+terminacionAs)
    print("Terminación de rima simple: "+terminacionSim)
    print("Terminación de rima consonante: "+terminacionCon)
    print("Inicio para aliteración: "+iniAliteracion)
    print("\n")


if __name__ == "__main__": 
    main()
