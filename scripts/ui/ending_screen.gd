extends Control

## Milestone 1 Ending / Mission Debrief Screen
## Congratulates player on clearing Sector A and provides options to replay or exit.

@onready var replay_btn: Button = $CenterContainer/EndingPanel/MarginContainer/VBoxContainer/ReplayButton
@onready var menu_btn: Button = $CenterContainer/EndingPanel/MarginContainer/VBoxContainer/MainMenuButton

func _ready() -> void:
	replay_btn.pressed.connect(_on_replay_pressed)
	menu_btn.pressed.connect(_on_menu_pressed)
	replay_btn.grab_focus()

func _on_replay_pressed() -> void:
	GameState.start_new_game()

func _on_menu_pressed() -> void:
	GameState.return_to_main_menu()
