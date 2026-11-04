import os
import math
from PIL import Image, ImageDraw

os.makedirs("assets/platformer", exist_ok=True)

# 1. Falling / Crumbling Platform (64x32)
fall_p = Image.new("RGBA", (64, 32), (0, 0, 0, 0))
d = ImageDraw.Draw(fall_p)
d.rectangle([2, 2, 61, 29], fill=(130, 75, 55, 255), outline=(70, 35, 25, 255), width=2)
# Crack lines
d.line([(8, 4), (16, 14), (12, 28)], fill=(40, 20, 15, 255), width=2)
d.line([(28, 4), (34, 18), (42, 12), (48, 28)], fill=(40, 20, 15, 255), width=2)
d.line([(48, 12), (58, 20)], fill=(40, 20, 15, 255), width=2)
# Warning glowing orange fracture lines
d.line([(16, 14), (20, 22)], fill=(255, 140, 30, 255), width=1)
d.line([(34, 18), (40, 24)], fill=(255, 140, 30, 255), width=1)
fall_p.save("assets/platformer/falling_platform.png")

# 2. Moving Platform (80x28) - High-tech metallic hover platform
move_p = Image.new("RGBA", (80, 28), (0, 0, 0, 0))
d = ImageDraw.Draw(move_p)
d.rectangle([2, 2, 77, 25], fill=(55, 70, 95, 255), outline=(25, 35, 50, 255), width=2)
# Top grip plate
d.rectangle([6, 4, 73, 10], fill=(85, 105, 140, 255))
# Glowing cyan energy core strip
d.rectangle([10, 14, 69, 18], fill=(0, 220, 255, 255))
d.line([(14, 16), (65, 16)], fill=(200, 255, 255, 255), width=1)
# Thruster nozzles
for tx in [14, 38, 62]:
    d.polygon([(tx-4, 25), (tx+4, 25), (tx, 27)], fill=(255, 180, 40, 255))
move_p.save("assets/platformer/moving_platform.png")

# 3. Thwomp Slammer Trap (56x56) - Menacing spiky stone block
thwomp = Image.new("RGBA", (56, 56), (0, 0, 0, 0))
d = ImageDraw.Draw(thwomp)
# Main body
d.rectangle([6, 6, 49, 49], fill=(90, 100, 115, 255), outline=(45, 50, 60, 255), width=3)
# Edge spikes
for i in range(10, 48, 12):
    # Top spikes
    d.polygon([(i, 6), (i+6, 0), (i+12, 6)], fill=(160, 175, 195, 255), outline=(45, 50, 60, 255))
    # Bottom spikes
    d.polygon([(i, 49), (i+6, 55), (i+12, 49)], fill=(160, 175, 195, 255), outline=(45, 50, 60, 255))
    # Left spikes
    d.polygon([(6, i), (0, i+6), (6, i+12)], fill=(160, 175, 195, 255), outline=(45, 50, 60, 255))
    # Right spikes
    d.polygon([(49, i), (55, i+6), (49, i+12)], fill=(160, 175, 195, 255), outline=(45, 50, 60, 255))
# Angry glowing eyes
d.polygon([(14, 20), (24, 24), (16, 28)], fill=(255, 40, 40, 255))
d.polygon([(41, 20), (31, 24), (39, 28)], fill=(255, 40, 40, 255))
d.ellipse([18, 22, 22, 26], fill=(255, 255, 255, 255))
d.ellipse([33, 22, 37, 26], fill=(255, 255, 255, 255))
# Gritted teeth
d.rectangle([16, 34, 39, 42], fill=(220, 225, 235, 255), outline=(30, 30, 40, 255), width=2)
for x in range(20, 36, 4):
    d.line([(x, 34), (x, 42)], fill=(30, 30, 40, 255), width=1)
thwomp.save("assets/platformer/thwomp.png")

# 4. Fire Orb / Plasma Ball (24x24)
fire = Image.new("RGBA", (24, 24), (0, 0, 0, 0))
d = ImageDraw.Draw(fire)
d.ellipse([1, 1, 22, 22], fill=(255, 60, 10, 200))
d.ellipse([4, 4, 19, 19], fill=(255, 160, 20, 240))
d.ellipse([7, 7, 16, 16], fill=(255, 240, 80, 255))
d.ellipse([9, 9, 14, 14], fill=(255, 255, 220, 255))
fire.save("assets/platformer/fire_orb.png")

# 5. Power-Up Star (32x32) - Glowing Rainbow Fire/Power Star
star = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
d = ImageDraw.Draw(star)
points = [
    (16, 1), (20, 11), (31, 12), (23, 20),
    (26, 31), (16, 25), (6, 31), (9, 20),
    (1, 12), (12, 11)
]
d.polygon(points, fill=(255, 230, 30, 255), outline=(220, 140, 10, 255), width=2)
# Cute eyes
d.ellipse([12, 12, 15, 18], fill=(30, 30, 40, 255))
d.ellipse([17, 12, 20, 18], fill=(30, 30, 40, 255))
d.ellipse([13, 13, 14, 15], fill=(255, 255, 255, 255))
d.ellipse([18, 13, 19, 15], fill=(255, 255, 255, 255))
star.save("assets/platformer/powerup_star.png")

print("New suspenseful dynamic platformer sprites generated!")
