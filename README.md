# Auditoría ASG y Refactorización Sostenible

### Alberto Rueda Romero

### Sostenibilidad Aplicada al Sistema Productivo

### 1ºDAW

# Fase 1: Inventario y Dimensión Ambiental (A)

La empresa elegida para esta actividad es Hagles S.L. (https://www.hagles.com)

## Medición inicial

Hemos realizado una medición inicial de la URL con "Website Carbon Calculator"

Esta página califica la huella de carbono en unos rangos de A+,A,B,C,D,E y F.

<img width="1258" height="826" alt="image" src="https://github.com/user-attachments/assets/20f90562-3f9d-4a42-a3e5-85b6a4de23e7" />


El resultado obtenido ha sido una calificación D, mostrando un mensaje que dice que esta página es más sucia que el 51% de webs del mundo.

## Identificación de Bloatware

Haciendo Ctrl+U dentro de la web podemos ver el html de la web, que hemos añadido.

Esta web cuenta con contenido multimedia muy pesado y recursos bastante mal, o poco optimizados.

Los principales son:

### Imagenes

Usa fotografías de gran tamaño con formato png o jpg, en las que no se aprecia el uso de formatos eficientes como WebP o AVIF. Tampoco existe la carga diferida (Loady Lazing), si no que la web las descarga al instante.

### Librerias JavaScript y plugins heredados

Usa estructuras de plantillas antiguas con menús y sliders y el uso de librerias completas para funciones simples.

### Recursos múltimedia y catálogo

Se descargan completas documentos pesados.

## Análisis.

Con todo lo anterior, podemos concluir que la web presenta inflacción de software por que contiene archivos multimedia con formato poco obsoleto y ausencia de modernos con WebP.

Se implementan cargas de JavaScripts para funciones simples como sliders, animaciones, o efectos de scroll. Todo ello hoy día puede sustiturse por CSS moderno o JavaScript nativo.

Usa una plantillla con múltiples recursos cargados desde el principio que hace demasiadas peticiones HTTP y falta de carga diferida.
