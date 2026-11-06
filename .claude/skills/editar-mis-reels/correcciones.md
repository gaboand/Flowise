# Correcciones

Claude lee este archivo antes de cada edición. Claude suma una entrada por cada corrección.

Formato:

```markdown
## AAAA-MM-DD · <reel>
- Dijo: "<la frase del usuario>"
- Por qué: <qué problema causaba>
- Regla: <qué hacer de ahora en más>
```

Las entradas van debajo de esta línea, de la más nueva a la más vieja.

---

## 2026-11-06 · edicion-mora (reel-v1, encontradas en la revisión propia)
- Problema: la webcam graba muy bajo (media −44 dB). El detector de silencios tiene un piso fijo y puede cortar voz.
- Regla: si `volumedetect` da media < −35 dB, crear `trabajo/fuente.mp4` con `-c:v copy -af volume=<dB>` (pico ≈ −5 dB) y cortar desde ahí.

- Problema: whisper entendió "moda", "la cultura", "felicidades de taza", "cartel".
- Regla: comparar cada tramo con la transcripción del audio entero y con lo que dice el usuario; corregir rangos con `scripts/corregir_palabras.py`. Términos del rubro: mora, elasticidades de tasa, cartera, costos.

- Problema: el azul de marca #1E6FD9 como color de palabra no se lee sobre la remera negra.
- Regla: palabras destacadas en #4FB0FF (azul claro del logo). #1E6FD9 queda para cajas de títulos.

- Problema: con el zoom de corte (1,12) el subtítulo quedaba sobre el mentón.
- Regla: con grabación de webcam recortada a 9:16, `base` 1260; títulos grandes en y≈1420-1770, sobre la remera.

- Problema: subtitulos.py dejaba `\r}` visible, no marcaba "mora?" y dejaba palabras sueltas de 0,04 s ("¿y", "así").
- Regla: corregido en el script.
