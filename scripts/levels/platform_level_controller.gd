extends Node2D

## Platformer Level Controller

@export var level_number: int = 1

func _ready() -> void:
	GameState.current_level = level_number
	GameState.play_bgm("bgm", -6.0)
	GameState.stats_changed.emit()

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("pause"):
		GameState.return_to_menu()

