import os

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

[node name="PlatformLevel1" type="Node2D"]
script = ExtResource("1_ctrl")
level_number = 1
music_track = "bgm"

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
    print("Level 1 generated!")

def build_level_2():
    content = """[gd_scene load_steps=17 format=3]

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
[ext_resource type="PackedScene" path="res://scenes/objects/moving_platform.tscn" id="12_move"]
[ext_resource type="PackedScene" path="res://scenes/objects/goal_flag.tscn" id="13_flag"]
[ext_resource type="PackedScene" path="res://scenes/ui/platform_hud.tscn" id="14_hud"]

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
music_track = "bgm"

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

[node name="MovingHoverLedge" parent="." instance=ExtResource("12_move")]
position = Vector2(1580, 420)
move_offset = Vector2(200, 0)
speed = 70.0

[node name="Spikes1" parent="." instance=ExtResource("11_spike")]
position = Vector2(920, 440)

[node name="Spikes2" parent="." instance=ExtResource("11_spike")]
position = Vector2(980, 440)

[node name="Spikes3" parent="." instance=ExtResource("11_spike")]
position = Vector2(1040, 440)

[node name="SpringPad1" parent="." instance=ExtResource("10_spring")]
position = Vector2(340, 420)

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
position = Vector2(1650, 360)

[node name="Coin7" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(1740, 360)

[node name="Enemies" type="Node2D" parent="."]

[node name="Goomba1" parent="Enemies" instance=ExtResource("8_goomba")]
position = Vector2(240, 410)

[node name="Flyer1" parent="Enemies" instance=ExtResource("9_flyer")]
position = Vector2(760, 280)

[node name="Flyer2" parent="Enemies" instance=ExtResource("9_flyer")]
position = Vector2(1200, 260)

[node name="Goomba2" parent="Enemies" instance=ExtResource("8_goomba")]
position = Vector2(2050, 410)

[node name="GoalFlag" parent="." instance=ExtResource("13_flag")]
position = Vector2(2320, 388)

[node name="Player" parent="." instance=ExtResource("5_player")]
position = Vector2(80, 400)

[node name="PlatformHUD" parent="." instance=ExtResource("14_hud")]
"""
    with open("scenes/levels/platform_level_2.tscn", "w", encoding="utf-8") as f:
        f.write(content.strip())
    print("Level 2 generated!")

def build_level_3():
    # World 1-3: Haunted Midnight Abyss (Suspense with Falling Platforms and Power Star!)
    content = """[gd_scene load_steps=16 format=3]

[ext_resource type="Script" path="res://scripts/levels/platform_level_controller.gd" id="1_ctrl"]
[ext_resource type="Texture2D" path="res://assets/platformer/tile_stone.png" id="2_stone"]
[ext_resource type="Texture2D" path="res://assets/platformer/block_brick.png" id="3_brick"]
[ext_resource type="PackedScene" path="res://scenes/player/platform_player.tscn" id="4_player"]
[ext_resource type="PackedScene" path="res://scenes/objects/coin.tscn" id="5_coin"]
[ext_resource type="PackedScene" path="res://scenes/objects/enemy_flyer.tscn" id="6_flyer"]
[ext_resource type="PackedScene" path="res://scenes/objects/enemy_goomba.tscn" id="7_goomba"]
[ext_resource type="PackedScene" path="res://scenes/objects/falling_platform.tscn" id="8_fall"]
[ext_resource type="PackedScene" path="res://scenes/objects/moving_platform.tscn" id="9_move"]
[ext_resource type="PackedScene" path="res://scenes/objects/powerup_star.tscn" id="10_star"]
[ext_resource type="PackedScene" path="res://scenes/objects/spring_pad.tscn" id="11_spring"]
[ext_resource type="PackedScene" path="res://scenes/objects/goal_flag.tscn" id="12_flag"]
[ext_resource type="PackedScene" path="res://scenes/ui/platform_hud.tscn" id="13_hud"]

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_340_96"]
size = Vector2(340, 96)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_220_48"]
size = Vector2(220, 48)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_480_96"]
size = Vector2(480, 96)

[node name="PlatformLevel3" type="Node2D"]
script = ExtResource("1_ctrl")
level_number = 3
music_track = "suspense"

[node name="AbyssSky" type="CanvasLayer" parent="."]
layer = -100

[node name="ColorRect" type="ColorRect" parent="AbyssSky"]
anchors_preset = 15
anchor_right = 1.0
anchor_bottom = 1.0
color = Color(0.06, 0.04, 0.12, 1)

[node name="Platforms" type="Node2D" parent="."]

[node name="StartLedge" type="StaticBody2D" parent="Platforms"]
position = Vector2(170, 480)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/StartLedge"]
texture_repeat = 2
texture = ExtResource("2_stone")
region_enabled = true
region_rect = Rect2(0, 0, 340, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/StartLedge"]
shape = SubResource("RectangleShape2D_p_340_96")

[node name="MidLedge" type="StaticBody2D" parent="Platforms"]
position = Vector2(980, 380)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/MidLedge"]
texture_repeat = 2
texture = ExtResource("3_brick")
region_enabled = true
region_rect = Rect2(0, 0, 220, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/MidLedge"]
shape = SubResource("RectangleShape2D_p_220_48")

[node name="HighAltar" type="StaticBody2D" parent="Platforms"]
position = Vector2(1500, 260)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/HighAltar"]
texture_repeat = 2
texture = ExtResource("2_stone")
region_enabled = true
region_rect = Rect2(0, 0, 220, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/HighAltar"]
shape = SubResource("RectangleShape2D_p_220_48")

[node name="GoalLedge" type="StaticBody2D" parent="Platforms"]
position = Vector2(2200, 480)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/GoalLedge"]
texture_repeat = 2
texture = ExtResource("2_stone")
region_enabled = true
region_rect = Rect2(0, 0, 480, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/GoalLedge"]
shape = SubResource("RectangleShape2D_p_480_96")

[node name="Crumble1" parent="." instance=ExtResource("8_fall")]
position = Vector2(440, 460)

[node name="Crumble2" parent="." instance=ExtResource("8_fall")]
position = Vector2(560, 420)

[node name="Crumble3" parent="." instance=ExtResource("8_fall")]
position = Vector2(680, 380)

[node name="Crumble4" parent="." instance=ExtResource("8_fall")]
position = Vector2(800, 380)

[node name="MovingPlatform1" parent="." instance=ExtResource("9_move")]
position = Vector2(1180, 340)
move_offset = Vector2(180, -60)
speed = 75.0

[node name="SpringPad1" parent="." instance=ExtResource("11_spring")]
position = Vector2(980, 344)

[node name="PowerupStar" parent="." instance=ExtResource("10_star")]
position = Vector2(1500, 200)

[node name="MovingPlatform2" parent="." instance=ExtResource("9_move")]
position = Vector2(1720, 380)
move_offset = Vector2(220, 40)
speed = 80.0

[node name="Coins" type="Node2D" parent="."]

[node name="Coin1" parent="Coins" instance=ExtResource("5_coin")]
position = Vector2(440, 400)

[node name="Coin2" parent="Coins" instance=ExtResource("5_coin")]
position = Vector2(560, 360)

[node name="Coin3" parent="Coins" instance=ExtResource("5_coin")]
position = Vector2(680, 320)

[node name="Coin4" parent="Coins" instance=ExtResource("5_coin")]
position = Vector2(1270, 260)

[node name="Coin5" parent="Coins" instance=ExtResource("5_coin")]
position = Vector2(1830, 340)

[node name="Enemies" type="Node2D" parent="."]

[node name="Flyer1" parent="Enemies" instance=ExtResource("6_flyer")]
position = Vector2(560, 240)

[node name="Flyer2" parent="Enemies" instance=ExtResource("6_flyer")]
position = Vector2(1360, 200)

[node name="Goomba1" parent="Enemies" instance=ExtResource("7_goomba")]
position = Vector2(2100, 410)

[node name="GoalFlag" parent="." instance=ExtResource("12_flag")]
position = Vector2(2360, 388)

[node name="Player" parent="." instance=ExtResource("4_player")]
position = Vector2(80, 400)

[node name="PlatformHUD" parent="." instance=ExtResource("13_hud")]
"""
    with open("scenes/levels/platform_level_3.tscn", "w", encoding="utf-8") as f:
        f.write(content.strip())
    print("Level 3 generated!")

def build_level_4():
    # World 1-4: Lava Clockwork Foundry (Crushing Thwomps, Fire Bars, and Molten Lava!)
    content = """[gd_scene load_steps=18 format=3]

[ext_resource type="Script" path="res://scripts/levels/platform_level_controller.gd" id="1_ctrl"]
[ext_resource type="Texture2D" path="res://assets/platformer/tile_stone.png" id="2_stone"]
[ext_resource type="Texture2D" path="res://assets/platformer/tile_lava.png" id="3_lava"]
[ext_resource type="Texture2D" path="res://assets/platformer/block_brick.png" id="4_brick"]
[ext_resource type="PackedScene" path="res://scenes/player/platform_player.tscn" id="5_player"]
[ext_resource type="PackedScene" path="res://scenes/objects/coin.tscn" id="6_coin"]
[ext_resource type="PackedScene" path="res://scenes/objects/thwomp_trap.tscn" id="7_thwomp"]
[ext_resource type="PackedScene" path="res://scenes/objects/fire_bar.tscn" id="8_firebar"]
[ext_resource type="PackedScene" path="res://scenes/objects/falling_platform.tscn" id="9_fall"]
[ext_resource type="PackedScene" path="res://scenes/objects/enemy_goomba.tscn" id="10_goomba"]
[ext_resource type="PackedScene" path="res://scenes/objects/spring_pad.tscn" id="11_spring"]
[ext_resource type="PackedScene" path="res://scenes/objects/goal_flag.tscn" id="12_flag"]
[ext_resource type="PackedScene" path="res://scenes/ui/platform_hud.tscn" id="13_hud"]

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_320_96"]
size = Vector2(320, 96)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_400_48"]
size = Vector2(400, 48)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_380_96"]
size = Vector2(380, 96)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_520_96"]
size = Vector2(520, 96)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_lava_1600"]
size = Vector2(1600, 64)

[node name="PlatformLevel4" type="Node2D"]
script = ExtResource("1_ctrl")
level_number = 4
music_track = "suspense"

[node name="FoundrySky" type="CanvasLayer" parent="."]
layer = -100

[node name="ColorRect" type="ColorRect" parent="FoundrySky"]
anchors_preset = 15
anchor_right = 1.0
anchor_bottom = 1.0
color = Color(0.16, 0.06, 0.06, 1)

[node name="Platforms" type="Node2D" parent="."]

[node name="StartLedge" type="StaticBody2D" parent="Platforms"]
position = Vector2(160, 480)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/StartLedge"]
texture_repeat = 2
texture = ExtResource("2_stone")
region_enabled = true
region_rect = Rect2(0, 0, 320, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/StartLedge"]
shape = SubResource("RectangleShape2D_p_320_96")

[node name="ThwompRunway" type="StaticBody2D" parent="Platforms"]
position = Vector2(580, 460)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/ThwompRunway"]
texture_repeat = 2
texture = ExtResource("2_stone")
region_enabled = true
region_rect = Rect2(0, 0, 400, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/ThwompRunway"]
shape = SubResource("RectangleShape2D_p_400_48")

[node name="FireBarSanctuary" type="StaticBody2D" parent="Platforms"]
position = Vector2(1320, 420)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/FireBarSanctuary"]
texture_repeat = 2
texture = ExtResource("4_brick")
region_enabled = true
region_rect = Rect2(0, 0, 380, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/FireBarSanctuary"]
shape = SubResource("RectangleShape2D_p_380_96")

[node name="ExitLedge" type="StaticBody2D" parent="Platforms"]
position = Vector2(2150, 480)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/ExitLedge"]
texture_repeat = 2
texture = ExtResource("2_stone")
region_enabled = true
region_rect = Rect2(0, 0, 520, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/ExitLedge"]
shape = SubResource("RectangleShape2D_p_520_96")

[node name="LavaHazard" type="Area2D" parent="." groups=["hazard"]]
position = Vector2(1100, 530)
collision_layer = 32
collision_mask = 1

[node name="Sprite2D" type="Sprite2D" parent="LavaHazard"]
texture_repeat = 2
texture = ExtResource("3_lava")
region_enabled = true
region_rect = Rect2(0, 0, 1600, 64)

[node name="CollisionShape2D" type="CollisionShape2D" parent="LavaHazard"]
shape = SubResource("RectangleShape2D_lava_1600")

[node name="Thwomp1" parent="." instance=ExtResource("7_thwomp")]
position = Vector2(480, 220)

[node name="Thwomp2" parent="." instance=ExtResource("7_thwomp")]
position = Vector2(680, 220)

[node name="Crumble1" parent="." instance=ExtResource("9_fall")]
position = Vector2(880, 440)

[node name="Crumble2" parent="." instance=ExtResource("9_fall")]
position = Vector2(1000, 440)

[node name="FireBar1" parent="." instance=ExtResource("8_firebar")]
position = Vector2(1250, 340)
rotation_speed = 2.4

[node name="FireBar2" parent="." instance=ExtResource("8_firebar")]
position = Vector2(1400, 340)
rotation_speed = -2.4

[node name="SpringPad1" parent="." instance=ExtResource("11_spring")]
position = Vector2(1480, 360)

[node name="CrumbleBridge3" parent="." instance=ExtResource("9_fall")]
position = Vector2(1700, 380)

[node name="CrumbleBridge4" parent="." instance=ExtResource("9_fall")]
position = Vector2(1820, 420)

[node name="Coins" type="Node2D" parent="."]

[node name="Coin1" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(480, 380)

[node name="Coin2" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(680, 380)

[node name="Coin3" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(1320, 280)

[node name="Coin4" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(1700, 320)

[node name="Coin5" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(1820, 360)

[node name="Enemies" type="Node2D" parent="."]

[node name="Goomba1" parent="Enemies" instance=ExtResource("10_goomba")]
position = Vector2(2050, 410)

[node name="GoalFlag" parent="." instance=ExtResource("12_flag")]
position = Vector2(2320, 388)

[node name="Player" parent="." instance=ExtResource("5_player")]
position = Vector2(80, 400)

[node name="PlatformHUD" parent="." instance=ExtResource("13_hud")]
"""
    with open("scenes/levels/platform_level_4.tscn", "w", encoding="utf-8") as f:
        f.write(content.strip())
    print("Level 4 generated!")

def build_level_5():
    # World 1-5: The Final Citadel & 2-Phase King Boss Battle!
    content = """[gd_scene load_steps=17 format=3]

[ext_resource type="Script" path="res://scripts/levels/platform_level_controller.gd" id="1_ctrl"]
[ext_resource type="Texture2D" path="res://assets/platformer/tile_stone.png" id="2_stone"]
[ext_resource type="Texture2D" path="res://assets/platformer/tile_lava.png" id="3_lava"]
[ext_resource type="Texture2D" path="res://assets/platformer/block_brick.png" id="4_brick"]
[ext_resource type="PackedScene" path="res://scenes/player/platform_player.tscn" id="5_player"]
[ext_resource type="PackedScene" path="res://scenes/objects/coin.tscn" id="6_coin"]
[ext_resource type="PackedScene" path="res://scenes/objects/question_block.tscn" id="7_qblock"]
[ext_resource type="PackedScene" path="res://scenes/objects/powerup_star.tscn" id="8_star"]
[ext_resource type="PackedScene" path="res://scenes/objects/fire_bar.tscn" id="9_firebar"]
[ext_resource type="PackedScene" path="res://scenes/objects/thwomp_trap.tscn" id="10_thwomp"]
[ext_resource type="PackedScene" path="res://scenes/objects/boss_monster.tscn" id="11_boss"]
[ext_resource type="PackedScene" path="res://scenes/ui/platform_hud.tscn" id="12_hud"]

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_320_96"]
size = Vector2(320, 96)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_220_48"]
size = Vector2(220, 48)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_p_860_96"]
size = Vector2(860, 96)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_lava_800"]
size = Vector2(800, 64)

[node name="PlatformLevel5" type="Node2D"]
script = ExtResource("1_ctrl")
level_number = 5
music_track = "bgm"

[node name="CastleSky" type="CanvasLayer" parent="."]
layer = -100

[node name="ColorRect" type="ColorRect" parent="CastleSky"]
anchors_preset = 15
anchor_right = 1.0
anchor_bottom = 1.0
color = Color(0.12, 0.02, 0.05, 1)

[node name="Platforms" type="Node2D" parent="."]

[node name="CastleStart" type="StaticBody2D" parent="Platforms"]
position = Vector2(160, 480)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/CastleStart"]
texture_repeat = 2
texture = ExtResource("2_stone")
region_enabled = true
region_rect = Rect2(0, 0, 320, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/CastleStart"]
shape = SubResource("RectangleShape2D_p_320_96")

[node name="Bridge1" type="StaticBody2D" parent="Platforms"]
position = Vector2(490, 380)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/Bridge1"]
texture_repeat = 2
texture = ExtResource("4_brick")
region_enabled = true
region_rect = Rect2(0, 0, 220, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/Bridge1"]
shape = SubResource("RectangleShape2D_p_220_48")

[node name="Bridge2" type="StaticBody2D" parent="Platforms"]
position = Vector2(840, 320)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/Bridge2"]
texture_repeat = 2
texture = ExtResource("4_brick")
region_enabled = true
region_rect = Rect2(0, 0, 220, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/Bridge2"]
shape = SubResource("RectangleShape2D_p_220_48")

[node name="BossArenaFloor" type="StaticBody2D" parent="Platforms"]
position = Vector2(1800, 480)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/BossArenaFloor"]
texture_repeat = 2
texture = ExtResource("2_stone")
region_enabled = true
region_rect = Rect2(0, 0, 860, 96)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/BossArenaFloor"]
shape = SubResource("RectangleShape2D_p_860_96")

[node name="BossArenaStepLeft" type="StaticBody2D" parent="Platforms"]
position = Vector2(1500, 360)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/BossArenaStepLeft"]
texture_repeat = 2
texture = ExtResource("2_stone")
region_enabled = true
region_rect = Rect2(0, 0, 180, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/BossArenaStepLeft"]
shape = SubResource("RectangleShape2D_p_220_48")

[node name="BossArenaStepRight" type="StaticBody2D" parent="Platforms"]
position = Vector2(2100, 360)
collision_layer = 2
collision_mask = 0

[node name="Sprite2D" type="Sprite2D" parent="Platforms/BossArenaStepRight"]
texture_repeat = 2
texture = ExtResource("2_stone")
region_enabled = true
region_rect = Rect2(0, 0, 180, 48)

[node name="CollisionShape2D" type="CollisionShape2D" parent="Platforms/BossArenaStepRight"]
shape = SubResource("RectangleShape2D_p_220_48")

[node name="LavaHazard" type="Area2D" parent="." groups=["hazard"]]
position = Vector2(660, 530)
collision_layer = 32
collision_mask = 1

[node name="Sprite2D" type="Sprite2D" parent="LavaHazard"]
texture_repeat = 2
texture = ExtResource("3_lava")
region_enabled = true
region_rect = Rect2(0, 0, 800, 64)

[node name="CollisionShape2D" type="CollisionShape2D" parent="LavaHazard"]
shape = SubResource("RectangleShape2D_lava_800")

[node name="ThwompEntry" parent="." instance=ExtResource("10_thwomp")]
position = Vector2(490, 160)

[node name="FireBarBridge" parent="." instance=ExtResource("9_firebar")]
position = Vector2(840, 240)
rotation_speed = 2.0

[node name="PowerStarBeforeBoss" parent="." instance=ExtResource("8_star")]
position = Vector2(1200, 320)

[node name="QBlock1" parent="." instance=ExtResource("7_qblock")]
position = Vector2(1800, 320)

[node name="Coins" type="Node2D" parent="."]

[node name="Coin1" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(440, 310)

[node name="Coin2" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(540, 310)

[node name="Coin3" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(840, 180)

[node name="Coin4" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(1500, 290)

[node name="Coin5" parent="Coins" instance=ExtResource("6_coin")]
position = Vector2(2100, 290)

[node name="BossMonster" parent="." instance=ExtResource("11_boss")]
position = Vector2(1950, 400)

[node name="Player" parent="." instance=ExtResource("5_player")]
position = Vector2(80, 400)

[node name="PlatformHUD" parent="." instance=ExtResource("12_hud")]
"""
    with open("scenes/levels/platform_level_5.tscn", "w", encoding="utf-8") as f:
        f.write(content.strip())
    print("Level 5 generated!")

if __name__ == "__main__":
    os.makedirs("scenes/levels", exist_ok=True)
    build_level_1()
    build_level_2()
    build_level_3()
    build_level_4()
    build_level_5()
    print("All 5 Platformer levels generated successfully!")
