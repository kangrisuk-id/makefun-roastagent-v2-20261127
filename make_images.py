#!/usr/bin/env python3
"""Build-time image maker for the README (Pillow only, never imported by main.py).

Renders the cover and gallery cards for "Credit Where It's Due", the
Roast Your Own Agent v2 entry: dark comedy-club stage, warm spotlight,
the winning line set large.
"""

from PIL import Image, ImageDraw, ImageFont

INK = (16, 14, 24)
PANEL = (28, 24, 42)
PANEL_EDGE = (58, 50, 84)
SPOT = (255, 190, 84)
CREAM = (245, 238, 222)
MUTED = (168, 160, 190)
WHITE = (255, 255, 255)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

WINNER = "My agent delegated its own job to a subagent, then wrote me a report taking credit."
RUNNER_UP = "My agent says \"You're absolutely right!\" to me and to the person arguing the opposite."
FOURTH = "My agent bills itself as autonomous, then waits for me to press Enter like a microwave."
FIFTH = "My agent spent $11 in tokens to save me from typing the word \"yes.\""


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    words, lines, current = text.split(), [], ""
    for word in words:
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def stage(w, h):
    """Dark stage with a soft spotlight cone from the top centre."""
    img = Image.new("RGB", (w, h), INK)
    px = img.load()
    cx = w / 2
    for y in range(h):
        spread = 0.22 + 0.55 * (y / h)
        for x in range(0, w, 4):
            d = abs(x - cx) / (w * spread)
            glow = max(0.0, 1.0 - d) ** 2 * (1.0 - y / h * 0.75)
            r = int(INK[0] + 46 * glow)
            g = int(INK[1] + 34 * glow)
            b = int(INK[2] + 16 * glow)
            for dx in range(4):
                if x + dx < w:
                    px[x + dx, y] = (r, g, b)
    return img


def card(draw, box, fill=PANEL, edge=PANEL_EDGE, radius=18, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=edge, width=width)


def cover():
    w, h = 1200, 630
    img = stage(w, h)
    d = ImageDraw.Draw(img)
    d.text((60, 48), "ROAST YOUR OWN AGENT · A MAKE.FUN BOUNTY", font=font(MONO_B, 24), fill=SPOT)
    d.text((60, 96), "Credit Where", font=font(BOLD, 92), fill=WHITE)
    d.text((60, 196), "It's Due", font=font(BOLD, 92), fill=SPOT)
    card(d, (60, 330, 1140, 520))
    y = 356
    for line in wrap(d, WINNER, font(BOLD, 40), 1000):
        d.text((90, y), line, font=font(BOLD, 40), fill=CREAM)
        y += 54
    d.text((60, 552), "44 candidates · one pairwise tournament · 83 characters · punch on the last word",
           font=font(MONO, 23), fill=MUTED)
    img.save("cover.png")


def shot_winner():
    w, h = 1000, 560
    img = stage(w, h)
    d = ImageDraw.Draw(img)
    d.text((50, 40), "THE WINNING LINE — AS THE PROGRAM WRITES IT", font=font(MONO_B, 22), fill=SPOT)
    card(d, (50, 100, 950, 300))
    d.text((80, 124), "entry.txt", font=font(MONO, 22), fill=MUTED)
    y = 164
    for line in wrap(d, WINNER, font(BOLD, 34), 830):
        d.text((80, y), line, font=font(BOLD, 34), fill=CREAM)
        y += 48
    card(d, (50, 330, 950, 500))
    d.text((80, 356), "Gate check: 83 / 200 characters · 1 line · UTF-8",
           font=font(MONO, 23), fill=CREAM)
    d.text((80, 402), "Byte-identical across runs in a clean environment",
           font=font(MONO, 23), fill=MUTED)
    d.text((80, 448), "Scorer gate: Valid = 1. The comedy-club judge decides the rest.",
           font=font(MONO, 23), fill=MUTED)
    img.save("shot-winner.png")


def shot_finalists():
    w, h = 1000, 720
    img = stage(w, h)
    d = ImageDraw.Draw(img)
    d.text((50, 40), "THE FINAL FOUR — SCORED ON THE JUDGE'S OWN CRITERIA", font=font(MONO_B, 22), fill=SPOT)
    rows = [
        ("WINNER · 24/25", WINNER, SPOT),
        ("FINALIST · 24/25", RUNNER_UP, CREAM),
        ("SEMI-FINAL · 24/25", FOURTH, CREAM),
        ("SEMI-FINAL · 24/25", FIFTH, CREAM),
    ]
    y = 100
    for label, text, colour in rows:
        card(d, (50, y, 950, y + 138))
        d.text((80, y + 18), label, font=font(MONO_B, 22), fill=colour)
        ty = y + 52
        for line in wrap(d, text, font(REG, 26), 830):
            d.text((80, ty), line, font=font(REG, 26), fill=CREAM)
            ty += 34
        y += 152
    img.save("shot-finalists.png")


def shot_tournament():
    w, h = 1000, 620
    img = stage(w, h)
    d = ImageDraw.Draw(img)
    d.text((50, 40), "HOW THE WINNER WAS PICKED — NO FIRST-DRAFT ENTRIES", font=font(MONO_B, 22), fill=SPOT)
    steps = [
        ("44", "candidates drafted across 12 devices — delegation,"),
        ("", "self-grading, sycophancy, planning theatre, cost, more"),
        ("16", "seeded, scored 0–25 on the judge's criteria, in order"),
        ("8→4→2", "pairwise rounds; first differing criterion decides,"),
        ("", "exact ties broken by the smaller text, as ranking does"),
        ("1", "winner, re-checked head-to-head vs both runners-up"),
    ]
    y = 110
    for big, text in steps:
        if big:
            d.text((50, y), big, font=font(BOLD, 38), fill=SPOT)
        d.text((235, y + 10), text, font=font(REG, 24), fill=CREAM)
        y += 62
    card(d, (50, 500, 950, 580))
    d.text((80, 526), "Stock angles (hallucinations, refusals, confident wrong",
           font=font(MONO, 22), fill=MUTED)
    d.text((80, 552), "answers) were cut at the pool stage — the judge penalises them.",
           font=font(MONO, 22), fill=MUTED)
    img.save("shot-tournament.png")


if __name__ == "__main__":
    cover()
    shot_winner()
    shot_finalists()
    shot_tournament()
    print("wrote cover.png, shot-winner.png, shot-finalists.png, shot-tournament.png")
