def construir_lista_invertida(documentos):
    indice_invertido = {}

    for doc_id, texto in enumerate(documentos, start=1): # Los documentos tienen IDs 1, 2, 3 ...
        palabras = texto. lower() .split() # Convertimos a minusculas y separamos en palabras

        for palabra in palabras:
            if palabra not in indice_invertido:
                indice_invertido[palabra] = [] # Si no existe, creamos la lista

            if doc_id not in indice_invertido[palabra]:
                indice_invertido[palabra].append(doc_id) # Evitamos duplicados
 
    return indice_invertido

def buscarPalabra(index, word):
    if word in index:
        print(f"{word}: {index[word]}")
    else:
        print(f"{word} no encontrado")

# Documentos de ejemplo
documentos = [
"el gato está durmiendo",
"el perro está jugando",
"el gato y el perro son amigos"
]

indice = construir_lista_invertida(documentos)

# Implementar una consulta - ACT 2
for palabra, docs in indice.items():
    print(f"{palabra}: {docs}")
    
buscarPalabra(indice, "gato") #IMPLEMENTADO