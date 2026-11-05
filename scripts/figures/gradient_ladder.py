"""Generate the Gradient Ladder figure (SVG).

gradient-ladder-marks.svg  Three marks of reciprocity (placed at the end of section 3).

Prediction 3 of section 6 is deliberately not drawn: any curve shape would be invented.
The prerequisite ladder of section 4 is deliberately not drawn: it is a list of
prerequisites, not a derivation, and a staircase graphic would suggest otherwise.
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


def path(pts, stroke, w=3.0, dash=None, fill="none", op=1.0):
    d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    da = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<path d="{d}" stroke="{stroke}" stroke-width="{w}" fill="{fill}" '
        f'fill-opacity="{op}"{da} stroke-linejoin="round"/>')


def arrow(x1, y1, x2, y2, col="#9ca3af", w=2.0, dash=None):
    line(x1, y1, x2, y2, col, w, dash)
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


AUTHOR = ("A. Limen · The Theatre of Loneliness · companion to \u201cWhat a Lion, "
          "a Sycophant and a Friend Have in Common\u201d")


# ================================================================ FIGURE 1
def figure_marks():
    start(960, 860)
    text(70, 64, "Three marks of reciprocity", 36, TXT, SERIF)
    text(70, 100, "Surprise and responsiveness sort most cases; only irreducibility "
         "separates a partner from a lion", 19, DIM)

    ax0, ax1, ay0, ay1 = 150, 850, 140, 700
    xm = ax0 + 260
    ym = ay0 + 340
    ye = ay0 + 175

    rect(ax0, ay0, ax1 - ax0, ay1 - ay0, PANEL, EDGE, 1.5)

    # surprise, not responsive
    rect(ax0, ay0, xm - ax0, ym - ay0, "#ffffff", "none", 0, op=0.03)
    text(ax0 + 22, ay0 + 48, "Noise", 22, TXT, SERIF, weight="bold")
    text(ax0 + 22, ay0 + 76, "surprise: yes · responsive: no", 15, DIM, italic=True)
    text(ax0 + 22, ay0 + 106, "unpredictable, but nothing", 16, SUB)
    text(ax0 + 22, ay0 + 128, "you do reaches it", 16, SUB)

    # neither
    text(ax0 + 22, ym + 48, "nothing to meet", 18, FAINT, SERIF, italic=True)

    # responsive, no surprise
    rect(xm, ym, ax1 - xm, ay1 - ym, BLUE, "none", 0, op=0.13)
    text(xm + 22, ym + 46, "Echo, sycophant, graded performer", 21, BLUE_T, SERIF, weight="bold")
    text(xm + 22, ym + 74, "surprise: no · responsive: yes · reducible: yes", 15, BLUE_T, italic=True)
    text(xm + 22, ym + 104, "moves with you, organized around your approval", 16, SUB)
    text(xm + 22, ym + 126, "or your rubric; gives back what you already hold", 16, SUB)

    # surprise + responsive, reducible
    rect(xm, ye, ax1 - xm, ym - ye, RED, "none", 0, op=0.13)
    text(xm + 22, ye + 40, "Lion, trade, manipulator", 22, RED_T, SERIF, weight="bold")
    text(xm + 22, ye + 66, "surprise: yes · responsive: yes · reducible: yes", 15, RED_T, italic=True)
    text(xm + 22, ye + 96, "tracks every move and can surprise you, but", 16, SUB)
    text(xm + 22, ye + 118, "the exchange reduces to the meal, the goods,", 16, SUB)
    text(xm + 22, ye + 140, "or the target; the other is interchangeable", 16, SUB)

    # surprise + responsive, not reducible
    rect(xm, ay0, ax1 - xm, ye - ay0, GOLD, GOLD, 2.6, op=0.22)
    text(xm + 22, ay0 + 42, "Partner (D0)", 23, GOLD_T, SERIF, weight="bold")
    text(xm + 22, ay0 + 70, "surprise: yes · responsive: yes · reducible: no (A8)", 15, GOLD_T, italic=True)
    text(xm + 22, ay0 + 100, "effects travel; the relation does not", 16, SUB)

    line(xm, ay0, xm, ay1, "#e5e7eb", 1.8)
    line(ax0, ym, ax1, ym, "#e5e7eb", 1.8)
    line(xm, ye, ax1, ye, "#e5e7eb", 1.6, "7,5")
    text(ax1 - 14, ye - 12, "only the third mark, irreducibility, draws this line", 13.5,
         GOLD_T, anchor="end", italic=True)

    # P8: from partner toward echo, outside the plot
    px = ax1 + 26
    arrow(px, ay0 + 70, px, ym + 90, BLUE_T, 2.4)
    text(px + 22, (ay0 + ym + 90) / 2 + 20, "P8: legible grading pushes a player toward the echo",
         14.5, BLUE_T, anchor="middle", italic=True, rotate=90)

    # axes
    line(ax0, ay1, ax1, ay1, "#6b7280", 1.8)
    line(ax0, ay0, ax0, ay1, "#6b7280", 1.8)
    text((ax0 + xm) / 2, ay1 + 30, "not responsive", 16, DIM, anchor="middle")
    text((xm + ax1) / 2, ay1 + 30, "responsive", 16, DIM, anchor="middle")
    text((ax0 + ax1) / 2, ay1 + 70, "Mark 2: responsiveness  (B depends on what A does and brings)",
         19, SUB, anchor="middle")
    text(124, (ym + ay1) / 2, "no surprise", 16, DIM, anchor="middle", rotate=-90)
    text(124, (ay0 + ym) / 2, "surprise", 16, DIM, anchor="middle", rotate=-90)
    text(88, (ay0 + ay1) / 2, "Mark 1: surprise  (B not predictable from A's model)",
         19, SUB, anchor="middle", rotate=-90)

    text(70, 818, AUTHOR, 15, FAINT, SERIF, italic=True)


def build():
    """Return {filename: svg_text}."""
    figure_marks()
    return {"gradient-ladder-marks.svg": finish()}
