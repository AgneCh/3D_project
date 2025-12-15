from pathlib import Path
import add

# Išvesties aplankas + atstatymas
isvesties_aplankas = Path(__file__).parent
add.clear()

# Parametrai
STORIO_MASTELIS = 1.15

# Aukščiai
AUKSTIS_STIKLO = 18.0   # stiklo dalies aukštis
AUKSTIS_DANGTELIO = 4.0  # dangtelio aukštis

# Stiklo (nupjauto kūgio) spinduliai
SPIND_STIKLO_APACIA = 3.2   # ties A1 (prie pagrindo)
SPIND_STIKLO_VIRSUS = 1.6   # ties A2 (prie dangtelio)

# Dangtelio (nupjauto kūgio) spinduliai
SPIND_DANGTELIO_APACIA = SPIND_STIKLO_VIRSUS  # sutampa su stiklo viršumi
SPIND_DANGTELIO_VIRSUS = 1.1                  # maža viršutinė anga

# --- Metalinis pagrindas ---
AUKSTIS_PAGRINDO = 10.0
SPIND_PADAS = 4.0        # apatinis spindulys (padas)
SPIND_LIEMUO = 1.7       # siauriausia vieta (liemuo)
LIEMENS_POZICIJA = 0.55  # liemens vieta pagal aukštį (0..1)

# Siūlė pagrindo viršuje (kur jungiasi su stiklu)
SPIND_SIULE = SPIND_STIKLO_APACIA

# Tinklelio rezoliucija
K_APLINK = 64   # segmentų kiekis aplink
T_TINKLAS = 64  # segmentų kiekis pagal aukštį

# Spalvos
SPALVA_PAGRINDO = [80, 80, 80]
SPALVA_STIKLO = [185, 230, 255]
SPALVA_DANGT = [60, 60, 60]
SPALVA_LAVOS = [230, 60, 40]

# Sandarinimo žiedas (išorinis „apvadas“ stiklo/dangtelio sandūroje)
SPIND_ZIEDO = SPIND_DANGTELIO_APACIA * STORIO_MASTELIS


# Ašies taškai (lempa stovi ant Z ašies)
A0 = [0.0, 0.0, 0.0]
A1 = [0.0, 0.0, AUKSTIS_PAGRINDO]
A2 = [0.0, 0.0, AUKSTIS_PAGRINDO + AUKSTIS_STIKLO]
A3 = [0.0, 0.0, AUKSTIS_PAGRINDO + AUKSTIS_STIKLO + AUKSTIS_DANGTELIO]

# ==================================
# Profiliai (spin3D funkcijoms)
# Kiekviena grąžina [spindulys, z]
# ==================================
def S_pagrindas(t: float):
    """
    - apatinė dalis: nuo pado iki liemens
    - viršutinė dalis: nuo liemens iki siūlės
    """
    z = t * AUKSTIS_PAGRINDO

    if t <= LIEMENS_POZICIJA:
        # APATINĖ DALIS: SPIND_PADAS -> SPIND_LIEMUO
        u = t / LIEMENS_POZICIJA
        r = SPIND_PADAS + (SPIND_LIEMUO - SPIND_PADAS) * u
    else:
        # VIRŠUTINĖ DALIS: SPIND_LIEMUO -> SPIND_SIULE
        u = (t - LIEMENS_POZICIJA) / (1.0 - LIEMENS_POZICIJA)
        r = SPIND_LIEMUO + (SPIND_SIULE - SPIND_LIEMUO) * u

    return [r * STORIO_MASTELIS, z]

def S_stiklas(t: float):
    z = t * AUKSTIS_STIKLO
    r = SPIND_STIKLO_APACIA + (SPIND_STIKLO_VIRSUS - SPIND_STIKLO_APACIA) * t
    return [r * STORIO_MASTELIS, z]

def S_dangtelis(t: float):
    z = t * AUKSTIS_DANGTELIO
    r = SPIND_DANGTELIO_APACIA + (SPIND_DANGTELIO_VIRSUS - SPIND_DANGTELIO_APACIA) * t
    return [r * STORIO_MASTELIS, z]


### Objekto kūrimas ###
# --- PAGRINDAS ---
add.spin3D(A0, A1, S_pagrindas, 0.0, 1.0, T_TINKLAS, K_APLINK, SPALVA_PAGRINDO)

# Uždaryti pagrindo apačią (diskas ties A0)
add.circle(A0, A1, SPIND_PADAS * STORIO_MASTELIS, K_APLINK, SPALVA_PAGRINDO)

add.off(str(isvesties_aplankas / "lamp_base.off"))

# --- STIKLAS ---
add.spin3D(A1, A2, S_stiklas, 0.0, 1.0, T_TINKLAS, K_APLINK, SPALVA_STIKLO)
add.off(str(isvesties_aplankas / "lamp_glass.off"))

# --- DANGTELIS + ŽIEDAS ---
add.spin3D(A2, A3, S_dangtelis, 0.0, 1.0, T_TINKLAS // 2, K_APLINK, SPALVA_DANGT)

# Uždaryti dangtelio viršų (diskas ties A3)
add.circle(A3, A2, SPIND_DANGTELIO_VIRSUS * STORIO_MASTELIS, K_APLINK, SPALVA_DANGT)

# Žiedas stiklo/dangtelio sandūroje
add.cylinder2(
    [0.0, 0.0, AUKSTIS_PAGRINDO + AUKSTIS_STIKLO - 0.12],
    [0.0, 0.0, AUKSTIS_PAGRINDO + AUKSTIS_STIKLO + 0.12],
    SPIND_ZIEDO,
    K_APLINK,
    SPALVA_DANGT,
)

add.off(str(isvesties_aplankas / "lamp_cap.off"))


# Lava
def stiklo_spindulys_ties_z(z: float) -> float:
    """Stiklo spindulys ties konkrečiu z (modelio viduje)."""
    t = (z - AUKSTIS_PAGRINDO) / AUKSTIS_STIKLO
    t = max(0.0, min(1.0, t))
    r = SPIND_STIKLO_APACIA + (SPIND_STIKLO_VIRSUS - SPIND_STIKLO_APACIA) * t
    return r * STORIO_MASTELIS

def saugi_sfera(centras, r, k, rgb, paklaida=0.12):
    """Prideda sferą tik jei ji telpa stiklo viduje (neprasikiša pro sienelę)."""
    x, y, z = centras
    d = (x * x + y * y) ** 0.5  # atstumas nuo ašies
    rmax = stiklo_spindulys_ties_z(z) - d - paklaida
    if rmax < 0.05:
        return
    add.sphere([x, y, z], min(r, rmax), k, rgb)

# --- Apatinis lavos blob ---
saugi_sfera([0.0, 0.0, AUKSTIS_PAGRINDO + 0.6], 3.35, 30, SPALVA_LAVOS)
saugi_sfera([0.0, 0.0, AUKSTIS_PAGRINDO + 1.3], 3.20, 28, SPALVA_LAVOS)
saugi_sfera([0.0, 0.0, AUKSTIS_PAGRINDO + 2.0], 3.00, 26, SPALVA_LAVOS)

# --- Beveik atsiskiriantis burbulas ---
saugi_sfera([0.0, 0.0, AUKSTIS_PAGRINDO + 3.05], 1.00, 20, SPALVA_LAVOS)
saugi_sfera([0.0, 0.0, AUKSTIS_PAGRINDO + 3.70], 0.55, 18, SPALVA_LAVOS)
saugi_sfera([0.0, 0.0, AUKSTIS_PAGRINDO + 6.0], 1.55, 22, SPALVA_LAVOS)

# --- Plūduriuojantys lavos gabalėliai ---
for (x, y, z), r in zip(
    [(0.6, 0.2, AUKSTIS_PAGRINDO + 4.8),
     (-0.5, -0.2, AUKSTIS_PAGRINDO + 10.0),
     (0.1, 0.4, AUKSTIS_PAGRINDO + 14.0)],
    [1.1, 0.9, 0.7],
):
    saugi_sfera([x, y, z], r, 18, SPALVA_LAVOS)

add.off(str(isvesties_aplankas / "lamp_lava.off"))
