import os
import math
from PIL import Image, ImageDraw

os.makedirs("assets/textures", exist_ok=True)

# 1. Floor Tile (64x64) - High-tech facility floor with glowing cyan power conduits
floor = Image.new("RGBA", (64, 64), (28, 34, 48, 255))
d = ImageDraw.Draw(floor)
# Inner panel
d.rectangle([2, 2, 61, 61], fill=(36, 44, 62, 255), outline=(20, 26, 38, 255), width=2)
# Glowing cyan sub-surface power line in middle
d.line([(0, 32), (63, 32)], fill=(40, 180, 240, 160), width=2)
d.line([(0, 32), (63, 32)], fill=(120, 230, 255, 255), width=1)
# Corner rivets / tech pads
for x, y in [(6, 6), (57, 6), (6, 57), (57, 57)]:
    d.rectangle([x-2, y-2, x+2, y+2], fill=(65, 85, 120, 255), outline=(15, 20, 30, 255))
floor.save("assets/textures/floor_tile.png")

# 2. Wall (64x64) - Reinforced bulkhead wall with bright hazard stripes
wall = Image.new("RGBA", (64, 64), (18, 22, 32, 255))
d = ImageDraw.Draw(wall)
d.rectangle([0, 0, 63, 63], fill=(24, 30, 44, 255), outline=(60, 75, 110, 255), width=2)
# Metal panel seams
d.rectangle([6, 6, 57, 57], fill=(32, 40, 58, 255), outline=(15, 20, 30, 255), width=2)
# Top bright warning hazard bar
d.rectangle([6, 6, 57, 16], fill=(45, 55, 78, 255))
for i in range(8, 54, 8):
    d.line([(i, 6), (i+4, 16)], fill=(255, 200, 40, 255), width=2)
# Glowing wall status light
d.ellipse([30, 34, 34, 38], fill=(0, 240, 255, 255))
wall.save("assets/textures/wall.png")

# 3. Player Sprite (48x48) - High-visibility detective
player = Image.new("RGBA", (48, 48), (0, 0, 0, 0))
d = ImageDraw.Draw(player)
# Drop shadow
d.ellipse([10, 12, 38, 44], fill=(0, 0, 0, 140))
# Coat (High-tech navy/teal with neon orange shoulder straps)
d.ellipse([11, 13, 37, 39], fill=(35, 60, 85, 255), outline=(60, 110, 150, 255), width=2)
# Neon safety straps
d.line([(16, 16), (22, 32)], fill=(255, 120, 30, 255), width=2)
d.line([(32, 16), (26, 32)], fill=(255, 120, 30, 255), width=2)
# Head & hair
d.ellipse([18, 11, 30, 25], fill=(70, 50, 40, 255))
d.ellipse([19, 10, 29, 20], fill=(240, 195, 165, 255))
# Flashlight in hand
d.ellipse([32, 9, 39, 16], fill=(240, 195, 165, 255), outline=(30, 50, 70, 255))
d.rectangle([34, 3, 38, 11], fill=(120, 130, 150, 255), outline=(40, 45, 55, 255))
d.rectangle([32, 1, 40, 4], fill=(255, 255, 180, 255))
player.save("assets/textures/player.png")

# 4. Terminal CRT (48x48) - Clue 1 with bright vibrant screen
term = Image.new("RGBA", (48, 48), (0, 0, 0, 0))
d = ImageDraw.Draw(term)
# Desk table base
d.rectangle([4, 16, 44, 46], fill=(42, 50, 68, 255), outline=(25, 30, 45, 255), width=2)
# CRT monitor chassis
d.rectangle([10, 4, 38, 28], fill=(60, 72, 95, 255), outline=(30, 38, 55, 255), width=2)
# Vivid glowing Cyan CRT screen
d.rectangle([13, 7, 35, 25], fill=(10, 80, 110, 255))
d.rectangle([14, 8, 34, 24], fill=(0, 200, 240, 255))
# Screen content lines
d.line([(16, 11), (32, 11)], fill=(255, 255, 255, 255), width=1)
d.line([(16, 14), (28, 14)], fill=(180, 245, 255, 255), width=1)
d.line([(16, 17), (30, 17)], fill=(255, 255, 255, 255), width=1)
d.line([(16, 20), (24, 20)], fill=(255, 220, 80, 255), width=1) # Highlighted 7
# Keyboard
d.rectangle([14, 32, 34, 40], fill=(30, 36, 50, 255), outline=(15, 20, 30, 255))
term.save("assets/textures/terminal.png")

# 5. Whiteboard / Research Board (48x48) - Clue 2 with colorful pinned notes
wb = Image.new("RGBA", (48, 48), (0, 0, 0, 0))
d = ImageDraw.Draw(wb)
d.rectangle([2, 8, 45, 40], fill=(230, 235, 245, 255), outline=(90, 105, 135, 255), width=2)
d.rectangle([5, 11, 42, 37], fill=(245, 248, 255, 255))
# Yellow sticky note
d.rectangle([8, 14, 21, 26], fill=(255, 245, 100, 255), outline=(210, 195, 40, 255))
d.line([(10, 18), (19, 18)], fill=(30, 30, 30, 255), width=1)
d.line([(10, 22), (17, 22)], fill=(30, 30, 30, 255), width=1)
# Red circled formula
d.ellipse([24, 14, 40, 30], outline=(255, 40, 70, 255), width=2)
d.line([(28, 22), (36, 22)], fill=(20, 20, 20, 255), width=2)
# Blue diagram
d.line([(10, 32), (24, 32)], fill=(0, 140, 255, 255), width=2)
wb.save("assets/textures/whiteboard.png")

# 6. Audio Console / Specimen Rack (48x48) - Clue 3 with bright glowing oscilloscope
bio = Image.new("RGBA", (48, 48), (0, 0, 0, 0))
d = ImageDraw.Draw(bio)
d.rectangle([4, 6, 44, 44], fill=(35, 42, 58, 255), outline=(18, 24, 36, 255), width=2)
# Oscilloscope screen
d.rectangle([8, 10, 40, 24], fill=(10, 35, 25, 255), outline=(0, 255, 120, 255))
# Green audio sine wave
d.line([(10, 17), (16, 12), (22, 22), (28, 14), (34, 19), (38, 17)], fill=(50, 255, 140, 255), width=2)
# Equalizer bars
d.rectangle([8, 27, 40, 40], fill=(22, 28, 40, 255))
for idx, (h, c) in enumerate([(6, (255, 80, 80)), (10, (255, 180, 40)), (5, (255, 220, 40)), (12, (0, 255, 160))]):
    x = 11 + idx * 7
    d.rectangle([x, 38 - h, x + 4, 38], fill=(c[0], c[1], c[2], 255))
bio.save("assets/textures/bio_shelf.png")

# 7. Security Keypad Wall Unit (32x32)
pad = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
d = ImageDraw.Draw(pad)
d.rectangle([6, 4, 26, 28], fill=(48, 56, 75, 255), outline=(25, 30, 45, 255), width=2)
# Bright LED screen
d.rectangle([9, 7, 23, 12], fill=(0, 230, 255, 255))
# Buttons
for by in [14, 18, 22]:
    for bx in [9, 14, 19]:
        d.rectangle([bx, by, bx+3, by+2], fill=(80, 95, 125, 255))
pad.save("assets/textures/keypad.png")

# 8. Blast Door Closed (64x64) - Bright hazard stripes and glowing red lights
door_c = Image.new("RGBA", (64, 64), (18, 22, 32, 255))
d = ImageDraw.Draw(door_c)
d.rectangle([0, 0, 63, 63], fill=(30, 36, 50, 255), outline=(70, 85, 120, 255), width=2)
# Door leaves
d.rectangle([8, 8, 30, 55], fill=(45, 54, 75, 255), outline=(20, 25, 35, 255), width=1)
d.rectangle([33, 8, 55, 55], fill=(45, 54, 75, 255), outline=(20, 25, 35, 255), width=1)
# Bright hazard chevrons
for ix in range(8, 54, 8):
    d.polygon([(ix, 28), (ix+4, 28), (ix+2, 36), (ix-2, 36)], fill=(255, 210, 30, 255))
# Center lock
d.rectangle([27, 23, 36, 41], fill=(85, 100, 130, 255), outline=(20, 25, 35, 255))
# Glowing Red warning lights
d.ellipse([13, 11, 19, 17], fill=(255, 40, 50, 255))
d.ellipse([44, 11, 50, 17], fill=(255, 40, 50, 255))
door_c.save("assets/textures/blast_door_closed.png")

# 9. Blast Door Open (64x64) - Bright green access lights
door_o = Image.new("RGBA", (64, 64), (18, 22, 32, 255))
d = ImageDraw.Draw(door_o)
d.rectangle([12, 4, 51, 63], fill=(12, 16, 24, 255))
# Glowing pathway light in corridor
d.line([(31, 6), (31, 63)], fill=(0, 255, 160, 180), width=3)
d.rectangle([2, 8, 12, 55], fill=(50, 60, 82, 255), outline=(20, 25, 35, 255))
d.rectangle([51, 8, 61, 55], fill=(50, 60, 82, 255), outline=(20, 25, 35, 255))
d.rectangle([0, 0, 63, 63], fill=None, outline=(70, 85, 120, 255), width=2)
# Glowing Green lights
d.ellipse([13, 11, 19, 17], fill=(30, 255, 120, 255))
d.ellipse([44, 11, 50, 17], fill=(30, 255, 120, 255))
door_o.save("assets/textures/blast_door_open.png")

# 10. Round Light Gradient (256x256)
light_round = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
cx, cy = 128, 128
max_r = 124.0
pixels = light_round.load()
for y in range(256):
    for x in range(256):
        dist = math.hypot(x - cx, y - cy)
        if dist < max_r:
            t = dist / max_r
            alpha = max(0.0, min(1.0, 1.0 - (3.0 * t**2 - 2.0 * t**3)))
            val = int(alpha * 255)
            pixels[x, y] = (255, 255, 255, val)
light_round.save("assets/textures/light_round.png")

# 11. Flashlight Cone Light (256x256)
light_cone = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
cx, cy = 128, 240
pixels = light_cone.load()
for y in range(256):
    for x in range(256):
        dx = x - cx
        dy = y - cy
        dist = math.hypot(dx, dy)
        if dist > 0 and dist < 230 and dy < 0:
            angle = math.atan2(dx, -dy)
            max_angle = math.radians(38)
            if abs(angle) < max_angle:
                dist_factor = 1.0 - (dist / 230.0)
                angle_factor = math.cos((angle / max_angle) * (math.pi / 2.0))
                intensity = dist_factor * angle_factor
                val = int(max(0.0, min(1.0, intensity)) * 255)
                pixels[x, y] = (255, 252, 230, val)
light_cone.save("assets/textures/light_cone.png")

print("Vibrant textures updated successfully.")
