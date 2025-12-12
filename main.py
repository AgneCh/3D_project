from pathlib import Path
import add

# reset
add.clear()

# ---------- parameters ----------
THICKNESS_SCALE = 1.15
H_GLASS = 18.0
H_CAP   = 4.0

# glass frustum radii
R_GLASS_BOTTOM = 3.2   # at A1 (near base)
R_GLASS_TOP    = 1.6   # at A2 (near cap)

# cap frustum radii
R_CAP_BOTTOM = R_GLASS_TOP   # slightly wider than glass top
R_CAP_TOP    = 1.1                 # small top opening

# --- metal base ---
H_BASE = 10.0
R_FOOT = 4.0     # bottom radius
R_WAIST = 1.7     # narrow waist radius
WAIST_POS = 0.55   # waist position along height (0..1)

# seam at the top of the base
R_SEAM = R_GLASS_BOTTOM

# resolution
K_AROUND = 64
GRID_T   = 64

# colors
CLR_BASE  = [80, 80, 80]
CLR_GLASS = [185, 230, 255]
CLR_CAP   = [60, 60, 60]
CLR_LAVA  = [230, 60, 40]

# sealing ring radius (outer-looking rim at glass/cap junction)
R_RING = R_CAP_BOTTOM * THICKNESS_SCALE

# axis points (lamp upright on Z)
A0 = [0.0, 0.0, 0.0]
A1 = [0.0, 0.0, H_BASE]
A2 = [0.0, 0.0, H_BASE + H_GLASS]
A3 = [0.0, 0.0, H_BASE + H_GLASS + H_CAP]

# ---------- profiles ----------
def ease_out(u: float) -> float:
    """0..1 -> 0..1, smooth near 0, stronger near 1."""
    u = max(0.0, min(1.0, u))
    return 1.0 - (1.0 - u) ** 2

def S_base_black(t: float):
    """
    - lower part: smooth flare (curved)
    - upper part: nearly straight cone
    """
    z = t * H_BASE

    if t <= WAIST_POS:
        # LOWER PART (curved flare): R_FOOT -> R_WAIST
        u = t / WAIST_POS
        r = R_FOOT + (R_WAIST - R_FOOT) * u
    else:
        # UPPER PART (straight): R_WAIST -> R_SEAM
        u = (t - WAIST_POS) / (1.0 - WAIST_POS)
        r = R_WAIST + (R_SEAM - R_WAIST) * u

    return [r * THICKNESS_SCALE, z]

def S_glass(t: float):
    z = t * H_GLASS
    r = R_GLASS_BOTTOM + (R_GLASS_TOP - R_GLASS_BOTTOM) * t
    return [r * THICKNESS_SCALE, z]

def S_cap(t: float):
    z = t * H_CAP
    r = R_CAP_BOTTOM + (R_CAP_TOP - R_CAP_BOTTOM) * t
    return [r * THICKNESS_SCALE, z]

# ---------- build ----------

# metal base
add.spin3D(A0, A1, S_base_black, 0.0, 1.0, GRID_T, K_AROUND, CLR_BASE)

# glass bottle
add.spin3D(A1, A2, S_glass, 0.0, 1.0, GRID_T, K_AROUND, CLR_GLASS)

# cap (frustum)
add.spin3D(A2, A3, S_cap, 0.0, 1.0, GRID_T // 2, K_AROUND, CLR_CAP)

# sealing ring at glass/cap junction
add.cylinder2([0.0, 0.0, H_BASE + H_GLASS - 0.12],
              [0.0, 0.0, H_BASE + H_GLASS + 0.12],
              R_RING, K_AROUND, CLR_CAP)

# lava blobs (inside glass)
for (x, y, z), r in zip(
    [(0.6, 0.2, H_BASE + 4.0),
     (-0.5, -0.2, H_BASE + 10.0),
     (0.1, 0.4, H_BASE + 14.0)],
    [1.2, 0.9, 0.7],
):
    add.sphere([x, y, z], r, 18, CLR_LAVA)

# ---------- export ----------
out_path = Path(__file__).with_name("lava_lamp.off")
add.off(str(out_path))
print(f"Saved: {out_path}")
