# Fase 1: Inventario y Dimensión Ambiental (A)

Analiza el peso y consumo de la web elegida.

## Medición inicial. Utiliza herramientas gratuitas como Website Carbon Calculator o Lighthouse (pestaña de rendimiento en Chrome/Edge) para obtener la huella de carbono estimada por visita.

## Identificación de Bloatware. Inspecciona la red (Network) en las herramientas de desarrollador del navegador. Identifica los 3 recursos más pesados que se descargan al abrir la web (imágenes sin comprimir, vídeos de fondo, librerías JavaScript pesadas, etc.).

## Análisis. ¿Crees que la web sufre de "inflación de software"? Justifica tu respuesta.

# Fase 2: Dimensión Social y Equidad (S)

La web debe ser utilizable por todos. Evalúa la accesibilidad (Sostenibilidad Social):

## Test de Accesibilidad. Pasa una herramienta como WAVE Web Accessibility Evaluation Tool o el propio Lighthouse (pestaña Accessibility).

## Identificación de barreras. Documenta al menos 2 problemas graves que impidan a personas con diversidad funcional usar la web correctamente (ej. falta de atributos alt en imágenes clave, bajo contraste de colores en botones, formularios sin etiquetas).

# Fase 3: Dimensión de Gobernanza y Ética (G)

Revisa cómo trata la empresa a sus usuarios y sus datos:

## Transparencia. ¿Es fácil rechazar las cookies no esenciales o utilizan "patrones oscuros" (Dark Patterns) para forzar al usuario a aceptarlas?

## Datos innecesarios. ¿Pide la web datos personales excesivos en su formulario de contacto o registro?

# Fase 4: Propuesta de Refactorización (Green Coding)

Como desarrollador/a, no basta con encontrar los fallos; debes proponer soluciones. Redacta una propuesta de mejora técnica detallando:

## Optimización de activos. 

- ¿Qué formatos usarías para sustituir las imágenes actuales (ej. WebP, AVIF)?
- ¿Implementarías Lazy Loading?

## Reducción de peticiones.
  
- ¿Qué librerías o scripts externos eliminarías o aplazarías para mejorar la eficiencia del código y reducir el procesamiento en el dispositivo del cliente?

## Reflexión sobre la Paradoja de Jevons.
  
- Si optimizamos la web y la carga mucho más rápido, podríamos atraer a muchos más usuarios diarios. ¿Cómo evitarías que este éxito anule el ahorro energético conseguido?
