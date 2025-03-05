def construir_lista_invertida(documentos):
    indice_invertido = {}

    for doc_id, texto in enumerate(documentos, start=1): # Los documentos tienen IDs 1, 2, 3 ...
        palabras = texto.lower().split() # Convertimos a minusculas y separamos en palabras

        for palabra in palabras:
            if palabra not in indice_invertido:
                indice_invertido[palabra] = {} # Si no existe, creamos el diccionario

            if doc_id not in indice_invertido[palabra]:
                indice_invertido[palabra][doc_id] = 0 # Inicializamos el contador

            indice_invertido[palabra][doc_id] += 1 # Incrementamos el contador
 
    return indice_invertido

def buscarPalabra(index, word):
    print(index)
    if word in index:
        print(f"Encontrado ({word}) en: ")
        for doc, count in index[word].items():
            print(f"  Documento{doc} ")
    else:
        print(f"{word} no encontrado")

# Extender la implementación para soportar búsquedas de varias palabras.
# Agregar la capacidad de contar cuántas veces aparece cada palabra en cada documento.
def buscarPalabras(index, words):
    if isinstance(words, str):
        words = words.split()
    
    result = ""
    for word in words:
        if word in index:
            result += f"\nPalabra ({word}): conteo de aparicion\n"
            for doc, count in index[word].items():
                result += f"  En doc{doc}: {count} veces\n"
        else:
            result += f"\n{word} no encontrado\n"
    print(result)
        

# Documentos de ejemplo
documentos = [
"el gato perro gato está durmiendo",
"el perro está jugando",
"el gato y el perro son amigos"
]

indice = construir_lista_invertida(documentos)

# Implementar una consulta - ACT 2
for palabra, docs in indice.items():
    print(f"{palabra}: {docs}")
    
buscarPalabra(indice, "gato") #IMPLEMENTADO ACT2
buscarPalabras(indice, "perro gato") #IMPLEMENTADO ACT3
