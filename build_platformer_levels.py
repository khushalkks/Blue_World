import os

def create_platform(name, x, y, w, h, tex_res):
    return f"""
[node name="{name}" type="StaticBody2D" parent="Platforms"]
position = Vector2({x}, {y})
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/{name}"]
texture_repeat = 2
texture = ExtResource("{tex_res}")
region_enabled = true
region_rect = Rect2(0, 0, {w}, {h})

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/{name}"]
shape = SubResource("RectangleShape2D_p_{w}_{h}")
"""

# Let's write the generator
def build_level_1():
    content = """[gd_scene load_steps=15 format=3]

[ext_resource type="Script" path="res://scripts/levels/platform_level_controller.gd" id="1_ctrl"]
[ext_resource type="Texture2D" path="res://assets/platformer/tile_grass.png" id="2_grass"]
[ext_resource type="Texture2D" path="res://assets/platformer/tile_dirt.png" id="3_dirt"]
[ext_resource type="Texture2D" path="res://assets/platformer/block_brick.png" id="4_brick"]
[ext_resource type="Texture2D" path="res://assets/platformer/cloud.png" id="5_cloud"]
[ext_resource type="PackedScene" path="res://scenes/player/platform_player.tscn" id="6_player"]
[ext_resource type="PackedScene" path="res://scenes/objects/coin.tscn" id="7_coin"]
[ext_resource type="PackedScene" path="res://scenes/objects/question_block.tscn" id="8_qblock"]
[ext_resource type="PackedScene" path="res://scenes/objects/enemy_goomba.tscn" id="9_goomba"]
[ext_resource type="PackedScene" path="res://scenes/objects/spring_pad.tscn" id="10_spring"]
[ext_resource type="PackedScene" path="res://scenes/objects/goal_flag.tscn" id="11_flag"]
[ext_resource type="PackedScene" path="res://scenes/ui/platform_hud.tscn" id="12_hud"]

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_700_96"]
size = Vector2(700, 96)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_540_96"]
size = Vector2(540, 96)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_180_48"]
size = Vector2(180, 48)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_160_96"]
size = Vector2(160, 96)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_240_48"]
size = Vector2(240, 48)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_620_96"]
size = Vector2(620, 96)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_96_48"]
size = Vector2(96, 48)

[node name="PlatformLevel1" type="Node2D"]
script = ExtResource("1_ctrl")
level_number = 1

[node name="Sky" type="CanvasLayer" parent="."]
layer = -100

[node name="ColorRect" type="ColorRect" parent="Sky"]
anchors_preset = 15
anchor_right = 1.0
anchor_bottom = 1.0
color = Color(0.35, 0.68, 0.98, 1)

[node name="Clouds" type="Node2D" parent="."]
z_index = -50

[node name="Cloud1" type="Sprite2D" parent="Clouds"]
position = Vector2(200, 100)
texture = ExtResource("5_cloud")

[node name="Cloud2" type="Sprite2D" parent="Clouds"]
position = Vector2(650, 70)
texture = ExtResource("5_cloud")

[node name="Cloud3" type="Sprite2D" parent="Clouds"]
position = Vector2(1100, 120)
texture = ExtResource("5_cloud")

[node name="Cloud4" type="Sprite2D" parent="Clouds"]
position = Vector2(1600, 80)
texture = ExtResource("5_cloud")

[node name="Cloud5" type="Sprite2D" parent="Clouds"]
position = Vector2(2100, 110)
texture = ExtResource("5_cloud")

[node name="Platforms" type="Node2D" parent="."]

[node name="Ground1" type="StaticBody2D" parent="Platforms"]
position = Vector2(350, 480)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/Ground1"]
texture_repeat = 2
texture = ExtResource("2_grass")
region_enabled = true
region_rect = Rect2(0, 0, 700, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/Ground1"]
shape = SubResource("RectangleShape2D_p_700_96")

[node name="Ground2" type="StaticBody2D" parent="Platforms"]
position = Vector2(1100, 480)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/Ground2"]
texture_repeat = 2
texture = ExtResource("2_grass")
region_enabled = true
region_rect = Rect2(0, 0, 540, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/Ground2"]
shape = SubResource("RectangleShape2D_p_540_96")

[node name="Step1" type="StaticBody2D" parent="Platforms"]
position = Vector2(1160, 350)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/Step1"]
texture_repeat = 2
texture = ExtResource("4_brick")
region_enabled = true
region_rect = Rect2(0, 0, 180, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/Step1"]
shape = SubResource("RectangleShape2D_p_180_48")

[node name="SpringIsland" type="StaticBody2D" parent="Platforms"]
position = Vector2(1540, 480)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/SpringIsland"]
texture_repeat = 2
texture = ExtResource("2_grass")
region_enabled = true
region_rect = Rect2(0, 0, 160, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/SpringIsland"]
shape = SubResource("RectangleShape2D_p_160_96")

[node name="SkyBonus" type="StaticBody2D" parent="Platforms"]
position = Vector2(1740, 220)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/SkyBonus"]
texture_repeat = 2
texture = ExtResource("2_grass")
region_enabled = true
region_rect = Rect2(0, 0, 240, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/SkyBonus"]
shape = SubResource("RectangleShape2D_p_240_48")

[node name="GroundEnd" type="StaticBody2D" parent="Platforms"]
position = Vector2(2120, 480)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/GroundEnd"]
texture_repeat = 2
texture = ExtResource("2_grass")
region_enabled = true
region_rect = Rect2(0, 0, 620, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/GroundEnd"]
shape = SubResource("RectangleShape2D_p_620_96")

[node name="QBlock1" parent="." instance=ExtResource("8_qblock")]
position = Vector2(400, 340)

[node name="QBlock2" parent="." instance=ExtResource("8_qblock")]
position = Vector2(470, 340)

[node name="QBlock3" parent="." instance=ExtResource("8_qblock")]
position = Vector2(540, 340)

[node name="SpringPad" parent="." instance=ExtResource("10_spring")]
position = Vector2(1540, 420)

[node name="Coins" type="Node2D" parent="."]

[node name="Coin1" parent="Coins" instance=ExtResource("7_coin")]
position = Vector2(280, 390)

[node name="Coin2" parent="Coins" instance=ExtResource("7_coin")]
position = Vector2(330, 370)

[node name="Coin3" parent="Coins" instance=ExtResource("7_coin")]
position = Vector2(760, 330)

[node name="Coin4" parent="Coins" instance=ExtResource("7_coin")]
position = Vector2(1100, 290)

[node name="Coin5" parent="Coins" instance=ExtResource("7_coin")]
position = Vector2(1160, 290)

[node name="Coin6" parent="Coins" instance=ExtResource("7_coin")]
position = Vector2(1220, 290)

[node name="Coin7" parent="Coins" instance=ExtResource("7_coin")]
position = Vector2(1660, 160)

[node name="Coin8" parent="Coins" instance=ExtResource("7_coin")]
position = Vector2(1720, 160)

[node name="Coin9" parent="Coins" instance=ExtResource("7_coin")]
position = Vector2(1780, 160)

[node name="Coin10" parent="Coins" instance=ExtResource("7_coin")]
position = Vector2(1840, 160)

[node name="Enemies" type="Node2D" parent="."]

[node name="Goomba1" parent="Enemies" instance=ExtResource("9_goomba")]
position = Vector2(520, 410)

[node name="Goomba2" parent="Enemies" instance=ExtResource("9_goomba")]
position = Vector2(980, 410)

[node name="Goomba3" parent="Enemies" instance=ExtResource("9_goomba")]
position = Vector2(1280, 410)

[node name="Goomba4" parent="Enemies" instance=ExtResource("9_goomba")]
position = Vector2(1980, 410)

[node name="GoalFlag" parent="." instance=ExtResource("11_flag")]
position = Vector2(2340, 388)

[node name="Player" parent="." instance=ExtResource("6_player")]
position = Vector2(80, 400)

[node name="PlatformHUD" parent="." instance=ExtResource("12_hud")]
"""
    with open("scenes/levels/platform_level_1.tscn", "w", encoding="utf-8") as f:
        f.write(content.strip())
    print("Level 1 created successfully!")

def build_level_2():
    content = """[gd_scene load_steps=16 format=3]

[ext_resource type="Script" path="res://scripts/levels/platform_level_controller.gd" id="1_ctrl"]
[ext_resource type="Texture2D" path="res://assets/platformer/tile_dirt.png" id="2_dirt"]
[ext_resource type="Texture2D" path="res://assets/platformer/tile_stone.png" id="3_stone"]
[ext_resource type="Texture2D" path="res://assets/platformer/block_brick.png" id="4_brick"]
[ext_resource type="PackedScene" path="res://scenes/player/platform_player.tscn" id="5_player"]
[ext_resource type="PackedScene" path="res://scenes/objects/coin.tscn" id="6_coin"]
[ext_resource type="PackedScene" path="res://scenes/objects/question_block.tscn" id="7_qblock"]
[ext_resource type="PackedScene" path="res://scenes/objects/enemy_goomba.tscn" id="8_goomba"]
[ext_resource type="PackedScene" path="res://scenes/objects/enemy_flyer.tscn" id="9_flyer"]
[ext_resource type="PackedScene" path="res://scenes/objects/spring_pad.tscn" id="10_spring"]
[ext_resource type="PackedScene" path="res://scenes/objects/spikes.tscn" id="11_spike"]
[ext_resource type="PackedScene" path="res://scenes/objects/goal_flag.tscn" id="12_flag"]
[ext_resource type="PackedScene" path="res://scenes/ui/platform_hud.tscn" id="13_hud"]

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_400_96"]
size = Vector2(400, 96)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_220_48"]
size = Vector2(220, 48)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_320_96"]
size = Vector2(320, 96)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_140_48"]
size = Vector2(140, 48)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_500_96"]
size = Vector2(500, 96)

[node name="PlatformLevel2" type="Node2D"]
script = ExtResource("1_ctrl")
level_number = 2

[node name="CaveBackground" type="CanvasLayer" parent="."]
layer = -100

[node name="ColorRect" type="ColorRect" parent="CaveBackground"]
anchors_preset = 15
anchor_right = 1.0
anchor_bottom = 1.0
color = Color(0.08, 0.11, 0.2, 1)

[node name="Platforms" type="Node2D" parent="."]

[node name="StartLedge" type="StaticBody2D" parent="Platforms"]
position = Vector2(200, 480)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/StartLedge"]
texture_repeat = 2
texture = ExtResource("3_stone")
region_enabled = true
region_rect = Rect2(0, 0, 400, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/StartLedge"]
shape = SubResource("RectangleShape2D_p_400_96")

[node name="Floating1" type="StaticBody2D" parent="Platforms"]
position = Vector2(560, 380)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/Floating1"]
texture_repeat = 2
texture = ExtResource("2_dirt")
region_enabled = true
region_rect = Rect2(0, 0, 220, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/Floating1"]
shape = SubResource("RectangleShape2D_p_220_48")

[node name="SpikePitFloor" type="StaticBody2D" parent="Platforms"]
position = Vector2(980, 500)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/SpikePitFloor"]
texture_repeat = 2
texture = ExtResource("3_stone")
region_enabled = true
region_rect = Rect2(0, 0, 320, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/SpikePitFloor"]
shape = SubResource("RectangleShape2D_p_320_96")

[node name="HighPlatform1" type="StaticBody2D" parent="Platforms"]
position = Vector2(980, 280)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/HighPlatform1"]
texture_repeat = 2
texture = ExtResource("4_brick")
region_enabled = true
region_rect = Rect2(0, 0, 220, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/HighPlatform1"]
shape = SubResource("RectangleShape2D_p_220_48")

[node name="PillarJump" type="StaticBody2D" parent="Platforms"]
position = Vector2(1360, 380)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/PillarJump"]
texture_repeat = 2
texture = ExtResource("2_dirt")
region_enabled = true
region_rect = Rect2(0, 0, 140, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/PillarJump"]
shape = SubResource("RectangleShape2D_p_140_48")

[node name="SpringLedge" type="StaticBody2D" parent="Platforms"]
position = Vector2(1650, 460)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/SpringLedge"]
texture_repeat = 2
texture = ExtResource("3_stone")
region_enabled = true
region_rect = Rect2(0, 0, 140, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/SpringLedge"]
shape = SubResource("RectangleShape2D_p_140_48")

[node name="ExitPlatform" type="StaticBody2D" parent="Platforms"]
position = Vector2(2150, 480)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/ExitPlatform"]
texture_repeat = 2
texture = ExtResource("3_stone")
region_enabled = true
region_rect = Rect2(0, 0, 500, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/ExitPlatform"]
shape = SubResource("RectangleShape2D_p_500_96")

[node name="Spikes1" parent="." instance=ExtResource("11_spike")]
position = Vector2(920, 440)

[node name="Spikes2" parent="." instance=ExtResource("11_spike")]
position = Vector2(980, 440)

[node name="Spikes3" parent="." instance=ExtResource("11_spike")]
position = Vector2(1040, 440)

[node name="SpringPad1" parent="." instance=ExtResource("10_spring")]
position = Vector2(340, 420)

[node name="SpringPad2" parent="." instance=ExtResource("10_spring")]
position = Vector2(1650, 424)

[node name="QBlock1" parent="." instance=ExtResource("7_qblock")]
position = Vector2(560, 240)

[node name="Coins" type="Node2D" parent="."]

[node name="Coin1" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(500, 320)

[node name="Coin2" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(620, 320)

[node name="Coin3" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(920, 220)

[node name="Coin4" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(980, 220)

[node name="Coin5" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(1040, 220)

[node name="Coin6" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(1650, 220)

[node name="Coin7" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(1740, 180)

[node name="Coin8" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(1820, 220)

[node name="Enemies" type="Node2D" parent="."]

[node name="Goomba1" parent="Enemies" instance=ExtResource("8_goomba")]
position = Vector2(240, 410)

[node name="Flyer1" parent="Enemies" instance=ExtResource("9_flyer")]
position = Vector2(760, 280)

[node name="Flyer2" parent="Enemies" instance=ExtResource("9_flyer")]
position = Vector2(1200, 260)

[node name="Goomba2" parent="Enemies" instance=ExtResource("8_goomba")]
position = Vector2(2050, 410)

[node name="GoalFlag" parent="." instance=ExtResource("12_flag")]
position = Vector2(2320, 388)

[node name="Player" parent="." instance=ExtResource("5_player")]
position = Vector2(80, 400)

[node name="PlatformHUD" parent="." instance=ExtResource("13_hud")]
"""
    with open("scenes/levels/platform_level_2.tscn", "w", encoding="utf-8") as f:
        f.write(content.strip())
    print("Level 2 created successfully!")

def build_level_3():
    content = """[gd_scene load_steps=15 format=3]

[ext_resource type="Script" path="res://scripts/levels/platform_level_controller.gd" id="1_ctrl"]
[ext_resource type="Texture2D" path="res://assets/platformer/tile_stone.png" id="2_stone"]
[ext_resource type="Texture2D" path="res://assets/platformer/tile_lava.png" id="3_lava"]
[ext_resource type="Texture2D" path="res://assets/platformer/block_brick.png" id="4_brick"]
[ext_resource type="PackedScene" path="res://scenes/player/platform_player.tscn" id="5_player"]
[ext_resource type="PackedScene" path="res://scenes/objects/coin.tscn" id="6_coin"]
[ext_resource type="PackedScene" path="res://scenes/objects/question_block.tscn" id="7_qblock"]
[ext_resource type="PackedScene" path="res://scenes/objects/enemy_flyer.tscn" id="8_flyer"]
[ext_resource type="PackedScene" path="res://scenes/objects/boss_monster.tscn" id="9_boss"]
[ext_resource type="PackedScene" path="res://scenes/objects/spikes.tscn" id="10_spike"]
[ext_resource type="PackedScene" path="res://scenes/ui/platform_hud.tscn" id="11_hud"]

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_360_96"]
size = Vector2(360, 96)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_180_48"]
size = Vector2(180, 48)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_220_48"]
size = Vector2(220, 48)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_720_96"]
size = Vector2(720, 96)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_lava_800"]
size = Vector2(800, 64)

[node name="PlatformLevel3" type="Node2D"]
script = ExtResource("1_ctrl")
level_number = 3

[node name="CastleSky" type="CanvasLayer" parent="."]
layer = -100

[node name="ColorRect" type="ColorRect" parent="CastleSky"]
anchors_preset = 15
anchor_right = 1.0
anchor_bottom = 1.0
color = Color(0.14, 0.05, 0.08, 1)

[node name="Platforms" type="Node2D" parent="."]

[node name="CastleStart" type="StaticBody2D" parent="Platforms"]
position = Vector2(180, 480)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/CastleStart"]
texture_repeat = 2
texture = ExtResource("2_stone")
region_enabled = true
region_rect = Rect2(0, 0, 360, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/CastleStart"]
shape = SubResource("RectangleShape2D_p_360_96")

[node name="LavaBridge1" type="StaticBody2D" parent="Platforms"]
position = Vector2(490, 380)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/LavaBridge1"]
texture_repeat = 2
texture = ExtResource("4_brick")
region_enabled = true
region_rect = Rect2(0, 0, 180, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/LavaBridge1"]
shape = SubResource("RectangleShape2D_p_180_48")

[node name="LavaBridge2" type="StaticBody2D" parent="Platforms"]
position = Vector2(780, 320)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/LavaBridge2"]
texture_repeat = 2
texture = ExtResource("4_brick")
region_enabled = true
region_rect = Rect2(0, 0, 180, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/LavaBridge2"]
shape = SubResource("RectangleShape2D_p_180_48")

[node name="HighArch" type="StaticBody2D" parent="Platforms"]
position = Vector2(1100, 260)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/HighArch"]
texture_repeat = 2
texture = ExtResource("2_stone")
region_enabled = true
region_rect = Rect2(0, 0, 220, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/HighArch"]
shape = SubResource("RectangleShape2D_p_220_48")

[node name="BossArena" type="StaticBody2D" parent="Platforms"]
position = Vector2(1800, 480)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/BossArena"]
texture_repeat = 2
texture = ExtResource("2_stone")
region_enabled = true
region_rect = Rect2(0, 0, 720, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/BossArena"]
shape = SubResource("RectangleShape2D_p_720_96")

[node name="LavaHazard" type="Area2D" parent="." groups=["hazard"]]
position = Vector2(750, 520)
collision_layer = 32
collision_mask = 1

[node name="Sprite2D" type="Sprite2D" parent="LavaHazard"]
texture_repeat = 2
texture = ExtResource("3_lava")
region_enabled = true
region_rect = Rect2(0, 0, 800, 64)

[node name="CollisionShape2D" type="CollisionShape2D" parent="LavaHazard"]
shape = SubResource("RectangleShape2D_lava_800")

[node name="QBlock1" parent="." instance=ExtResource("7_qblock")]
position = Vector2(490, 240)

[node name="QBlock2" parent="." instance=ExtResource("7_qblock")]
position = Vector2(1100, 140)

[node name="Coins" type="Node2D" parent="."]

[node name="Coin1" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(440, 310)

[node name="Coin2" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(540, 310)

[node name="Coin3" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(780, 240)

[node name="Coin4" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(1040, 190)

[node name="Coin5" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(1160, 190)

[node name="Enemies" type="Node2D" parent="."]

[node name="Flyer1" parent="Enemies" instance=ExtResource("8_flyer")]
position = Vector2(640, 220)

[node name="Flyer2" parent="Enemies" instance=ExtResource("8_flyer")]
position = Vector2(940, 180)

[node name="BossMonster" parent="Enemies" instance=ExtResource("9_boss")]
position = Vector2(1950, 400)

[node name="Player" parent="." instance=ExtResource("5_player")]
position = Vector2(80, 400)

[node name="PlatformHUD" parent="." instance=ExtResource("11_hud")]
"""
    with open("scenes/levels/platform_level_3.tscn", "w", encoding="utf-8") as f:
        f.write(content.strip())
    print("Level 3 created successfully!")

if __name__ == "__main__":
    os.makedirs("scenes/levels", exist_ok=True)
    build_level_1()
    build_level_2()
    build_level_3()
    print("All 3 Platformer levels generated!")

