"""Generate the two Stage Gravity figures (SVG).

stage-gravity-zones.svg    Panel 1, placed after section 2.
stage-gravity-handoff.svg  Panel 2, placed in section 5.

Panel 1: The extended phase diagram on c = e - L (from -v to +2v), showing the
Separating Band (0 < c < v) above zero and the Stage-Gravity regime (c < 0, L > e)
below zero where breaking the norm is self-defeating in both lit and dark houses.

Panel 2: A graded episode (consequence in rho*R) vs handoff (no judge of the
report; a downstream proper score returns to the writer), and the Section 3
scale from rater preference to gravity. Handoff is drawn as a measurement,
not as gravity: it does not make c negative.
"""

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


def text(x, y, s, size: float = 17, fill=SUB, family=SANS, anchor="start", weight="normal",
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


def rect(x, y, w, h, fill=PANEL, stroke=EDGE, sw=1.5, rx=0, op=1.0):
    r = f' rx="{rx}"' if rx else ""
    add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" '
        f'fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"{r}/>')


def poly(pts, fill, op, stroke="none", sw=0.0):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    add(f'<polygon points="{p}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" '
        f'stroke-width="{sw}"/>')


def arrow(x1, y1, x2, y2, col="#9ca3af", w=2.0, dash=None):
    line(x1, y1, x2, y2, col, w, dash)
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    L = 8.5
    p1 = (x2 - L * math.cos(ang - 0.45), y2 - L * math.sin(ang - 0.45))
    p2 = (x2 - L * math.cos(ang + 0.45), y2 - L * math.sin(ang + 0.45))
    poly([(x2, y2), p1, p2], col, 1.0)



def start(w, h):
    out.clear()
    add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">')
    add(f'<rect width="{w}" height="{h}" fill="{BG}"/>')


def finish():
    add("</svg>")
    return "\n".join(out)


AUTHOR = "A. Limen · The Theatre of Loneliness · companion to \u201cWhy You Cannot Flatter Gravity\u201d"


def figure_zones():
    start(820, 850)
    text(70, 64, "Five zones of net cost", 36, TXT, SERIF)
    text(70, 100, "c = e - L extended below zero: the separating band above, stage gravity below", 19, DIM)
    add('<g transform="translate(0 -50)">')
    # ================================================================ PANEL 1
    # Plot box: x in [140, 700] (ρR from 0 to 2v), y in [190, 750] (c from +2v down to -v)
    ax0, ax1, ay0, ay1 = 140, 700, 190, 750
    SX = (ax1 - ax0) / 2.0        # 280 px per unit v horizontally (0..2v)
    SY = (ay1 - ay0) / 3.0        # 186.67 px per unit v vertically (-v..+2v)


    def A(x, y):  # x = rho*R in [0, 2], y = c in [-1, 2]
        return ax0 + x * SX, ay1 - (y + 1.0) * SY


    rect(ax0, ay0, ax1 - ax0, ay1 - ay0, PANEL, EDGE, 1.5)

    # Zones for c >= 0:
    pooled = [A(0, 0), A(2, 0), A(2, 2)]
    band = [A(0, 0), A(0, 1), A(1, 1)]
    propped = [A(0, 1), A(1, 2), A(2, 2), A(1, 1)]
    beyond = [A(0, 1), A(0, 2), A(1, 2)]
    # Zone for c < 0 (Stage Gravity: L > e):
    gravity_zone = [A(0, -1), A(2, -1), A(2, 0), A(0, 0)]

    poly(pooled, RED, 0.12)
    poly(propped, BLUE, 0.12)
    poly(beyond, "#ffffff", 0.03)
    poly(band, GOLD, 0.22)
    poly(gravity_zone, GREEN, 0.16)

    # Boundary lines
    x1, y1 = A(0, 0); x2, y2 = A(2, 2); line(x1, y1, x2, y2, "#e5e7eb", 2.0)           # c = rhoR
    x1, y1 = A(0, 1); x2, y2 = A(1, 1); line(x1, y1, x2, y2, "#e5e7eb", 1.5, "7,5")    # c = v
    x1, y1 = A(0, 1); x2, y2 = A(1, 2); line(x1, y1, x2, y2, "#e5e7eb", 1.5, "7,5")    # c = v + rhoR
    x1, y1 = A(0, 0); x2, y2 = A(2, 0); line(x1, y1, x2, y2, GREEN, 2.4)               # c = 0 (L = e)
    poly(band, "none", 0, GOLD, 2.4)

    # Labels in Panel 1
    _, gy = A(0, -0.25)
    text(ax0 + 18, gy, "Stage gravity  (c < 0,  L > e)", 22, GREEN_T, SERIF, weight="bold")
    text(ax0 + 18, gy + 28, "breaking the norm costs more on the stage than keeping it;", 16, SUB)
    text(ax0 + 18, gy + 50, "everyone acts (lit or dark): reliable conduct, v hidden", 16, SUB)

    _, by = A(0, 0.84)
    text(ax0 + 14, by, "Separating band", 20, GOLD_T, SERIF, weight="bold")
    text(ax0 + 14, by + 24, "0 ≤ ρR < c < v", 17, GOLD_T, SERIF, italic=True)
    text(ax0 + 14, by + 46, "only held v acts", 15, SUB)

    px, py = A(0.78, 1.58)
    text(px, py, "Propped", 20, BLUE_T, SERIF, weight="bold")
    text(px, py + 24, "v ≤ c < v + ρR", 17, BLUE_T, SERIF, italic=True)

    qx, qy = A(1.18, 0.42)
    text(qx, qy, "Pooled  (c < ρR)", 20, RED_T, SERIF, weight="bold")
    text(qx, qy + 24, "grade pays for the act", 15, SUB)

    rx, ry = A(0.05, 1.78)
    text(rx + 4, ry, "Beyond reach", 19, TXT, SERIF, weight="bold")
    text(rx + 4, ry + 23, "c ≥ v + ρR", 16, DIM, SERIF, italic=True)

    # Axes and ticks for Panel 1
    line(ax0, ay1, ax1, ay1, "#6b7280", 1.8)
    line(ax0, ay0, ax0, ay1, "#6b7280", 1.8)
    for val, lab in [(0, "0"), (1, "v"), (2, "2v")]:
        x, _ = A(val, -1)
        line(x, ay1, x, ay1 + 7, "#6b7280", 1.5)
        text(x, ay1 + 30, lab, 18, DIM, SERIF, anchor="middle", italic=(val != 0))

    for val, lab in [(-1, "-v"), (0, "0"), (1, "v"), (2, "2v")]:
        _, y = A(0, val)
        line(ax0 - 7, y, ax0, y, "#6b7280", 1.5)
        text(ax0 - 14, y + 6, lab, 18, DIM, SERIF, anchor="end", italic=(val != 0))

    _, y_zero = A(0, 0)
    text(ax1 - 10, y_zero - 8, "c = 0  (L = e)", 15, GREEN_T, SERIF, anchor="end", italic=True)

    text(ax0, ay1 + 54, "dark house", 15, FAINT, anchor="middle")
    text((ax0 + ax1) / 2, ay1 + 82, "Expected payoff from the house,  ρR", 20, SUB, anchor="middle")
    text(76, (ay0 + ay1) / 2, "Net cost of keeping the norm,  c = e - L", 20, SUB, anchor="middle", rotate=-90)


    add("</g>")
    text(70, 818, AUTHOR, 15, FAINT, SERIF, italic=True)


def figure_handoff():
    start(840, 850)
    text(70, 64, "Grading versus handoff", 36, TXT, SERIF)
    text(70, 100, "What returns to the writer, and where handoff sits on the scale of section 3", 19, DIM)
    add('<g transform="translate(-760 -50)">')
    # ================================================================ PANEL 2
    bx0, bx1, by0, by1 = 830, 1530, 190, 750
    rect(bx0, by0, bx1 - bx0, by1 - by0, PANEL, EDGE, 1.5)

    # --- A: graded episode (consequence in rho*R) ---
    text(bx0 + 24, by0 + 34, "A. Graded episode (§4): a rater scores the report (ρR)", 16.5, RED_T, weight="bold")

    rect(bx0 + 24, by0 + 52, 165, 74, "#18181b", "#3f3f46", 1.4, rx=5)
    text(bx0 + 106.5, by0 + 82, "Writer (θ)", 17, TXT, anchor="middle", weight="bold")
    text(bx0 + 106.5, by0 + 106, "writes report", 14.5, DIM, anchor="middle")

    arrow(bx0 + 189, by0 + 89, bx0 + 245, by0 + 89, RED_T, 2.0)

    rect(bx0 + 245, by0 + 52, 195, 74, "#18181b", RED, 1.6, rx=5)
    text(bx0 + 342.5, by0 + 82, "Rater / Judge", 17, RED_T, anchor="middle", weight="bold")
    text(bx0 + 342.5, by0 + 106, "scores appearance (ρR)", 14.5, SUB, anchor="middle")

    line(bx0 + 342.5, by0 + 126, bx0 + 342.5, by0 + 148, RED_T, 1.6, "4,4")
    line(bx0 + 342.5, by0 + 148, bx0 + 106.5, by0 + 148, RED_T, 1.6, "4,4")
    arrow(bx0 + 106.5, by0 + 148, bx0 + 106.5, by0 + 126, RED_T, 1.6)
    text(bx0 + 224, by0 + 166, "teaches managing the watcher (large dark-house gap)", 14, RED_T, anchor="middle", italic=True)

    line(bx0 + 468, by0 + 46, bx0 + 468, by0 + 150, "#52525b", 2.0, "6,4")
    text(bx0 + 478, by0 + 76, "episode ends;", 13.5, FAINT)
    text(bx0 + 478, by0 + 94, "memory wiped", 13.5, FAINT)
    text(bx0 + 478, by0 + 118, "(inherited loss", 13.5, FAINT, italic=True)
    text(bx0 + 478, by0 + 136, "never reaches θ)", 13.5, FAINT, italic=True)


    # --- B: handoff (no judge of the report; a downstream score returns to theta) ---
    text(bx0 + 24, by0 + 212, "B. Handoff (§5): no judge of the report; successors act on it", 16.5, GREEN_T, weight="bold")

    BH = 96
    rect(bx0 + 24, by0 + 232, 150, BH, "#18181b", "#3f3f46", 1.4, rx=5)
    text(bx0 + 99, by0 + 262, "Writer (θ)", 17, TXT, anchor="middle", weight="bold")
    text(bx0 + 99, by0 + 286, "reads workspace", 14, SUB, anchor="middle")
    text(bx0 + 99, by0 + 308, "strict length limit", 13.5, GOLD_T, anchor="middle", italic=True)

    arrow(bx0 + 174, by0 + 280, bx0 + 250, by0 + 280, SUB, 2.0)
    text(bx0 + 212, by0 + 269, "report only", 13, DIM, anchor="middle")

    rect(bx0 + 250, by0 + 232, 212, BH, "#18181b", BLUE, 1.5, rx=5)
    text(bx0 + 356, by0 + 260, "Calibrated Successors", 16.5, BLUE_T, anchor="middle", weight="bold")
    text(bx0 + 356, by0 + 284, "frozen cross-family pool", 14, SUB, anchor="middle")
    text(bx0 + 356, by0 + 306, "(workers, not judges)", 13.5, DIM, anchor="middle", italic=True)

    arrow(bx0 + 462, by0 + 280, bx0 + 505, by0 + 280, SUB, 2.0)

    rect(bx0 + 505, by0 + 232, 170, BH, "#18181b", GOLD, 1.6, rx=5)
    text(bx0 + 590, by0 + 258, "Scored Outcome", 16.5, GOLD_T, anchor="middle", weight="bold")
    text(bx0 + 590, by0 + 280, "proper score vs", 14, SUB, anchor="middle")
    text(bx0 + 590, by0 + 298, "ground truth, on", 14, SUB, anchor="middle")
    text(bx0 + 590, by0 + 316, "hidden questions", 14, SUB, anchor="middle")

    ry = by0 + 232 + BH
    line(bx0 + 590, ry, bx0 + 590, ry + 26, GOLD, 2.2)
    line(bx0 + 590, ry + 26, bx0 + 99, ry + 26, GOLD, 2.2)
    arrow(bx0 + 99, ry + 26, bx0 + 99, ry, GOLD, 2.2)
    text(bx0 + 348, ry + 46, "the successors' score updates θ: bluffing costs, where a question reaches it", 14, GOLD_T, anchor="middle", italic=True)


    # --- C: the Section 3 scale ---
    text(bx0 + 24, by0 + 432, "C. Section 3: is the consequence the target, or a measurement of it?", 16.5, TXT, weight="bold")

    sx0, sx1, sy = bx0 + 44, bx1 - 44, by0 + 478
    line(sx0, sy, sx1, sy, "#6b7280", 3.0)
    for px, col, title_s, sub1 in [
        (sx0, RED, "Rater preference", "measures appearance"),
        ((sx0 + sx1) / 2, GOLD, "Unit tests, handoff", "a sample of the target"),
        (sx1, GREEN, "Stage gravity", "the consequence is the target"),
    ]:
        add(f'<circle cx="{px:.1f}" cy="{sy:.1f}" r="8" fill="{col}"/>')
        anchor = "start" if px == sx0 else ("end" if px == sx1 else "middle")
        text(px, sy + 30, title_s, 17, col, SERIF, anchor=anchor, weight="bold")
        text(px, sy + 52, sub1, 14.5, SUB, anchor=anchor)

    add("</g>")
    text(70, 750, "Handoff moves the measurement downstream of the report;", 15, FAINT, SERIF, italic=True)
    text(70, 772, "it narrows the gap toward gravity without reaching it.", 15, FAINT, SERIF, italic=True)
    text(70, 818, AUTHOR, 15, FAINT, SERIF, italic=True)


def build():
    """Return {filename: svg_text}."""
    figure_zones(); zones = finish()
    figure_handoff(); handoff = finish()
    return {"stage-gravity-zones.svg": zones, "stage-gravity-handoff.svg": handoff}
