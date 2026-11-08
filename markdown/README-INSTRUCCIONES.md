# Instrucciones para traducir el sitio al inglés

## ¿Qué es un archivo Markdown?

Los archivos que vas a encontrar aquí tienen extensión `.md` y se llaman **archivos Markdown**. 

Son archivos de texto muy simples, parecidos a un archivo `.txt`, pero con unos símbolos pequeños (`#`, `*`, `[]`, `()`, `-`) que sirven para organizar el texto (títulos, listas, enlaces, etc.).

La gran ventaja es que con estos símbolos podemos conservar la **misma estructura** que tiene ahora el sitio web, para que, al traducirlos y volver a pasarlos a HTML, todo quede en su lugar correcto sin tener que rehacer la página desde cero.

## ¿Para qué sirve esta carpeta?

Esta carpeta te permite traducir todo el contenido del sitio web al inglés de una manera ordenada. 

Al mantener la estructura tal como está, podremos tomar tus archivos traducidos y convertirlos de vuelta a las páginas web sin errores, reemplazando únicamente el texto.

## ¿Cómo está organizada la carpeta?

Dentro de la carpeta `markdown` encontrarás dos carpetas principales:

### 1. `estructura/` - Se traduce UNA SOLA VEZ
Aquí están los elementos que aparecen en **todas** las páginas del sitio:

- **`navegacion.md`** - El menú que está arriba (Portada, Doctorado, Plan de Estudios, etc.)
- **`pie-de-pagina.md`** - El pie de página (logotipos y redes sociales)
- **`elementos-comunes.md`** - Otros elementos que se repiten en todas las páginas

**Importante:** Si traduces estos archivos, se actualizarán automáticamente en todas las páginas.

### 2. `contenido/` - Se traduce por página
Aquí está el contenido único de cada página web:

- `index.md` - Página de inicio
- `page-presentacion.md` - Presentación del programa
- `page-academicos.md` - Académicas/os
- `page-admision.md` - Admisión
- `page-estudiantes.md` - Estudiantes y Graduadas/os
- `page-galeria.md` - Galería
- `page-investigacion.md` - Investigación
- `page-laboratorios.md` - Laboratorios
- `page-plandeestudios.md` - Plan de Estudios

Cada uno corresponde exactamente a su página en el sitio web, con el mismo nombre.

## ¿Qué debo traducir y qué NO debo tocar?

### SÍ debes traducir:
- **Títulos** (lo que aparece como encabezados)
- **Textos, párrafos y descripciones**
- **Nombres de secciones** (Objetivo general, Perfil de ingreso, etc.)
- **Textos de botones** (por ejemplo, "Saber más")
- **Listas** (mantén el mismo número y orden)
- **Texto que describe imágenes** (cuando dice algo como descripción)

### NO debes tocar bajo NINGÚN motivo:
- **Rutas de imágenes** - Todo lo que diga `assets/` debe quedar igual. Ejemplo: `assets/logo-1.png`
- **Nombres de archivos** - `index.html`, `page-presentacion.html`, etc. Deben quedarse tal como están
- **Enlaces web** - Las direcciones que empiezan con `https://...` deben quedarse iguales
- **Enlaces entre páginas** - Los enlaces como `(page-admision.html)` deben quedarse iguales, solo traduce lo que está fuera de los paréntesis
- **Lo que está dentro de paréntesis `()` en enlaces o imágenes** - Ahí van las rutas o direcciones, NO las traduzcas
- **Símbolos de Markdown** - **NO borres** `#`, `##`, `###`, `*`, `-`, `1.`, `[`, `]`, `(`, `)`. Estos son los que mantienen el orden.
- **Saltos de línea y estructura** - Respeta el orden de los títulos, párrafos y listas tal como están ahora.
- **Años o números importantes** - Como "2027" en "Admisión 2027", es mejor dejarlos tal como están
- **El formato** - Mantén las listas con el mismo tipo (con viñetas o numeradas) que ya tienen

## Cuidados para NO romper el archivo

- **No añadas símbolos nuevos.** Usa solo traducción de texto.
- **No elimines líneas vacías** si las hay entre secciones. Muchas veces ayudan a mantener la separación entre bloques.
- **No cambies el orden.** Si un título va primero y luego una lista, debe seguir así después de traducir.
- **Cuidado con los corchetes y paréntesis.** Estos SIEMPRE van juntos: `[Texto a traducir](ruta-que-NO-se-traduce)`. Traduce solo lo que está dentro de los corchetes.
- **Guarda siempre como archivo `.md`** (Markdown). No lo guardes como `.txt`, `.docx` o `.html`.
- **Si tienes dudas, deja tal como está.** Es mucho más seguro dejar una ruta o símbolo sin tocar, que borrarlo por error.

## Consejos prácticos

1. **Empieza por la estructura.** Traduce primero `navegacion.md`, `pie-de-pagina.md` y `elementos-comunes.md`. Con eso ya tienes traducido lo que aparece en todas las páginas.
2. **Luego ve por contenido.** Traduce cada archivo de la carpeta `contenido/` uno por uno, manteniendo el mismo orden.
3. **Traduce solo el texto visible.** Si ves `[Conoce nuestro programa](page-presentacion.html)`, traduce solo `Conoce nuestro programa`, deja `(page-presentacion.html)` exactamente igual.
4. **Cuida las imágenes.** Si ves `![Foto del Director](assets/manuel-ortiz-parada.jpg)`, puedes traducir `Foto del Director` si lo deseas, pero **nunca** cambies `assets/manuel-ortiz-parada.jpg`.
5. **Piensa en "volver a armar".** Imagina que alguien va a tomar **exactamente** este archivo traducido para pegarlo de vuelta en el sitio web. Si rompes los símbolos o el orden, no podrá volver a armarlo correctamente.
6. **No te preocupes por el diseño.** Los colores, estilos y posición se mantienen en el sitio web original. Tú solo necesitas traducir el texto.

## Regla de oro

**Traduce lo que LEES, no lo que APUNTA.**

Todo lo que te indica hacia dónde ir (rutas, archivos, direcciones web) debe quedarse exactamente igual. Todo lo que una persona vería escrito en la página, sí se traduce.

**La clave:** Mantén la estructura tal como está. Si conservas los símbolos, el orden y las rutas sin tocarlos, el regreso de estos archivos a HTML será rápido, limpio y sin problemas.
