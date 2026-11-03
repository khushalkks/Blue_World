import os
import math
from PIL import Image, ImageDraw

os.makedirs("assets/platformer", exist_ok=True)

# 1. Player Sprite (48x48) - Mario-style charismatic Blue Runner
# Vibrant blue hero with red cap, white gloves, running sneakers!
player = Image.new("RGBA", (48, 48), (0, 0, 0, 0))
d = ImageDraw.Draw(player)
# Cap & Brim
d.rectangle([14, 4, 32, 14], fill=(235, 45, 55, 255))
d.rectangle([20, 11, 38, 15], fill=(210, 30, 40, 255))
# Face & Nose
d.rectangle([16, 14, 32, 24], fill=(255, 215, 175, 255))
d.ellipse([27, 16, 35, 23], fill=(255, 200, 160, 255), outline=(210, 150, 120, 255))
# Big cartoon eyes
d.ellipse([23, 15, 27, 21], fill=(255, 255, 255, 255))
d.ellipse([25, 16, 27, 20], fill=(20, 60, 180, 255))
# Mustache
d.rectangle([21, 21, 34, 25], fill=(50, 30, 20, 255))
# Blue Overalls / Body
d.rectangle([14, 24, 34, 38], fill=(30, 110, 240, 255), outline=(15, 60, 160, 255), width=1)
# Red Shirt under overalls
d.rectangle([10, 25, 15, 34], fill=(235, 45, 55, 255))
d.rectangle([33, 25, 38, 34], fill=(235, 45, 55, 255))
# Yellow buttons on overalls
d.ellipse([18, 27, 21, 30], fill=(255, 220, 30, 255))
d.ellipse([27, 27, 30, 30], fill=(255, 220, 30, 255))
# White Gloves
d.ellipse([8, 30, 15, 37], fill=(250, 250, 250, 255), outline=(180, 180, 180, 255))
d.ellipse([33, 30, 40, 37], fill=(250, 250, 250, 255), outline=(180, 180, 180, 255))
# Red running shoes
d.rectangle([12, 38, 21, 46], fill=(180, 40, 40, 255), outline=(100, 20, 20, 255))
d.rectangle([27, 38, 36, 46], fill=(180, 40, 40, 255), outline=(100, 20, 20, 255))
d.rectangle([11, 43, 22, 46], fill=(240, 240, 240, 255))
d.rectangle([26, 43, 37, 46], fill=(240, 240, 240, 255))
player.save("assets/platformer/player.png")

# 2. Goomba-style Enemy (40x40) - Angry Orange/Brown Mushroom Monster
enemy = Image.new("RGBA", (40, 40), (0, 0, 0, 0))
d = ImageDraw.Draw(enemy)
# Cap
d.ellipse([4, 4, 36, 28], fill=(190, 80, 35, 255), outline=(120, 40, 15, 255), width=2)
# Cap spots
d.ellipse([10, 8, 16, 14], fill=(240, 130, 70, 255))
d.ellipse([24, 8, 30, 14], fill=(240, 130, 70, 255))
# Stem / Body
d.rectangle([10, 22, 30, 34], fill=(245, 225, 190, 255), outline=(160, 140, 110, 255))
# Angry Eyes (triangular eyebrows)
d.ellipse([12, 22, 18, 28], fill=(255, 255, 255, 255))
d.ellipse([22, 22, 28, 28], fill=(255, 255, 255, 255))
d.ellipse([15, 24, 18, 28], fill=(20, 20, 20, 255))
d.ellipse([22, 24, 25, 28], fill=(20, 20, 20, 255))
d.line([(11, 21), (18, 24)], fill=(100, 30, 10, 255), width=2)
d.line([(29, 21), (22, 24)], fill=(100, 30, 10, 255), width=2)
# Little feet
d.ellipse([4, 31, 17, 39], fill=(60, 30, 20, 255))
d.ellipse([23, 31, 36, 39], fill=(60, 30, 20, 255))
enemy.save("assets/platformer/enemy_goomba.png")

# 3. Flying Bat / Beetle Enemy (44x36)
flyer = Image.new("RGBA", (44, 36), (0, 0, 0, 0))
d = ImageDraw.Draw(flyer)
# Wings
d.polygon([(4, 18), (14, 6), (18, 18)], fill=(180, 50, 220, 255), outline=(120, 20, 160, 255))
d.polygon([(40, 18), (30, 6), (26, 18)], fill=(180, 50, 220, 255), outline=(120, 20, 160, 255))
# Body
d.ellipse([14, 10, 30, 30], fill=(70, 25, 110, 255), outline=(40, 10, 70, 255), width=2)
# Glowing yellow eyes
d.ellipse([17, 16, 21, 22], fill=(255, 230, 40, 255))
d.ellipse([23, 16, 27, 22], fill=(255, 230, 40, 255))
d.ellipse([19, 18, 21, 21], fill=(200, 20, 20, 255))
d.ellipse([23, 18, 25, 21], fill=(200, 20, 20, 255))
# Little fangs
d.polygon([(18, 26), (20, 29), (21, 26)], fill=(255, 255, 255, 255))
d.polygon([(23, 26), (24, 29), (26, 26)], fill=(255, 255, 255, 255))
flyer.save("assets/platformer/enemy_flyer.png")

# 4. Boss Monster (72x72) - Big Spiky Bowser-style Boss King
boss = Image.new("RGBA", (72, 72), (0, 0, 0, 0))
d = ImageDraw.Draw(boss)
# Shell / Back Spikes
d.ellipse([10, 16, 62, 64], fill=(40, 130, 60, 255), outline=(20, 70, 30, 255), width=3)
# Shell rim with yellow plates
d.rectangle([8, 38, 64, 46], fill=(230, 190, 40, 255), outline=(150, 120, 20, 255), width=2)
# Horns & Crown
d.polygon([(20, 16), (12, 2), (28, 12)], fill=(240, 220, 170, 255), outline=(140, 120, 80, 255))
d.polygon([(52, 16), (60, 2), (44, 12)], fill=(240, 220, 170, 255), outline=(140, 120, 80, 255))
d.polygon([(28, 14), (36, 4), (44, 14)], fill=(255, 215, 0, 255), outline=(180, 140, 0, 255))
# Fierce Red Head
d.ellipse([20, 16, 52, 44], fill=(220, 50, 40, 255), outline=(140, 20, 15, 255), width=2)
# Glowing angry eyes
d.ellipse([26, 24, 34, 32], fill=(255, 255, 255, 255))
d.ellipse([38, 24, 46, 32], fill=(255, 255, 255, 255))
d.ellipse([30, 26, 34, 31], fill=(20, 20, 20, 255))
d.ellipse([38, 26, 42, 31], fill=(20, 20, 20, 255))
d.line([(24, 23), (35, 26)], fill=(50, 10, 10, 255), width=2)
d.line([(48, 23), (37, 26)], fill=(50, 10, 10, 255), width=2)
# Big Snout & Sharp Teeth
d.ellipse([24, 32, 48, 44], fill=(245, 185, 120, 255))
for tx in range(27, 45, 5):
    d.polygon([(tx, 40), (tx+2, 44), (tx+4, 40)], fill=(255, 255, 255, 255))
# Feet & Claws
d.ellipse([10, 56, 28, 68], fill=(220, 50, 40, 255))
d.ellipse([44, 56, 62, 68], fill=(220, 50, 40, 255))
boss.save("assets/platformer/boss.png")

# 5. Grass Tile (48x48) - Lush Mario-style grass & rich dirt
grass = Image.new("RGBA", (48, 48), (140, 85, 45, 255))
d = ImageDraw.Draw(grass)
# Rich dirt texture specks
for x, y in [(8, 24), (22, 36), (38, 28), (16, 42), (32, 40)]:
    d.rectangle([x, y, x+3, y+2], fill=(110, 65, 30, 255))
    d.rectangle([x+10, y-6, x+12, y-5], fill=(170, 110, 60, 255))
# Bright green grass layer with overhang drops
d.rectangle([0, 0, 47, 12], fill=(70, 200, 50, 255))
d.rectangle([0, 0, 47, 3], fill=(115, 235, 85, 255)) # highlight
# Grass blades / drops
for gx in range(0, 48, 8):
    d.polygon([(gx, 12), (gx+4, 18), (gx+8, 12)], fill=(55, 175, 40, 255))
# Outline
d.rectangle([0, 0, 47, 47], outline=(40, 25, 15, 255), width=1)
grass.save("assets/platformer/tile_grass.png")

# 6. Dirt Tile (48x48)
dirt = Image.new("RGBA", (48, 48), (140, 85, 45, 255))
d = ImageDraw.Draw(dirt)
for x, y in [(6, 8), (24, 14), (38, 6), (12, 28), (28, 38), (8, 40), (36, 32)]:
    d.rectangle([x, y, x+4, y+3], fill=(105, 60, 25, 255))
    d.rectangle([x+6, y+4, x+9, y+6], fill=(175, 115, 65, 255))
d.rectangle([0, 0, 47, 47], outline=(40, 25, 15, 255), width=1)
dirt.save("assets/platformer/tile_dirt.png")

# 7. Stone / Castle Block (48x48) - Deep fortress stone
stone = Image.new("RGBA", (48, 48), (50, 58, 75, 255))
d = ImageDraw.Draw(stone)
d.rectangle([2, 2, 45, 45], fill=(62, 72, 92, 255), outline=(35, 40, 55, 255), width=2)
d.line([(2, 24), (45, 24)], fill=(35, 40, 55, 255), width=2)
d.line([(24, 2), (24, 23)], fill=(35, 40, 55, 255), width=2)
d.line([(12, 25), (12, 45)], fill=(35, 40, 55, 255), width=2)
d.line([(36, 25), (36, 45)], fill=(35, 40, 55, 255), width=2)
stone.save("assets/platformer/tile_stone.png")

# 8. Lava / Acid Hazard (48x48)
lava = Image.new("RGBA", (48, 48), (240, 80, 20, 255))
d = ImageDraw.Draw(lava)
d.rectangle([0, 0, 47, 8], fill=(255, 210, 40, 255))
for lx in range(0, 48, 12):
    d.ellipse([lx, 4, lx+10, 16], fill=(255, 150, 30, 255))
for bx, by in [(8, 22), (26, 32), (38, 20), (16, 38)]:
    d.ellipse([bx, by, bx+8, by+8], fill=(255, 230, 80, 255), outline=(200, 50, 10, 255))
lava.save("assets/platformer/tile_lava.png")

# 9. Question Block (?) (48x48) - Bright golden mystery block
qblock = Image.new("RGBA", (48, 48), (235, 160, 20, 255))
d = ImageDraw.Draw(qblock)
d.rectangle([2, 2, 45, 45], fill=(255, 185, 30, 255), outline=(170, 95, 10, 255), width=2)
d.rectangle([6, 6, 41, 41], fill=(250, 195, 45, 255), outline=(255, 230, 100, 255), width=2)
# Corner rivets
for rx, ry in [(8, 8), (37, 8), (8, 37), (37, 37)]:
    d.rectangle([rx-1, ry-1, rx+2, ry+2], fill=(130, 70, 10, 255))
# Bold White Question Mark with drop shadow
d.text((17, 10), "?", fill=(70, 35, 5, 255))
# Draw clear bold '?' with shapes
d.ellipse([18, 11, 30, 22], outline=(255, 255, 255, 255), width=3)
d.line([(24, 22), (24, 27)], fill=(255, 255, 255, 255), width=3)
d.rectangle([23, 31, 26, 34], fill=(255, 255, 255, 255))
qblock.save("assets/platformer/block_question.png")

# 10. Brick Block (48x48) - Classic breakable brown brick
brick = Image.new("RGBA", (48, 48), (175, 75, 45, 255))
d = ImageDraw.Draw(brick)
d.rectangle([0, 0, 47, 47], outline=(80, 30, 20, 255), width=2)
d.line([(0, 16), (47, 16)], fill=(80, 30, 20, 255), width=2)
d.line([(0, 32), (47, 32)], fill=(80, 30, 20, 255), width=2)
d.line([(24, 0), (24, 16)], fill=(80, 30, 20, 255), width=2)
d.line([(12, 16), (12, 32)], fill=(80, 30, 20, 255), width=2)
d.line([(36, 16), (36, 32)], fill=(80, 30, 20, 255), width=2)
d.line([(24, 32), (24, 47)], fill=(80, 30, 20, 255), width=2)
brick.save("assets/platformer/block_brick.png")

# 11. Empty Solid Block (48x48) - Brown steel block after hitting
empty_b = Image.new("RGBA", (48, 48), (120, 105, 95, 255))
d = ImageDraw.Draw(empty_b)
d.rectangle([2, 2, 45, 45], fill=(145, 130, 120, 255), outline=(80, 65, 55, 255), width=2)
for rx, ry in [(7, 7), (39, 7), (7, 39), (39, 39)]:
    d.rectangle([rx-1, ry-1, rx+2, ry+2], fill=(60, 50, 45, 255))
empty_b.save("assets/platformer/block_empty.png")

# 12. Gold Coin (32x32)
coin = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
d = ImageDraw.Draw(coin)
d.ellipse([4, 2, 27, 29], fill=(255, 215, 0, 255), outline=(190, 130, 10, 255), width=2)
d.ellipse([9, 5, 22, 26], fill=(255, 235, 70, 255), outline=(215, 165, 20, 255), width=1)
# Center vertical star shine
d.rectangle([14, 8, 17, 23], fill=(255, 255, 210, 255))
coin.save("assets/platformer/coin.png")

# 13. Spring Pad (36x24)
spring = Image.new("RGBA", (36, 24), (0, 0, 0, 0))
d = ImageDraw.Draw(spring)
# Red base
d.rectangle([4, 18, 31, 23], fill=(210, 40, 40, 255), outline=(120, 20, 20, 255), width=1)
# Yellow coiled spring
d.line([(8, 18), (14, 12), (22, 18), (28, 12)], fill=(255, 215, 30, 255), width=3)
d.line([(8, 12), (14, 6), (22, 12), (28, 6)], fill=(255, 215, 30, 255), width=3)
# Bright Green top plate
d.rectangle([2, 2, 33, 7], fill=(50, 220, 80, 255), outline=(20, 120, 40, 255), width=1)
spring.save("assets/platformer/spring.png")

# 14. Danger Spike (32x32)
spike = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
d = ImageDraw.Draw(spike)
d.polygon([(2, 30), (8, 4), (15, 30)], fill=(180, 190, 205, 255), outline=(90, 100, 120, 255), width=1)
d.polygon([(16, 30), (23, 4), (30, 30)], fill=(180, 190, 205, 255), outline=(90, 100, 120, 255), width=1)
d.line([(8, 4), (8, 30)], fill=(240, 245, 255, 255), width=1)
d.line([(23, 4), (23, 30)], fill=(240, 245, 255, 255), width=1)
spike.save("assets/platformer/spike.png")

# 15. Victory Flagpole (40x96)
flag = Image.new("RGBA", (40, 96), (0, 0, 0, 0))
d = ImageDraw.Draw(flag)
# Green base block
d.rectangle([10, 84, 30, 95], fill=(50, 180, 60, 255), outline=(20, 90, 30, 255), width=2)
# Golden top ball
d.ellipse([16, 2, 24, 10], fill=(255, 215, 0, 255), outline=(180, 140, 10, 255), width=1)
# Silver pole
d.rectangle([18, 10, 22, 84], fill=(220, 230, 245, 255), outline=(130, 140, 160, 255), width=1)
# Bright red pennant flag with star
d.polygon([(22, 12), (38, 22), (22, 32)], fill=(235, 45, 55, 255), outline=(160, 20, 30, 255))
d.ellipse([(24, 18), (28, 24)], fill=(255, 225, 40, 255))
flag.save("assets/platformer/flagpole.png")

# 16. Heart Icon (24x24) for Lives
heart = Image.new("RGBA", (24, 24), (0, 0, 0, 0))
d = ImageDraw.Draw(heart)
d.polygon([(12, 21), (2, 9), (4, 4), (10, 4), (12, 7), (14, 4), (20, 4), (22, 9)], fill=(240, 45, 70, 255), outline=(160, 15, 35, 255), width=1)
d.ellipse([5, 5, 8, 8], fill=(255, 160, 180, 255))
heart.save("assets/platformer/heart.png")

# 17. Cloud (96x48) - Retro fluffy sky cloud
cloud = Image.new("RGBA", (96, 48), (0, 0, 0, 0))
d = ImageDraw.Draw(cloud)
d.ellipse([8, 16, 40, 44], fill=(255, 255, 255, 230))
d.ellipse([28, 6, 68, 44], fill=(255, 255, 255, 240))
d.ellipse([56, 14, 88, 44], fill=(255, 255, 255, 230))
d.rectangle([18, 24, 78, 44], fill=(255, 255, 255, 240))
cloud.save("assets/platformer/cloud.png")

print("All Mario-style platformer sprites successfully created in assets/platformer/")

