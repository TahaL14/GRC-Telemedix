#!/usr/bin/env python3
"""Contrôle de cohérence du dossier : références croisées risques / mesures / actions."""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
errors = []


def rows(path, heading_prefix=None):
    """Lignes de tableaux Markdown d'un fichier, sous forme de listes de cellules."""
    out = []
    for line in (ROOT / path).read_text(encoding="utf-8").splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*-+", line):
            out.append([c.strip() for c in line.strip().strip("|").split("|")])
    return out


def ids(text, prefix):
    return set(re.findall(rf"\b{prefix}\d{{2}}\b", text))


MATRIX = {
    ("G4", "V1"): "Moyen", ("G4", "V2"): "Élevé", ("G4", "V3"): "Élevé", ("G4", "V4"): "Élevé",
    ("G3", "V1"): "Moyen", ("G3", "V2"): "Moyen", ("G3", "V3"): "Élevé", ("G3", "V4"): "Élevé",
    ("G2", "V1"): "Faible", ("G2", "V2"): "Faible", ("G2", "V3"): "Moyen", ("G2", "V4"): "Moyen",
}

# --- Plan d'actions
plan = {}
for r in rows("06-plan-actions.md"):
    if re.fullmatch(r"A\d{2}", r[0]) and len(r) >= 9:
        impact, effort = int(r[3]), int(r[4])
        if impact >= 3 and effort <= 2:
            q = "Gain rapide"
        elif impact >= 3:
            q = "Projet structurant"
        elif effort <= 2:
            q = "Complément"
        else:
            q = "À arbitrer"
        if q != r[5]:
            errors.append(f"{r[0]} : quadrant {r[5]} attendu {q}")
        plan[r[0]] = {"risks": ids(r[2], "R"), "quadrant": q, "month": int(r[6][1:])}
print(f"Actions : {len(plan)}")
expected_actions = {f"A{i:02d}" for i in range(1, 29)}
if set(plan) != expected_actions:
    errors.append(f"Actions manquantes ou en trop : {set(plan) ^ expected_actions}")

text06 = (ROOT / "06-plan-actions.md").read_text(encoding="utf-8")
for r in rows("06-plan-actions.md"):
    if r[0] in ("Gain rapide", "Projet structurant", "Complément", "À arbitrer") and r[1].isdigit():
        real = {a for a, v in plan.items() if v["quadrant"] == r[0]}
        if int(r[1]) != len(real) or ids(r[2], "A") != real:
            errors.append(f"Synthèse quadrant {r[0]} incohérente : {sorted(real)}")
    if r[0].startswith(("1.", "2.", "3.")) and len(r) == 4:
        lo, hi = [int(x) for x in re.findall(r"M(\d+)", r[1])]
        for a in ids(r[3], "A"):
            if not (lo <= plan[a]["month"] <= hi):
                errors.append(f"{a} : échéance M{plan[a]['month']} hors vague {r[1]}")
waves = set()
for r in rows("06-plan-actions.md"):
    if r[0].startswith(("1.", "2.", "3.")) and len(r) == 4:
        waves |= ids(r[3], "A")
if waves != expected_actions:
    errors.append(f"Feuille de route incomplète : {expected_actions ^ waves}")

# --- EBIOS
risks_initial, risks_residual, treat = {}, {}, {}
pp = []
for r in rows("02-ebios-rm.md"):
    if re.fullmatch(r"R\d{2}", r[0]):
        if len(r) == 5 and r[2].startswith("G"):
            risks_initial[r[0]] = (r[2], r[3], r[4])
        elif len(r) == 6 and r[3].startswith("G"):
            risks_residual[r[0]] = (r[3], r[4], r[5])
            treat[r[0]] = ids(r[2], "A")
    if re.fullmatch(r"PP\d+", r[0]) and len(r) == 8:
        d, p, m, c = (int(x) for x in r[2:6])
        val = d * p / (m * c)
        shown = float(r[6].replace(",", "."))
        zone = "Danger" if val >= 2.5 else "Contrôle" if val >= 1.0 else "Veille"
        if abs(round(val + 1e-9, 2) - shown) > 0.006 or zone != r[7]:
            errors.append(f"{r[0]} : calcul {val:.3f} / {zone}, affiché {r[6]} / {r[7]}")
        pp.append(r[0])
print(f"Risques : {len(risks_initial)} ; parties prenantes : {len(pp)}")
for name, table in (("initial", risks_initial), ("résiduel", risks_residual)):
    for rid, (g, v, lvl) in table.items():
        if MATRIX[(g, v)] != lvl:
            errors.append(f"{rid} {name} : {g}/{v} donne {MATRIX[(g, v)]}, affiché {lvl}")
if set(risks_initial) != set(risks_residual) or len(risks_initial) != 10:
    errors.append("Tables de risques incomplètes")

# cartographies
text02 = (ROOT / "02-ebios-rm.md").read_text(encoding="utf-8")
for title, table in (("### Cartographie initiale", risks_initial), ("### Cartographie résiduelle", risks_residual)):
    block = text02.split(title)[1].split("\n\n")[1]
    for line in block.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        m = re.match(r"\*\*(G\d)\*\*", cells[0])
        if m:
            for i, cell in enumerate(cells[1:], start=1):
                for rid in ids(cell, "R"):
                    if table[rid][:2] != (m.group(1), f"V{i}"):
                        errors.append(f"{title} : {rid} mal placé")
            placed = ids(line, "R")
            should = {r for r, v in table.items() if v[0] == m.group(1)}
            if placed != should:
                errors.append(f"{title} ligne {m.group(1)} : {placed} attendu {should}")

# cohérence traitement <-> plan
by_action = defaultdict(set)
for rid, acts in treat.items():
    for a in acts:
        by_action[a].add(rid)
        if a not in plan:
            errors.append(f"{rid} : action {a} inconnue")
for a, v in plan.items():
    if v["risks"] != by_action.get(a, set()):
        errors.append(f"{a} : risques du plan {sorted(v['risks'])} ≠ traitement EBIOS {sorted(by_action.get(a, set()))}")

# --- Déclaration d'applicabilité
soa = []
for r in rows("04-dda-iso27001.md"):
    if re.fullmatch(r"[5-8]\.\d{1,2}", r[0]) and len(r) == 6:
        soa.append(r)
        for rid in ids(r[3], "R"):
            if rid not in risks_initial:
                errors.append(f"DdA {r[0]} : risque {rid} inconnu")
        for a in ids(r[5], "A"):
            if a not in plan:
                errors.append(f"DdA {r[0]} : action {a} inconnue")
        if r[2] == "Non" and r[4] != "Exclu":
            errors.append(f"DdA {r[0]} : exclusion incohérente")
        if r[4] in ("Partiel", "À faire") and not ids(r[5], "A"):
            errors.append(f"DdA {r[0]} : état {r[4]} sans action")
        if r[4] == "En place" and ids(r[5], "A"):
            errors.append(f"DdA {r[0]} : en place mais action listée")
expected = [f"{t}.{i}" for t, n in ((5, 37), (6, 8), (7, 14), (8, 34)) for i in range(1, n + 1)]
if [r[0] for r in soa] != expected:
    errors.append("DdA : liste des 93 mesures incomplète ou désordonnée")
print(f"Mesures DdA : {len(soa)}")
soa_actions = set().union(*(ids(r[5], "A") for r in soa))
missing = expected_actions - soa_actions
if missing:
    errors.append(f"Actions absentes de la DdA : {sorted(missing)}")
counts = defaultdict(Counter)
for r in soa:
    counts[r[0][0]][r[4]] += 1
    counts[r[0][0]]["total"] += 1
    counts["T"][r[4]] += 1
    counts["T"]["total"] += 1
print("Synthèse DdA attendue (mesures, retenues, exclues, en place, partiel, à faire) :")
for k in ("5", "6", "7", "8", "T"):
    c = counts[k]
    calc = [c["total"], c["total"] - c["Exclu"], c["Exclu"], c["En place"], c["Partiel"], c["À faire"]]
    print(f"  {k} : {calc}")
    for r in rows("04-dda-iso27001.md"):
        label = r[0].replace("*", "")
        if (label.startswith(k + ".") and "Mesures" in label) or (k == "T" and label == "Total"):
            shown = [int(x.replace("*", "")) for x in r[1:7]]
            if shown != calc:
                errors.append(f"DdA synthèse thème {k} : affiché {shown}, calculé {calc}")

# --- Références dans les autres dossiers
for f in ("03-aipd-registre.md", "05-ecarts-hds-nis2.md", "01-cadrage.md", "07-pssi.md", "README.md"):
    p = ROOT / f
    if not p.exists():
        continue
    t = p.read_text(encoding="utf-8")
    for a in ids(t, "A"):
        if a not in plan:
            errors.append(f"{f} : action {a} inconnue")
    for rid in ids(t, "R"):
        if rid not in risks_initial:
            errors.append(f"{f} : risque {rid} inconnu")

# écarts majeurs annoncés dans le dossier 5
t5 = (ROOT / "05-ecarts-hds-nis2.md").read_text(encoding="utf-8")
hds2 = t5.split("### Volet 2")[1].split("**Bilan HDS.**")[0].count("**Majeur**")
nis = t5.split("## 5.4 Matrice")[1].split("**Bilan NIS2.**")[0].count("**Majeur**")
print(f"Écarts majeurs : HDS volet 2 = {hds2}, NIS2 = {nis}")
if f"{hds2} écarts majeurs" not in t5.split("**Bilan HDS.**")[1][:40]:
    errors.append("Bilan HDS incohérent")
if f"{nis} écarts majeurs" not in t5.split("**Bilan NIS2.**")[1][:40]:
    errors.append("Bilan NIS2 incohérent")

print()
if errors:
    print(f"{len(errors)} incohérence(s) :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("Aucune incohérence détectée.")
