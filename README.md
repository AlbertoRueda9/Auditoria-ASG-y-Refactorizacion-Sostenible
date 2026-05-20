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

# Fase 2: Dimensión Social y Equidad (S)

## Test de Accesibilidad

Pulsamos F12 dentro de la web, seleccionamos la herramienta Lighthouse, y seleccionamos la categoría de accesibilidad, una vez hecho esto. Pulsamos en analizar la página.

<img width="1913" height="965" alt="image-1" src="https://github.com/user-attachments/assets/02e2221d-a42e-46c5-a080-9c59aff189a0" />

<img width="550" height="421" alt="image-2" src="https://github.com/user-attachments/assets/9304cbb0-76e9-444e-9f61-57b75bf46495" />


## Identificación de barreras

He documentado 2 erroes que hacen que algunos usuarios con diversidad funcional no puedan usar la web de forma correcta.

### Los enlaces dependen únicamente del color para poder distinguirse

<img width="518" height="390" alt="image-3" src="https://github.com/user-attachments/assets/20eb0bde-df28-4222-b143-2105b59a22c1" />

Este problema de accesibilidad hace que los enlaces solo dependen de un único color para distinguirse, por lo que esto sería un problema para personas con daltonismo o dificultades visuales. Como solución debería de añadirse subrayado a los enlaces, iconos o cambios de estilo.

### Los enlaces no tienen un nombre reconocible o identificable

<img width="522" height="441" alt="image-4" src="https://github.com/user-attachments/assets/c9dc8d4a-874e-4ba4-a9c6-5a5a6f958496" />


Los enlaces gráficos de la web no tienen nombres accesibles reconocibles para tecnologías asistivas. Volvería a afectar a personas con los problemas anteriores. Los usuarios que utilizan lectores de pantalla no pueden identificar correctamente el propósito de los enlaces o imágenes clicables.
