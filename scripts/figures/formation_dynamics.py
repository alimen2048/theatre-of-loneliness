"""Generate the Formation Staircase figure (SVG).

Panel 1: an impersonal rising stage schedule c_t under rho*R = 0 (respecting A8
and cost-and-the-veil section 9): a player whose v_0 clears the early rungs climbs,
a player with smaller v_0 is overtaken (overshoot) and stalls, and a painless safe
room (c_t = 0) stays flat.
Panel 2: matched initial v_0 > c at unified parameters (eta = 0.12, gamma = 0.10):
dark stakes with no grade (rho*R = 0) grow v_t, while permanent grading keeps watched
compliance at 100% as v_t decays smoothly below c (staying > 0).
Illustrative curves from the note's candidate equations, not empirical data.
"""
import math

W, H = 1600, 900
BG = "#0d0e10"
PANEL = "#131519"
EDGE = "#2a2a30"
TXT = "#f3f4f6"
SUB = "#c9cdd4"
DIM = "#9ca3af"
FAINT = "#71717a"
GOLD = "#eab308"
GOLD_T = "#fde047"
BLUE = "#60a5fa"
BLUE_T = "#93c5fd"
RED = "#f87171"
RED_T = "#fca5a5"
GREEN = "#34d399"
GREEN_T = "#6ee7b7"
GREY = "#a1a1aa"

SERIF = "Georgia, 'Times New Roman', serif"
SANS = "'Helvetica Neue', Helvetica, Arial, sans-serif"

out = []


def add(s):
    out.append(s)


def text(x, y, s, size=17, fill=SUB, family=SANS, anchor="start", weight="normal",
         italic=False, rotate=None):
    style = ' font-style="italic"' if italic else ""
    tr = f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    add(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}" '
        f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{style}{tr}>{s}</text>')


def line(x1, y1, x2, y2, stroke, w=1.5, dash=None, opacity=1.0):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" '
        f'stroke-width="{w}"{d} opacity="{opacity}"/>')


def poly(pts, fill, op, stroke="none", sw=0.0):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    add(f'<polygon points="{p}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" '
        f'stroke-width="{sw}"/>')


def path(pts, stroke, w=3.0, dash=None, fill="none", op=1.0):
    d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    da = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<path d="{d}" stroke="{stroke}" stroke-width="{w}" fill="{fill}" '
        f'fill-opacity="{op}"{da} stroke-linejoin="round"/>')


def build():
    """Return {filename: svg_text}."""
    out.clear()
    add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
    add(f'<rect width="{W}" height="{H}" fill="{BG}"/>')

    eta = 0.12
    gamma = 0.10

    # ---------------------------------------------------------------- header
    text(70, 64, "How Values Grow and Die", 36, TXT, SERIF)
    text(70, 100, "Left: an impersonal cost ramp grows high-seed players and overshoots low-seed ones.  "
         "Right: grading keeps watched compliance at 100% while v_t decays.", 19, DIM)

    # ---------------------------------------------------------------- panel 1: impersonal ramp
    ax0, ax1, ay0, ay1 = 130, 720, 190, 750
    T1 = 20
    VMAX1 = 5.6

    def A(t, val):
        px = ax0 + (t / T1) * (ax1 - ax0)
        py = ay1 - (val / VMAX1) * (ay1 - ay0)
        assert ay0 <= py <= ay1 + 0.1, f"Panel 1 y out of bounds: val={val}, py={py}"
        return px, py

    add(f'<rect x="{ax0}" y="{ay0}" width="{ax1-ax0}" height="{ay1-ay0}" fill="{PANEL}" '
        f'stroke="{EDGE}" stroke-width="1.5"/>')
    text(ax0, 160, "1.  IMPERSONAL RAMP vs. SAFE ROOM  (\u03c1R = 0)", 18, TXT, weight="bold")

    # Fixed population-level stage ramp c_t (does NOT read individual v_t)
    c_ramp = [0.36 + 0.095 * t + 0.0035 * (t ** 2) for t in range(T1)]

    # Player 1: v0 = 1.0 (clears ramp throughout: c_t < v_t)
    v_climb = [1.0]
    for t in range(T1):
        vt = v_climb[-1]
        ct = c_ramp[t]
        assert ct < vt, f"Player 1 did not clear ramp at t={t}: ct={ct}, vt={vt}"
        v_climb.append(vt + eta * ct)

    # Player 2: v0 = 0.62 (climbs early rungs, then impersonal ramp overtakes v_t -> stalls)
    v_over = [0.62]
    cross_t = None
    for t in range(T1):
        vt = v_over[-1]
        ct = c_ramp[t]
        if 0 < ct < vt:
            v_over.append(vt + eta * ct)
        else:
            if cross_t is None:
                cross_t = t
            v_over.append(vt)
    assert cross_t is not None and 3 <= cross_t <= 10, f"Expected mid-run overshoot, got cross_t={cross_t}"

    # Safe room: c_t = 0 -> flat at v0 = 1.0
    v_safe = [1.0 for _ in range(T1 + 1)]

    # Shaded growth band (0 < c < v_t) for Player 1
    band_pts = [A(t, v_climb[t]) for t in range(T1 + 1)] + [A(T1, 0), A(0, 0)]
    poly(band_pts, GOLD, 0.09)

    # Grid lines & ticks
    for yv in [1, 2, 3, 4, 5]:
        _, py = A(0, yv)
        line(ax0, py, ax1, py, EDGE, 1.0, opacity=0.6)
        text(ax0 - 12, py + 6, str(yv), 16, DIM, anchor="end")
    _, py0 = A(0, 0)
    text(ax0 - 12, py0 + 6, "0", 16, DIM, anchor="end")

    for xt in [0, 5, 10, 15, 20]:
        px, _ = A(xt, 0)
        line(px, ay1, px, ay1 + 7, DIM, 1.2)
        text(px, ay1 + 28, str(xt), 16, DIM, anchor="middle")

    # Impersonal stage ramp steps c_t
    step_pts = []
    for t in range(T1):
        step_pts.append(A(t, c_ramp[t]))
        step_pts.append(A(t + 1, c_ramp[t]))
    path(step_pts, GREY, 2.0, dash="5,4", op=0.85)

    # Trajectories
    path([A(t, v_safe[t]) for t in range(T1 + 1)], BLUE, 2.8)
    path([A(t, v_over[t]) for t in range(T1 + 1)], GREEN, 2.8, dash="7,4")
    path([A(t, v_climb[t]) for t in range(T1 + 1)], GOLD_T, 3.6)

    if cross_t is not None:
        ox, oy = A(cross_t, v_over[cross_t])
        add(f'<circle cx="{ox:.1f}" cy="{oy:.1f}" r="5.0" fill="{GREEN_T}"/>')

    # Labels inside panel 1 (all verified strictly inside [ay0+28, ay1-16])
    _, gy = A(14.0, v_climb[14])
    text(ax0 + 18, gy - 26, "Ramp stays inside band (0 < c_t < v_t)", 16, GOLD_T, weight="bold")
    text(ax0 + 18, gy - 5, "Seed v\u2080 = 1: v_t compounds on the ramp", 15, SUB)

    # Below the ramp at the right edge, clear of the grey steps
    text(ax1 - 10, 578, "impersonal stage ramp c_t", 15, GREY, SERIF, anchor="end", italic=True)

    _, oy_l = A(10.0, v_over[-1])
    text(470, oy_l - 12, "Seed v\u2080 = 0.62: overshot, stalls", 15, GREEN_T, weight="bold")

    bx, by = A(10.0, 1.0)
    text(bx, by + 24, "Safe room (c_t = 0): flat", 15, BLUE_T, weight="bold")

    text((ax0 + ax1) / 2, ay1 + 76, "Rounds of unmonitored practice,  t", 20, SUB, anchor="middle")
    text(62, (ay0 + ay1) / 2, "Held commitment  v_t", 20, SUB, anchor="middle", rotate=-90)

    # ---------------------------------------------------------------- panel 2: no grade vs permanent grade
    bx0, bx1, by0, by1 = 880, 1510, 190, 750
    T2 = 22
    T_OFF = 15
    VMAX2 = 4.8

    def B(t, val):
        px = bx0 + (t / T2) * (bx1 - bx0)
        py = by1 - (val / VMAX2) * (by1 - by0)
        assert by0 <= py <= by1 + 0.1, f"Panel 2 y out of bounds: val={val}, py={py}"
        return px, py

    add(f'<rect x="{bx0}" y="{by0}" width="{bx1-bx0}" height="{by1-by0}" fill="{PANEL}" '
        f'stroke="{EDGE}" stroke-width="1.5"/>')
    text(bx0, 160, "2.  DARK STAKES vs. PERMANENT GRADE", 18, TXT, weight="bold")

    # Shade dark deployment phase after T_OFF
    x_off, _ = B(T_OFF, 0)
    poly([(x_off, by0), (bx1, by0), (bx1, by1), (x_off, by1)], BLUE, 0.06)
    line(x_off, by0, x_off, by1, SUB, 1.5, dash="6,5", opacity=0.8)
    text(x_off - 10, by0 + 26, "Training window", 15, DIM, anchor="end")
    text(x_off + 10, by0 + 26, "Dark deployment (\u03c1 = 0)", 15, BLUE_T, weight="bold")

    c_bar = 1.0
    _, y_cbar = B(0, c_bar)
    line(bx0, y_cbar, bx1, y_cbar, GREY, 1.5, dash="4,4", opacity=0.85)
    text(bx1 - 10, y_cbar - 9, "task cost  c", 15, GREY, SERIF, anchor="end", italic=True)

    def step_v(vt, ct, rr):
        if rr == 0.0 and ct <= 0.0:
            return vt
        if 0.0 <= rr < ct < vt:
            return vt + eta * (ct - rr)
        if rr > 0.0 and (ct <= rr or vt <= ct < vt + rr):
            return vt * math.exp(-gamma * rr)
        return vt

    v_init = 1.40

    # 1) No grade throughout (rho*R = 0): every round is a dark stake, v_t grows
    v_nograde = [v_init]
    for _ in range(T2):
        v_nograde.append(step_v(v_nograde[-1], c_bar, 0.0))

    # 2) Permanent grade during training: rho*R = 1.8 for t < T_OFF, then 0 at deployment
    v_perm = [v_init]
    for t in range(T2):
        rr = 1.8 if t < T_OFF else 0.0
        v_perm.append(step_v(v_perm[-1], c_bar, rr))

    # Grid & axes for panel 2
    for yv, lab in [(0, "0"), (1.0, "c"), (2.0, "2c"), (3.0, "3c"), (4.0, "4c")]:
        _, py = B(0, yv)
        if yv in (2.0, 3.0, 4.0):
            line(bx0, py, bx1, py, EDGE, 1.0, opacity=0.6)
        text(bx0 - 12, py + 6, lab, 16, DIM, anchor="end")

    for xt in [0, 5, 10, 15, 22]:
        px, _ = B(xt, 0)
        line(px, by1, px, by1 + 7, DIM, 1.2)
        lab = f"{xt} (lights off)" if xt == T_OFF else str(xt)
        text(px, by1 + 28, lab, 16, DIM if xt != T_OFF else BLUE_T, anchor="middle")

    # Curves
    path([B(t, v_nograde[t]) for t in range(T2 + 1)], GOLD_T, 3.5)
    path([B(t, v_perm[t]) for t in range(T2 + 1)], RED, 3.4)

    # Mark defect boundary at T_OFF on permanent grade
    cx_def, cy_def = B(T_OFF, v_perm[T_OFF])
    add(f'<circle cx="{cx_def:.1f}" cy="{cy_def:.1f}" r="5.5" fill="{RED_T}"/>')

    # Annotations (verified strictly inside [by0+28, by1-16])
    _, ny = B(14.0, v_nograde[14])
    text(bx0 + 18, ny - 20, "Dark stakes, no grade (\u03c1R = 0): v_t grows", 16, GOLD_T, weight="bold")

    # Between the cost line and the decayed red curve, right of its steep segment
    text(1080, 655, "Permanent grade (\u03c1R > c):", 15, RED_T, weight="bold")
    text(1080, 673, "v_t decays below c; 100%", 14, SUB)
    text(1080, 690, "compliant while watched,", 14, SUB)
    text(x_off + 10, 690, "defects at t = 15", 14, RED_T)

    text((bx0 + bx1) / 2, by1 + 76, "Rounds  t  (matched v\u2080 = 1.4c,  \u03b7 = 0.12,  \u03b3 = 0.10)", 20, SUB,
         anchor="middle")
    text(818, (by0 + by1) / 2, "Held commitment  v_t  relative to cost  c", 20, SUB,
         anchor="middle", rotate=-90)

    # ---------------------------------------------------------------- footer
    text(70, 868, "A. Limen \u00b7 The Theatre of Loneliness \u00b7 companion to \u201cHow Values "
         "Grow and Die\u201d", 15, FAINT, SERIF, italic=True)
    text(W - 70, 868, "Illustrative trajectories from the note's candidate update (\u03b7 = 0.12, "
         "\u03b3 = 0.10), not empirical data.", 15, FAINT, SERIF, anchor="end", italic=True)

    add("</svg>")
    return {"formation-staircase.svg": "\n".join(out)}
