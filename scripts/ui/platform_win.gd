extends Control

## Grand Victory Screen for clearing all levels!

@onready var score_label: Label = $CenterContainer/PanelContainer/MarginContainer/VBoxContainer/ScoreLabel
@onready var replay_btn: Button = $CenterContainer/PanelContainer/MarginContainer/VBoxContainer/ReplayButton
@onready var menu_btn: Button = $CenterContainer/PanelContainer/MarginContainer/VBoxContainer/MenuButton

func _ready() -> void:
	GameState.play_sfx("clear", 3.0)
	score_label.text = "FINAL SCORE: %06d   |   TOTAL COINS: %02d" % [GameState.score, GameState.coins]
	replay_btn.pressed.connect(_on_replay_pressed)
	menu_btn.pressed.connect(_on_menu_pressed)
	replay_btn.grab_focus()

func _on_replay_pressed() -> void:
	GameState.start_new_game()

func _on_menu_pressed() -> void:
	GameState.return_to_menu()

