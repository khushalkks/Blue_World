extends CanvasLayer

## In-Game Platformer HUD
## Displays World/Level number, Score, Coins, and Lives.

@onready var world_label: Label = $MarginContainer/HBoxContainer/WorldVBox/WorldLabel
@onready var score_label: Label = $MarginContainer/HBoxContainer/ScoreVBox/ScoreLabel
@onready var coin_label: Label = $MarginContainer/HBoxContainer/CoinHBox/CoinLabel
@onready var lives_label: Label = $MarginContainer/HBoxContainer/LivesHBox/LivesLabel

func _ready() -> void:
	GameState.stats_changed.connect(_update_display)
	_update_display()

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

