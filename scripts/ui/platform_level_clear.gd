extends Control

## Level Clear Victory Screen

@onready var title_label: Label = $CenterContainer/PanelContainer/MarginContainer/VBoxContainer/TitleLabel
@onready var stats_label: Label = $CenterContainer/PanelContainer/MarginContainer/VBoxContainer/StatsLabel
@onready var next_btn: Button = $CenterContainer/PanelContainer/MarginContainer/VBoxContainer/NextButton
@onready var menu_btn: Button = $CenterContainer/PanelContainer/MarginContainer/VBoxContainer/MenuButton

func _ready() -> void:
	GameState.play_sfx("clear", 3.0)
	title_label.text = "WORLD 1-%d CLEARED!" % GameState.current_level
	stats_label.text = "TOTAL SCORE: %06d   |   COINS: %02d" % [GameState.score, GameState.coins]
	
	next_btn.pressed.connect(_on_next_pressed)
	menu_btn.pressed.connect(_on_menu_pressed)
	next_btn.grab_focus()

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("jump") or event.is_action_pressed("ui_accept"):
		_on_next_pressed()

func _on_next_pressed() -> void:
	GameState.play_sfx("jump")
	GameState.next_level()

func _on_menu_pressed() -> void:
	GameState.return_to_menu()

