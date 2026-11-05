extends CanvasLayer

## In-Game Platformer HUD
## Displays World/Level number, Score, Coins, Lives, Speedrun Timer, Combos & Active Power-Ups.

@onready var world_label: Label = $MarginContainer/HBoxContainer/WorldVBox/WorldLabel
@onready var score_label: Label = $MarginContainer/HBoxContainer/ScoreVBox/ScoreLabel
@onready var coin_label: Label = $MarginContainer/HBoxContainer/CoinHBox/CoinLabel
@onready var lives_label: Label = $MarginContainer/HBoxContainer/LivesHBox/LivesLabel
@onready var time_label: Label = get_node_or_null("MarginContainer/HBoxContainer/TimeVBox/TimeLabel")
@onready var powerup_label: Label = get_node_or_null("MarginContainer/HBoxContainer/PowerupLabel")
@onready var combo_banner: Label = get_node_or_null("ComboBanner")

var combo_tween: Tween = null

func _ready() -> void:
	GameState.stats_changed.connect(_update_display)
	GameState.combo_triggered.connect(_on_combo_triggered)
	_update_display()

func _process(_delta: float) -> void:
	# Update Speedrun Timer
	if time_label:
		var total_sec: float = GameState.level_time
		var mins: int = int(total_sec) / 60
		var secs: float = fmod(total_sec, 60.0)
		time_label.text = "%02d:%04.1f" % [mins, secs]
		
	# Update Powerup Status
	if powerup_label:
		var player = get_tree().get_first_node_in_group("player")
		if player:
			if "is_rainbow_invincible" in player and player.is_rainbow_invincible:
				powerup_label.text = "🌈 STAR INVINCIBLE (%.1fs)" % player.rainbow_timer
				powerup_label.modulate = Color.from_hsv(fmod(total_sec * 4.0, 1.0), 0.9, 1.3)
			elif "has_magnet_power" in player and player.has_magnet_power:
				powerup_label.text = "🧲 COIN MAGNET (%.1fs)" % player.magnet_timer
				powerup_label.modulate = Color(0.3, 0.9, 1.0, 1.0)
			elif "has_plasma_power" in player and player.has_plasma_power:
				powerup_label.text = "🔥 PLASMA READY"
				powerup_label.modulate = Color(1.2, 0.9, 0.2, 1.0)
			else:
				powerup_label.text = ""
		else:
			powerup_label.text = ""

func _update_display() -> void:
	if world_label:
		world_label.text = "WORLD 1-%d" % GameState.current_level
	if score_label:
		score_label.text = "%06d" % GameState.score
	if coin_label:
		coin_label.text = "x %02d" % GameState.coins
	if lives_label:
		var hearts := ""
		for i in range(GameState.lives):
			hearts += "❤ "
		lives_label.text = hearts.strip_edges()

func _on_combo_triggered(combo_count: int, points: int, _world_pos: Vector2) -> void:
	if not combo_banner:
		return
		
	if combo_tween and combo_tween.is_valid():
		combo_tween.kill()
		
	if combo_count >= 5:
		combo_banner.text = "🌟 1-UP EXTRA LIFE! x%d AIR COMBO (+%d PTS) 🌟" % [combo_count, points]
		combo_banner.modulate = Color(0.3, 1.5, 0.5, 1.0)
	elif combo_count >= 2:
		combo_banner.text = "⚡ AIR COMBO x%d! +%d PTS ⚡" % [combo_count, points]
		combo_banner.modulate = Color(1.0, 0.9, 0.1, 1.0)
	else:
		return # Single stomp doesn't need big banner
		
	combo_banner.scale = Vector2(0.5, 0.5)
	combo_banner.pivot_offset = combo_banner.size * 0.5
	
	combo_tween = create_tween()
	combo_tween.tween_property(combo_banner, "scale", Vector2(1.15, 1.15), 0.15).set_trans(Tween.TRANS_BACK)
	combo_tween.tween_property(combo_banner, "scale", Vector2(1.0, 1.0), 0.1)
	combo_tween.tween_interval(0.6)
	combo_tween.tween_property(combo_banner, "modulate:a", 0.0, 0.25)
