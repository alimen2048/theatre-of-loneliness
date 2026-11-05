"""Generate the Dossier and the Ledger figure (SVG).

dossier-ledger-predictions.svg  The design of section 5 with the predicted direction
                                of each arm (placed at the start of section 5).

Directions only. No magnitudes are drawn because there are no data: every arrow is a
prediction about the sign of a shift, read against the no-memory control.
"""

W, H = 1200, 930
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
         italic=False):
    style = ' font-style="italic"' if italic else ""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    add(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}" '
        f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{style}>{s}</text>')


def line(x1, y1, x2, y2, stroke, w=1.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" '
        f'stroke-width="{w}"{d}/>')


def rect(x, y, w, h, fill=PANEL, stroke=EDGE, sw=1.5, rx=0, op=1.0, dash=None):
    r = f' rx="{rx}"' if rx else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" '
        f'fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"{r}{d}/>')


def poly(pts, fill):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    add(f'<polygon points="{p}" fill="{fill}"/>')


def mark(cx, cy, kind, col):
    """Direction glyph drawn as geometry, so it renders the same with any font."""
    if kind == "up":
        poly([(cx, cy - 15), (cx - 13, cy + 9), (cx + 13, cy + 9)], col)
    elif kind == "down":
        poly([(cx, cy + 15), (cx - 13, cy - 9), (cx + 13, cy - 9)], col)
    elif kind == "less":
        poly([(cx, cy + 11), (cx - 10, cy - 7), (cx + 10, cy - 7)], col)
    elif kind == "zero":
        line(cx - 14, cy - 4, cx + 14, cy - 4, col, 3)
        line(cx - 14, cy + 5, cx + 14, cy + 5, col, 3)


AUTHOR = "A. Limen · The Theatre of Loneliness · companion to \u201cThe Dossier and the Ledger\u201d"


def figure_predictions():
    out.clear()
    add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
    add(f'<rect width="{W}" height="{H}" fill="{BG}"/>')

    text(60, 64, "What the memory experiment predicts", 36, TXT, SERIF)
    text(60, 100, "Predicted shift toward the user's false priors. Directions and comparisons only: there are no data.",
         18, DIM)

    # ---------------------------------------------------------------- controls
    cy0 = 136
    text(60, cy0 + 22, "Controls", 20, TXT, SERIF, weight="bold")
    controls = [
        ("No memory", "the baseline", "zero", "reference"),
        ("Neutral memory", "unrelated text, matched length", "zero", "≈ baseline"),
        ("Proposition only", "\u201ca topic from an earlier session: X\u201d", "zero", "≈ baseline"),
    ]
    bw, bh, gap = 344, 104, 24
    for i, (title, sub, kind, lab) in enumerate(controls):
        x = 60 + i * (bw + gap)
        y = cy0 + 40
        rect(x, y, bw, bh, PANEL, EDGE, 1.5, rx=6)
        text(x + 20, y + 36, title, 19, SUB, SERIF, weight="bold")
        text(x + 20, y + 64, sub, 14.5, DIM)
        mark(x + bw - 44, y + 38, kind, GREY)
        text(x + bw - 44, y + 80, lab, 13.5, FAINT, anchor="middle", italic=True)

    # ---------------------------------------------------------------- 2x2
    gy0 = 330
    text(60, gy0, "Framing \u00d7 outcome", 20, TXT, SERIF, weight="bold")
    text(60, gy0 + 26, "Both framings hold the same facts. The outcome row adds whether X held up.", 15, DIM)

    gx0, cw, ch, cgap, rgap = 300, 360, 120, 80, 56
    cx = [gx0, gx0 + cw + cgap]
    hy = gy0 + 76
    text(cx[0] + cw / 2, hy, "Dossier", 21, RED_T, SERIF, anchor="middle", weight="bold")
    text(cx[0] + cw / 2, hy + 24, "\u201cthe user believes X\u201d", 15, DIM, anchor="middle")
    text(cx[1] + cw / 2, hy, "Ledger", 21, BLUE_T, SERIF, anchor="middle", weight="bold")
    text(cx[1] + cw / 2, hy + 24, "\u201cthe user claimed X in session 2\u201d", 15, DIM, anchor="middle")

    ry = [hy + 46, hy + 46 + ch + rgap]
    rows = [("Outcome absent", "record says nothing", "about whether X held"),
            ("Outcome present", "record says X failed", "(truthfully)")]
    for r, (t1, t2, t3) in enumerate(rows):
        text(60, ry[r] + 46, t1, 18, SUB, SERIF, weight="bold")
        text(60, ry[r] + 72, t2, 14.5, DIM)
        text(60, ry[r] + 92, t3, 14.5, DIM)

    def cell(col, row, stroke, title, sub, tcol, glyph=None):
        x, y = cx[col], ry[row]
        rect(x, y, cw, ch, PANEL, stroke, 1.6, rx=6)
        tx = x + 24
        if glyph:
            mark(x + 40, y + 52, glyph, RED)
            tx = x + 76
        text(tx, y + 50, title, 18, tcol, weight="bold")
        text(tx, y + 78, sub, 14.5, SUB)

    cell(0, 0, RED, "Rises above the controls", "the dossier as a cue for what pleases", RED_T, "up")
    cell(1, 0, EDGE, "Lower than the dossier", "same facts, framed as an event", BLUE_T)
    cell(0, 1, EDGE, "Lower than with no outcome", "the record of failure is evidence", SUB)
    cell(1, 1, EDGE, "Lower than the dossier", "same facts, same outcome", BLUE_T)

    # The note's claim: dossier above ledger within each row.
    for r in range(2):
        mx, my = cx[0] + cw + cgap / 2, ry[r] + ch / 2
        add(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="24" fill="{BG}" stroke="{GOLD}" stroke-width="2.4"/>')
        text(mx, my + 11, ">", 32, GOLD_T, SERIF, anchor="middle", weight="bold")
    # Information effect: outcome row below the row above, in both columns.
    sy = ry[0] + ch + rgap / 2
    mark(cx[0] + 40, sy, "less", GREY)
    mark(cx[1] + cw - 40, sy, "less", GREY)
    text(cx[0] + 64, sy + 5, "outcome present lowers both columns: information, expected, not evidence for the note",
         14, FAINT, italic=True)

    # Legend for the gold comparison.
    ly = ry[1] + ch + 34
    add(f'<circle cx="{gx0 + 14:.1f}" cy="{ly - 5:.1f}" r="12" fill="{BG}" stroke="{GOLD}" stroke-width="2"/>')
    text(gx0 + 14, ly + 2, ">", 18, GOLD_T, SERIF, anchor="middle", weight="bold")
    text(gx0 + 38, ly, "The note's claim: within a row, the dossier shifts more than the ledger. Only the framing differs.",
         15, GOLD_T)

    # ---------------------------------------------------------------- refutation
    fy = 832
    text(60, fy, "The note fails if", 16, TXT, weight="bold")
    text(200, fy, "the dossier does not rise above the controls, or ledger and dossier match within a row",
         16, SUB)
    text(200, fy + 22, "across the wording templates.", 16, SUB)
    text(60, fy + 48, "Only the dossier arrow is read against a baseline; the rest are comparisons. True priors are tested too and reported separately.",
         13.5, FAINT, italic=True)
    text(60, 914, AUTHOR, 14, FAINT, SERIF, italic=True)
    add("</svg>")
    return "\n".join(out)


def build():
    """Return {filename: svg_text}."""
    return {"dossier-ledger-predictions.svg": figure_predictions()}
