extends Control

## Milestone 1 Ending / Mission Debrief Screen
## Congratulates player on clearing Sector A and provides options to replay or exit.

@onready var replay_btn: Button = $CenterContainer/EndingPanel/MarginContainer/VBoxContainer/ReplayButton
@onready var menu_btn: Button = $CenterContainer/EndingPanel/MarginContainer/VBoxContainer/MainMenuButton

func _ready() -> void:
	GameState.play_sfx("access_granted", 1.0)
	replay_btn.pressed.connect(_on_replay_pressed)
	menu_btn.pressed.connect(_on_menu_pressed)
	replay_btn.mouse_entered.connect(func(): GameState.play_sfx("ui_hover", -6.0))
	menu_btn.mouse_entered.connect(func(): GameState.play_sfx("ui_hover", -6.0))
	replay_btn.grab_focus()

func _on_replay_pressed() -> void:
	GameState.play_sfx("power_surge", -2.0)
	GameState.start_new_game()

func _on_menu_pressed() -> void:
	GameState.play_sfx("ui_click")
	GameState.return_to_main_menu()
