extends Control

## Game Over Screen

@onready var retry_btn: Button = $CenterContainer/PanelContainer/MarginContainer/VBoxContainer/RetryButton
@onready var menu_btn: Button = $CenterContainer/PanelContainer/MarginContainer/VBoxContainer/MenuButton

func _ready() -> void:
	GameState.play_sfx("hurt", 3.0)
	retry_btn.pressed.connect(_on_retry_pressed)
	menu_btn.pressed.connect(_on_menu_pressed)
	retry_btn.grab_focus()

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("jump") or event.is_action_pressed("ui_accept"):
		_on_retry_pressed()

func _on_retry_pressed() -> void:
	GameState.lives = 3
	GameState.restart_current_level()

func _on_menu_pressed() -> void:
	GameState.return_to_menu()

