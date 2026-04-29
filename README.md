# Cifrador Hill Matricial

Programa de cifrado y descifrado de mensajes basado en el **cifrado Hill**, aplicando conceptos de álgebra lineal como multiplicación de matrices e inversas matriciales.

---

## Cómo funciona

### Encriptar

El programa recibe un mensaje de texto y lo convierte en un vector de índices numéricos usando un alfabeto de 28 caracteres (espacio + a-z + ñ). Luego genera una matriz aleatoria n×n (donde n es la longitud del mensaje) garantizando que su determinante sea distinto de cero, condición necesaria para que exista su inversa. Finalmente calcula la **clave pública** multiplicando esa matriz por el vector del mensaje:

```
clavePublica = M × mensaje
```

Los resultados se guardan en dos archivos JSON:

- `encryptador.json` — la matriz encriptadora M
- `clavePublica.json` — el mensaje cifrado

### Desencriptar

Carga los dos archivos JSON, calcula la **inversa** de la matriz encriptadora con NumPy, y recupera el mensaje original:

```
mensaje = M⁻¹ × clavePublica
```

Los valores se redondean al entero más cercano y se traducen de vuelta a caracteres usando el mismo alfabeto.

---

## Requisitos

```
pip install numpy
```

---

## Uso

```bash
python cifrador.py
```

Selecciona `1` para encriptar o `2` para desencriptar. Al desencriptar se pedirán las rutas de los archivos `.json` generados en el paso anterior.

---

## Alfabeto soportado

El programa reconoce los siguientes 28 caracteres:

```
[ espacio, a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z ]
```

Cualquier carácter fuera de este conjunto será ignorado silenciosamente.
