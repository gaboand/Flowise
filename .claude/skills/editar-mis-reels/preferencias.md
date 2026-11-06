# Mis preferencias de edición

Claude lee este archivo antes de cada edición. Claude no pregunta lo que este archivo responde.
Cuando des una indicación para próximos reels, Claude la suma acá, con la fecha y tu frase.

No hace falta completarlo a mano. Pedile a Claude: "configurá mi skill de edición".

## Quién sos

- Tema de tus reels: gestión del riesgo crediticio (mora, ingresos, tasas, cartera). Objetivo: captar clientes B2B para la consultora. Tono profesional y sobrio; cierre con llamado a contactar.
- Idioma de tus reels: español rioplatense (voseo: "podés", "tenés").
- Cómo grabás (celular, cámara, teleprompter, improvisado): webcam de compu, horizontal 1280×720 a 60 fps, sentado a cámara. Guion de memoria (no lo lee).
- Tres videos que te gustaría igualar, con su link o archivo: ninguno todavía (si pasa uno, medirlo con references/medir-referencia.md)

## Formatos

Definí de 1 a 4 formatos. Cada formato tiene su estructura.

| Formato | Cuándo se usa | Estructura |
|---|---|---|
| concepto-pregunta | explicar un concepto de riesgo crediticio a un potencial cliente | gancho con 1-2 preguntas provocadoras a cámara (texto grande con la pregunta), cuerpo: la idea clave con 1 título en pantalla, cierre a cámara con llamado a contactar + logo y contacto abajo. Duración ~20-40 s |

## Cortes

- Silencio más corto que se corta, en segundos (`--min`, sugerido 0,25): 0,25 (ritmo picado)
- Aire a cada lado del corte, en segundos (`--aire`, sugerido 0,10): 0,10
- Muletillas que se sacan: "eh", "em", "mmm", "bueno" y "este" (cuando arrancan frase)
- Muletillas o pausas que se dejan, porque son parte de tu estilo: "o sea", "digamos" y "así que" quedan

## Encuadre

- Tamaño y cuadros por segundo (sugerido 1080 × 1920, a 30): 1080 × 1920 a 30. La grabación es horizontal: recortar 9:16 centrado en la cara.
- Zoom en los planos a cámara (ninguno, lento, cortes de zoom): cortes de zoom leves (1,0 ↔ 1,12) para disimular los saltos de corte (sugerido, por ritmo picado)
- Cómo es el plano de cierre: sigue a cámara diciendo el llamado ("podés llamarnos…") y aparece el logo con teléfono/web en la parte baja. Logo y datos de contacto: [PEDIR AL USUARIO la primera vez y guardar acá]

## Subtítulos

Los valores exactos van en `estilo.json`.

- Lleva subtítulos (sí o no): sí
- Estilo en palabras, o un video para medir: dinámico estilo TikTok, grande, blanco con borde oscuro y negrita, debajo del mentón sin tapar la cara.
- Palabras por subtítulo (sugerido de 1 a 3): 1 a 2
- Mayúsculas, minúsculas o normal: minúscula (sugerido)
- Cómo se marca la palabra del gancho: color de marca en 1-2 palabras clave por frase (mora, ingresos, riesgo, costos, cartera…). Color de marca: azul #1E6FD9.

## Imagen en pantalla

- Qué lleva cada formato (capturas, clips, animaciones, memes): textos/títulos grandes con frases clave en momentos puntuales; logo y contacto de la consultora en el cierre. Sin memes.
- Cuánto se ve tu cara, en proporción del reel: casi todo el reel (es a cámara); los títulos van encima, sin taparla
- Colores y tipografías de tus animaciones: azul #1E6FD9 + blanco, tipografía sans negrita (sugerido)
- Cosas que nunca querés ver: memes, emojis, efectos de sonido, transiciones llamativas (sugerido, tono B2B)

## Audio

- Volumen final (sugerido −14 LUFS): −14 LUFS. La webcam graba bajo (media −44 dB): siempre nivelar.
- Música (sí o no, y cuál): no. Solo voz.
- Efectos de sonido (ninguno, pocos, muchos): ninguno (sugerido, por tono B2B)

## Autonomía

- Qué puede hacer Claude sin preguntar: todo el armado (cortes, subtítulos, títulos, cierre) y mostrar el v1
- Qué tiene que consultar siempre: usar material de terceros; datos de contacto o cifras que aparezcan en pantalla
- Cuándo querés ver la lista de planos antes del armado: nunca; directo al v1

## Entrega

- Dónde está el material de cada reel: lo adjunta en el chat de Claude Code (en la nube, /root/.claude/uploads/…)
- Dónde va el reel terminado: se le envía como archivo en el chat
- Cómo marcás los cambios (chat, comentarios en una app, otra forma): por chat, con el segundo del video
- Cuánto detalle querés en el mensaje de entrega: corto: qué hice y qué revisar (sugerido)
