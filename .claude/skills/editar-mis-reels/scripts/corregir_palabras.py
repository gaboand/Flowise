# Uso: python3 corregir_palabras.py trabajo/palabras.json '[[tramo, "palabras de whisper", "palabras correctas"], ...]'
# Reemplaza un rango de palabras de un tramo, repartiendo el tiempo por cantidad de letras.
import json, sys
f = sys.argv[1]; P = json.load(open(f))
fixes = json.loads(sys.argv[2])  # [[tramo, "viejas palabras", "nuevas palabras"], ...]
for tramo, viejo, nuevo in fixes:
    idx = [i for i, w in enumerate(P) if w['tramo'] == tramo]
    toks = [P[i]['p'] for i in idx]; v = viejo.split()
    k = next(k for k in range(len(toks)) if toks[k:k+len(v)] == v)
    sl = idx[k:k+len(v)]; a, b = P[sl[0]]['a'], P[sl[-1]]['b']
    nw = nuevo.split(); tot = sum(len(w) for w in nw); t = a; new = []
    for w in nw:
        d = (b - a) * len(w) / tot
        new.append({'p': w, 'a': round(t, 3), 'b': round(t + d, 3), 'tramo': tramo}); t += d
    P[sl[0]:sl[-1]+1] = new
json.dump(P, open(f, 'w'), ensure_ascii=False, indent=0)
print(' '.join(w['p'] for w in P))
