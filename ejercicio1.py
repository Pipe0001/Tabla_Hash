

class HashTable:
    def __init__(self, tamaño=10, tipo_hash="creativa"):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]
        self.tipo_hash = tipo_hash  # "knuth", "xor", "simple", "creativa"

    # 1. Hash Multiplicativa (Knuth)
    def hash_knuth(self, clave):
        AUREA_INVERSA = 0.6180339887
        valor = sum(ord(c) for c in clave)
        fraccion = (valor * AUREA_INVERSA) % 1
        return int(self.tamaño * fraccion)

    # 2. Hash con Desplazamiento y XOR
    def hash_xor(self, clave):
        hash_val = 0
        for c in clave:
            hash_val ^= (hash_val << 5) ^ (hash_val >> 2) ^ ord(c)
        return hash_val % self.tamaño

    # 3. Hash simple con suma y número primo (31)
    def hash_simple(self, clave):
        total = sum(ord(c) for c in clave)
        return (total * 31) % self.tamaño

    # 4. Tu función hash creativa (alternando suma y resta)
    def hash_creativa(self, clave):
        total = 0
        for i, letra in enumerate(clave):
            if i % 2 == 0:
                total += ord(letra)
            else:
                total -= ord(letra)
        return abs(total * 31) % self.tamaño

    # Elegir qué función hash usar según el tipo
    def calcular_hash(self, clave):
        if self.tipo_hash == "knuth":
            return self.hash_knuth(clave)
        elif self.tipo_hash == "xor":
            return self.hash_xor(clave)
        elif self.tipo_hash == "simple":
            return self.hash_simple(clave)
        else:
            return self.hash_creativa(clave)

    # Insertar par clave-valor
    def insert(self, clave, valor):
        indice = self.calcular_hash(clave)
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                self.tabla[indice][i] = (clave, valor)
                return
        self.tabla[indice].append((clave, valor))

    # Buscar valor por clave
    def search(self, clave):
        indice = self.calcular_hash(clave)
        for k, v in self.tabla[indice]:
            if k == clave:
                return v
        return None

    # Eliminar un par clave-valor
    def delete(self, clave):
        indice = self.calcular_hash(clave)
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                del self.tabla[indice][i]
                return True
        return False

    # Mostrar el contenido de la tabla
    def __str__(self):
        resultado = ""
        for i, lista in enumerate(self.tabla):
            resultado += f"Cajón {i}: {lista}\n"
        return resultado






# Puedes probar con cualquiera: "knuth", "xor", "simple", "creativa"

print("📌 Usando tu función hash XOR:")
tabla = HashTable(tamaño=10, tipo_hash="xor")
tabla.insert("a", "valor de a")
tabla.insert("b", "valor de b")
tabla.insert("c", "valor de c")

print(tabla)

# Buscar y eliminar para probar:
print("Buscar 'b':", tabla.search("b"))
tabla.delete("b")
print("Después de borrar 'b':")
print(tabla)
