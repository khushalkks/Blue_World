import os
import math
from PIL import Image, ImageDraw

os.makedirs("assets/platformer", exist_ok=True)

# 1. Warp Pipe (48x64) - Classic Mario green pipe with high-res cylindrical shading
pipe = Image.new("RGBA", (48, 64), (0, 0, 0, 0))
d = ImageDraw.Draw(pipe)

# Top collar rim (48x18)
for x in range(48):
    ratio = x / 47.0
    # Cylindrical highlight (peak around 25%)
    shine = math.sin(ratio * math.pi) ** 1.8
    r = int(20 + 35 * shine)
    g = int(140 + 105 * shine)
    b = int(40 + 40 * shine)
    d.line([(x, 2), (x, 19)], fill=(r, g, b, 255))
d.rectangle([0, 0, 47, 19], outline=(10, 70, 20, 255), width=2)
# Top inner lip shadow
d.ellipse([4, 1, 43, 6], fill=(5, 45, 15, 255))

# Pipe trunk (40x44)
for x in range(4, 44):
    ratio = (x - 4) / 39.0
    shine = math.sin(ratio * math.pi) ** 1.8
    r = int(15 + 30 * shine)
    g = int(120 + 100 * shine)
    b = int(35 + 35 * shine)
    d.line([(x, 20), (x, 63)], fill=(r, g, b, 255))
d.rectangle([4, 20, 43, 63], outline=(10, 70, 20, 255), width=2)
# Highlight stripe on collar and stem
d.line([(10, 3), (10, 18)], fill=(180, 255, 180, 200), width=2)
d.line([(12, 22), (12, 62)], fill=(180, 255, 180, 180), width=2)
pipe.save("assets/platformer/warp_pipe.png")

# 2. Checkpoint Flag (32x64)
flag = Image.new("RGBA", (32, 64), (0, 0, 0, 0))
d = ImageDraw.Draw(flag)
# Metallic Pole
d.line([(8, 4), (8, 63)], fill=(190, 200, 215, 255), width=3)
d.line([(7, 4), (7, 63)], fill=(240, 245, 255, 255), width=1)
# Finial gold ball on top
d.ellipse([5, 1, 11, 7], fill=(255, 215, 0, 255), outline=(180, 140, 0, 255))
# Base mount
d.rectangle([3, 58, 13, 63], fill=(80, 90, 105, 255), outline=(40, 45, 55, 255))
# Flag cloth (inactive state is red/orange swallowtail)
d.polygon([(9, 8), (30, 16), (22, 24), (30, 32), (9, 24)], fill=(255, 60, 60, 255), outline=(160, 20, 20, 255))
# Flag emblem star
d.polygon([(15, 14), (18, 16), (20, 20), (16, 21), (13, 17)], fill=(255, 230, 80, 255))
flag.save("assets/platformer/checkpoint_flag.png")

# 3. Cannon Blaster (48x48) - Cyber Cannon Turret
cannon = Image.new("RGBA", (48, 48), (0, 0, 0, 0))
d = ImageDraw.Draw(cannon)
# Heavy base pedestal
d.rectangle([6, 26, 41, 47], fill=(50, 60, 75, 255), outline=(25, 30, 40, 255), width=2)
# Pedestal rivets
for rx in [10, 24, 38]:
    d.ellipse([rx-2, 40, rx+2, 44], fill=(160, 175, 195, 255))
# Cannon main barrel body
d.ellipse([10, 6, 42, 38], fill=(40, 50, 65, 255), outline=(20, 25, 35, 255), width=2)
# Cannon nozzle extending left
d.polygon([(14, 12), (2, 14), (2, 30), (14, 32)], fill=(35, 42, 55, 255), outline=(15, 20, 30, 255), width=2)
# Warning glowing nozzle rim
d.rectangle([2, 14, 6, 30], fill=(255, 90, 30, 255))
# Tech glowing status light
d.ellipse([24, 18, 30, 24], fill=(0, 230, 255, 255))
cannon.save("assets/platformer/cannon_blaster.png")

# 4. Bullet Bill / Plasma Missile (40x24)
bullet = Image.new("RGBA", (40, 24), (0, 0, 0, 0))
d = ImageDraw.Draw(bullet)
# Missile body (sleek bullet shape)
d.chord([0, 2, 28, 21], 90, 270, fill=(30, 35, 45, 255), outline=(15, 20, 25, 255), width=2)
d.rectangle([14, 2, 32, 21], fill=(30, 35, 45, 255), outline=(15, 20, 25, 255), width=2)
# Thruster ring on back
d.rectangle([30, 5, 34, 18], fill=(70, 80, 95, 255), outline=(30, 35, 45, 255))
# Glowing rocket flame
d.polygon([(34, 8), (39, 11), (34, 15)], fill=(255, 140, 20, 255))
d.polygon([(34, 9), (37, 11), (34, 13)], fill=(255, 240, 100, 255))
# Angry visor eye
d.polygon([(6, 8), (14, 7), (12, 12)], fill=(255, 30, 30, 255))
d.line([(5, 7), (15, 6)], fill=(255, 220, 220, 255), width=1)
# Top shine
d.line([(8, 4), (26, 4)], fill=(120, 140, 170, 255), width=1)
bullet.save("assets/platformer/bullet_bill.png")

# 5. Power-up Magnet (32x32)
mag = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
d = ImageDraw.Draw(mag)
# Horseshoe curve
d.arc([4, 4, 27, 27], 180, 360, fill=(230, 40, 50, 255), width=6)
# Left and right legs
d.rectangle([4, 15, 10, 24], fill=(230, 40, 50, 255))
d.rectangle([21, 15, 27, 24], fill=(30, 120, 240, 255))
# Silver contact tips
d.rectangle([4, 23, 10, 27], fill=(220, 230, 240, 255))
d.rectangle([21, 23, 27, 27], fill=(220, 230, 240, 255))
# Electric spark arcs between tips
d.line([(10, 25), (14, 23), (17, 27), (21, 25)], fill=(255, 240, 50, 255), width=2)
# Sparkle sparkles
d.point([(2, 8), (30, 6), (29, 28), (2, 25)], fill=(255, 255, 255, 255))
mag.save("assets/platformer/powerup_magnet.png")

# 6. Rainbow Star (32x32)
star = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
d = ImageDraw.Draw(star)
pts = []
cx, cy = 16, 16
for i in range(10):
    ang = i * math.pi / 5 - math.pi / 2
    r = 14 if i % 2 == 0 else 6
    pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
d.polygon(pts, fill=(255, 225, 50, 255), outline=(255, 120, 0, 255), width=2)
# Glowing inner star
inner_pts = []
for i in range(10):
    ang = i * math.pi / 5 - math.pi / 2
    r = 9 if i % 2 == 0 else 4
    inner_pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
d.polygon(inner_pts, fill=(255, 255, 230, 255))
# Big anime eyes
d.ellipse([12, 12, 14, 18], fill=(30, 30, 40, 255))
d.ellipse([18, 12, 20, 18], fill=(30, 30, 40, 255))
d.point([(13, 13), (19, 13)], fill=(255, 255, 255, 255))
star.save("assets/platformer/rainbow_star.png")

print("Generated Platformer V2 assets successfully!")

