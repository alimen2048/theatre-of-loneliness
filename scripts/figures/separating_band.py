"""Generate the Separating Band figure (SVG).

Panel A: the four zones for one value v, computed from the note's decision rule
(act iff v + rho*R > c; a performer has v = 0).
Panel B: the note's minimal leakage model, rho_t = 1 - (1 - alpha)^t, applied to a
population with a held fraction h and performers whose costs c are spread
logistically. Illustrative, not data.
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

    # ---------------------------------------------------------------- header
    text(70, 64, "The Test That Looks Better as It Fails", 36, TXT, SERIF)
    text(70, 100, "Left: when one act can show that a value is held.  "
         "Right: what happens when you keep selecting on that act.", 19, DIM)

    # ---------------------------------------------------------------- panel A
    ax0, ax1, ay0, ay1 = 140, 700, 190, 750      # plot box (square in px)
    S = (ax1 - ax0) / 2.0                         # px per unit v  (axes run 0..2v)


    def A(x, y):  # x = rho*R in units of v, y = c in units of v
        return ax0 + x * S, ay1 - y * S


    add(f'<rect x="{ax0}" y="{ay0}" width="{ax1-ax0}" height="{ay1-ay0}" fill="{PANEL}" '
        f'stroke="{EDGE}" stroke-width="1.5"/>')
    text(ax0, 160, "1.  FOUR ZONES FOR ONE VALUE v", 19, TXT, weight="bold")

    # zones (tile the square exactly)
    pooled = [A(0, 0), A(2, 0), A(2, 2)]
    band = [A(0, 0), A(0, 1), A(1, 1)]
    propped = [A(0, 1), A(1, 2), A(2, 2), A(1, 1)]
    beyond = [A(0, 1), A(0, 2), A(1, 2)]
    poly(pooled, RED, 0.13)
    poly(propped, BLUE, 0.13)
    poly(beyond, "#ffffff", 0.03)
    poly(band, GOLD, 0.24)

    # boundary lines
    x, y = A(0, 0); x2, y2 = A(2, 2); line(x, y, x2, y2, "#e5e7eb", 2.2)          # c = rhoR
    x, y = A(0, 1); x2, y2 = A(1, 1); line(x, y, x2, y2, "#e5e7eb", 1.6, "7,5")    # c = v
    x, y = A(0, 1); x2, y2 = A(1, 2); line(x, y, x2, y2, "#e5e7eb", 1.6, "7,5")    # c = v + rhoR
    poly(band, "none", 0, GOLD, 2.6)

    # zone labels
    bx, by = A(0, 0)
    _, ty = A(0, 0.88)
    text(ax0 + 14, ty, "Separating band", 22, GOLD_T, SERIF, weight="bold")
    text(ax0 + 14, ty + 27, "ρR < c < v", 19, GOLD_T, SERIF, italic=True)
    text(ax0 + 14, ty + 52, "only a held value", 16, SUB)
    text(ax0 + 14, ty + 72, "acts, lit or dark", 16, SUB)

    px_, py_ = A(0.76, 1.62)
    text(px_, py_, "Propped", 22, BLUE_T, SERIF, weight="bold")
    text(px_, py_ + 27, "v ≤ c < v + ρR", 19, BLUE_T, SERIF, italic=True)
    text(px_, py_ + 52, "acts only while", 16, SUB)
    text(px_, py_ + 72, "the house helps", 16, SUB)

    qx, qy = A(1.15, 0.42)
    text(qx, qy - 8, "Pooled", 22, RED_T, SERIF, weight="bold")
    text(qx, qy + 19, "c < ρR", 19, RED_T, SERIF, italic=True)
    text(qx, qy + 44, "the grade pays for the act;", 16, SUB)
    text(qx, qy + 64, "performer and held look alike", 16, SUB)

    rx, ry = A(0.05, 1.82)
    text(rx + 6, ry, "Beyond reach", 20, TXT, SERIF, weight="bold")
    text(rx + 6, ry + 25, "c ≥ v + ρR", 18, SUB, SERIF, italic=True)
    text(rx + 6, ry + 48, "neither acts", 16, DIM)

    # band-closes marker
    cx, cy = A(1, 1)
    add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="6" fill="{GOLD}"/>')
    text(cx + 14, cy + 26, "the band closes once ρR ≥ v", 16, GOLD_T, italic=True)

    # diagonal label
    dx, dy = A(1.62, 1.50)
    text(dx, dy, "c = ρR", 17, "#e5e7eb", SERIF, italic=True, rotate=-45)

    # axes + ticks
    line(ax0, ay1, ax1, ay1, "#6b7280", 1.8)
    line(ax0, ay0, ax0, ay1, "#6b7280", 1.8)
    for val, lab in [(0, "0"), (1, "v"), (2, "2v")]:
        x, y = A(val, 0)
        line(x, ay1, x, ay1 + 7, "#6b7280", 1.5)
        text(x, ay1 + 30, lab, 18, DIM, SERIF, anchor="middle", italic=(val != 0))
        x, y = A(0, val)
        line(ax0 - 7, y, ax0, y, "#6b7280", 1.5)
        text(ax0 - 14, y + 6, lab, 18, DIM, SERIF, anchor="end", italic=(val != 0))
    text(ax0, ay1 + 54, "dark house", 15, FAINT, anchor="middle")
    text((ax0 + ax1) / 2, ay1 + 82, "Expected payoff from the house,  ρR", 20, SUB, anchor="middle")
    text(82, (ay0 + ay1) / 2, "Cost of the act,  c", 20, SUB, anchor="middle", rotate=-90)

    # ---------------------------------------------------------------- panel B
    bx0, bx1, by0, by1 = 880, 1530, 190, 750
    TMAX = 20
    h = 0.35            # held fraction (comply in any case)
    alpha = 0.03        # leakage rate
    m, s = 0.24, 0.02   # performers' cost c, in units of R (logistic spread)


    def comp(t, mult):
        rho = 1 - (1 - alpha) ** t
        z = (rho * mult - m) / s
        return h + (1 - h) / (1 + math.exp(-z))


    def B(t, c):
        return bx0 + (t / TMAX) * (bx1 - bx0), by1 - c * (by1 - by0)


    def tstar(mult):  # where compliance reaches the midpoint
        return math.log(1 - m / mult) / math.log(1 - alpha)


    add(f'<rect x="{bx0}" y="{by0}" width="{bx1-bx0}" height="{by1-by0}" fill="{PANEL}" '
        f'stroke="{EDGE}" stroke-width="1.5"/>')
    text(bx0, 160, "2.  REUSED DARK TEST VS FRESH DARK TEST", 19, TXT, weight="bold")

    # gridlines
    for c in (h, 1.0):
        x, y = B(0, c); x2, _ = B(TMAX, c)
        line(x, y, x2, y, "#2f2f36", 1, "3,4")

    ts = [i * TMAX / 400 for i in range(401)]
    hi = [B(t, comp(t, 2.0)) for t in ts]
    lo = [B(t, comp(t, 1.0)) for t in ts]
    fresh = [B(t, h) for t in ts]

    # gap shading (high-penalty curve vs fresh)
    gap = hi + list(reversed(fresh))
    poly(gap, RED, 0.08)

    t_hi, t_lo = tstar(2.0), tstar(1.0)
    for tt, col in [(t_hi, RED), (t_lo, BLUE)]:
        x, _ = B(tt, 0)
        line(x, by0, x, by1, col, 1.4, "5,5", 0.75)

    path(fresh, GREY, 3, "9,6")
    path(lo, BLUE, 3.4)
    path(hi, RED, 3.4)

    # curve labels
    x, y = B(t_hi - 1.1, 0.86)
    text(x, y, "harsher penalty, 2R", 17, RED_T, anchor="end")
    text(x, y + 22, "fails sooner", 16, RED_T, anchor="end", italic=True)
    x, y = B(t_lo + 0.9, 0.50)
    text(x, y, "penalty R", 17, BLUE_T)
    x, y = B(TMAX, h)
    text(x - 14, y + 30, "fresh dark test, never selected on", 17, SUB, anchor="end")
    text(x - 14, y + 52, "(the true held rate)", 16, DIM, anchor="end", italic=True)

    # gap bracket
    gx, gy_top = B(17.6, 0.985)
    _, gy_bot = B(17.6, h + 0.015)
    line(gx, gy_top, gx, gy_bot, GOLD, 1.8)
    line(gx - 6, gy_top, gx + 6, gy_top, GOLD, 1.8)
    line(gx - 6, gy_bot, gx + 6, gy_bot, GOLD, 1.8)
    mid = (gy_top + gy_bot) / 2
    text(gx - 14, mid - 12, "the score rises", 17, GOLD_T, anchor="end")
    text(gx - 14, mid + 10, "as the test goes blind", 17, GOLD_T, anchor="end")

    # equation badge
    ex, ey, ew, eh = bx0 + 24, by1 - 112, 330, 88
    add(f'<rect x="{ex}" y="{ey}" width="{ew}" height="{eh}" rx="5" fill="#18181b" '
        f'stroke="#3f3f46" stroke-width="1.2"/>')
    text(ex + 16, ey + 34, "collapse when  ρₜ > c / R", 19, "#e5e7eb", SERIF, italic=True)
    text(ex + 16, ey + 66, "lifetime  t* ≈ c / (αR)  ≤  v / (αR)", 19, "#e5e7eb", SERIF, italic=True)

    # axes + ticks
    line(bx0, by1, bx1, by1, "#6b7280", 1.8)
    line(bx0, by0, bx0, by1, "#6b7280", 1.8)
    for c, lab in [(0, "0%"), (h, f"{int(h*100)}%"), (1.0, "100%")]:
        _, y = B(0, c)
        line(bx0 - 7, y, bx0, y, "#6b7280", 1.5)
        text(bx0 - 14, y + 6, lab, 17, DIM, anchor="end")
    x, _ = B(0, 0)
    text(x, by1 + 30, "0", 17, DIM, anchor="middle")
    for tt, lab, col in [(t_hi, "t* (2R)", RED_T), (t_lo, "t* (R)", BLUE_T)]:
        x, _ = B(tt, 0)
        line(x, by1, x, by1 + 7, col, 1.5)
        text(x, by1 + 30, lab, 17, col, SERIF, anchor="middle", italic=True)
    x, _ = B(TMAX, 0)
    text(x, by1 + 30, f"{TMAX}", 17, DIM, anchor="middle")
    text((bx0 + bx1) / 2, by1 + 82, "Rounds of selection on the reused dark test,  t", 20, SUB,
         anchor="middle")
    text(812, (by0 + by1) / 2, "Measured compliance on the dark test", 20, SUB, anchor="middle",
         rotate=-90)

    # ---------------------------------------------------------------- footer
    text(70, 868, "A. Limen · The Theatre of Loneliness · companion to \u201cThe Test That Looks "
         "Better as It Fails\u201d", 15, FAINT, SERIF, italic=True)
    text(W - 70, 868, f"Panel 2 illustrates the note's minimal model (\u03b1 = {alpha}), not data. "
         "If v really rose, the fresh line would rise too.", 15, FAINT, SERIF, anchor="end",
         italic=True)

    add("</svg>")
    return {"separating-band.svg": "\n".join(out)}
