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

# Fase 3: Dimensión de Gobernanza y Ética (G)

## Transparencia

<img width="1907" height="235" alt="image-5" src="https://github.com/user-attachments/assets/6fe7154f-e6f3-431a-8f96-dd48f46a082e" />


La web solo marca la opción de aceptar las cookies, sin embargo La web permite cerrar el banner de cookies mediante un icono “X”, lo que ofrece cierta capacidad de rechazo implícito.

## Datos innecesarios

<img width="1202" height="730" alt="image-6" src="https://github.com/user-attachments/assets/d5dc106d-748d-4891-8676-19d66d64166e" />


Hagles S.L es una empresa que se dedica a la venta de hornos industriales, por lo que sus principales clientes son grandes empresas. En el formuario se nos pide Nombre y apellidos y cargo, por lo que entiendo que la empresa cliente enviará a un alto cargo para solicitar información sobre los productos de Hagles. También la ciudad y país, entiendo que este dato es importante por si en caso de compra, hagles pudiera valorar si puede realizar un envío de un producto de grandes dimesiones otros sitios lejanos.

Concluyendo, creo que valorando el contexto, todos los datos del formulario son necesarios.

# Fase 4: Propuesta de Refactorización (Green Coding)

## Optimización de activos.

Usaría principalmente:

- AVIF: Para imágenes grandes decorativas, comprime mejor y reduce el peso.

- WebP: Como formato alternativo compatible con más navegadores

El loading lazy lo implementaría sobre todo en imágenes que no aparezcan en la página de inicio para que no se descargue todo a la vez y se haga más pesado

## Reducción de peticiones.

## Reflexión sobre la Paradoja de Jevons.

Para evitar un colapso de la web en caso de éxito que anule el ahorro energético, aplicaría medidas de escabilidad sostenible:

- Uso de CDN: Menor carga de servidor principal, reduce latencia y por tanto consumo energético por transferencia de datos

- Sistemas de caché avanzados: con un caché agresivo tanto en el navegador como el servidor se producirían menos peticiones, dando lugar a un menor consumo de CPU y red

- Arquitectura sostenible: cada visita consume menos energía con uso de práctica como loading lazy, carga modular... etc

- Optimización continua de recursos: El resultado de esta medida sería evitar que vuelva a aparecer u software sobrecargado
