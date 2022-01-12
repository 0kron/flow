#Separación Silábica 

vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
vocaFuertes = ["a", "e", "o", "á", "é", "ó", "í", "ú"]
vocaDebiles = ["i", "u"]

consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
consonantesCompuestas = ["bl", "br", "cr", "cl", "ch", "dr", "gr", "gl", "ll",  "kl", "kr", "pr", "pl", "sh" , "fr", "fl", "tl", "tr", "rr"]
consonantesCompuestasFin = ["ns", "bs"]

def s_silabas(palabra):

    palabra = palabra.lower()
    puntero = 0
    silabas = []     
    
    while puntero + 3 <= len(palabra): 
        letra = palabra[puntero]
        
        #Consideraciones generales para vocales y consonantes
        if letra in vocales: 
            siguiente = palabra[puntero+1]
            grupo = palabra[puntero+1:puntero+3]
            
            #Consideraciones de vocales débiles:
            if letra in vocaDebiles: 
                if siguiente in vocaFuertes: puntero+=1 #Se hace un diptongo vocal Débil + Fuerte

                elif siguiente in vocaDebiles: #Si son dos vocales débiles se termina en la primera "chi-i-ta"
                    puntero += 1
                    silabas.append(palabra[:puntero])
                    palabra = palabra[puntero:]
                    puntero=0 

            #Consideraciones de vocales Fuertes: 
            if letra in vocaFuertes: 
                if  siguiente in vocaDebiles: puntero +=1 #Se hace el otro tipo de diptongo Fuerte + Débil
                
                elif siguiente in vocaFuertes: #Se hace un hiato: "ha-bla-rí-a"
                    puntero += 1
                    silabas.append(palabra[:puntero])
                    palabra = palabra[puntero:]
                    puntero=0 

            #Consideraciones para todas las vocales           
            if grupo in consonantesCompuestas: #Si le sigue una consonante compuesta termina de una "pa-la-bra"
                puntero += 1
                silabas.append(palabra[:puntero])
                palabra = palabra[puntero:]
                puntero=0 
            
            elif grupo in consonantesCompuestasFin: #Si la sílaba termina con "bs" o "ns": obs-cu-ro
                puntero += 3
                silabas.append(palabra[:puntero])
                palabra = palabra[puntero:]
                puntero=0

            elif siguiente in consonantes and palabra[puntero+2:puntero+3] in vocales: #Si sigue consonante y vocal "Gru-po"
                puntero += 1
                silabas.append(palabra[:puntero])
                palabra = palabra[puntero:]
                puntero=0 

            elif siguiente in consonantes and palabra[puntero+2:puntero+3] in consonantes: #Si siguen dos consonantes termina en la primera consonante "cam-pa-na"
                puntero += 2
                silabas.append(palabra[:puntero])
                palabra = palabra[puntero:]
                puntero=0 

        else: puntero+=1 #No puede haber sílaba sin vocal
    
    else: 
        puntero = 0
        while puntero < len(palabra)-1:
            if palabra[puntero] in vocaFuertes and palabra[puntero+1] in vocaFuertes: 
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

def fonemas_con(sil, tonica):
    string = "".join(sil[tonica:])
    if string[0:2] in consonantesCompuestas: string = string[2:]
    elif string[0:1] in consonantes: string = string[1:]
    return string 

def fonemas_aso(sil): 
    string = "".join(sil[-1:])
    if string[0:2] in consonantesCompuestas: string = string[2:]
    elif string[0:1] in consonantes: string = string[1:]
    return string


