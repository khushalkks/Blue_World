extends Control

## Grand Victory Screen for clearing all levels!

@onready var score_label: Label = $CenterContainer/PanelContainer/MarginContainer/VBoxContainer/ScoreLabel
@onready var replay_btn: Button = $CenterContainer/PanelContainer/MarginContainer/VBoxContainer/ReplayButton
@onready var menu_btn: Button = $CenterContainer/PanelContainer/MarginContainer/VBoxContainer/MenuButton

func _ready() -> void:
	GameState.play_sfx("clear", 3.0)
	var total_sec: float = GameState.level_time
	var mins: int = int(total_sec) / 60
	var secs: float = fmod(total_sec, 60.0)
	var time_str: String = "%02d:%04.1f" % [mins, secs]
	score_label.text = "FINAL TIME: %s\nFINAL SCORE: %06d   |   COINS: %02d" % [time_str, GameState.score, GameState.coins]
	replay_btn.pressed.connect(_on_replay_pressed)
	menu_btn.pressed.connect(_on_menu_pressed)
	replay_btn.grab_focus()

func _on_replay_pressed() -> void:
	GameState.start_new_game()

func _on_menu_pressed() -> void:
	GameState.return_to_menu()

