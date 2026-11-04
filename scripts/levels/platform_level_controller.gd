extends Node2D

## Platformer Level Controller

@export var level_number: int = 1
@export var music_track: String = "bgm"

func _ready() -> void:
	GameState.current_level = level_number
	GameState.play_bgm(music_track, -6.0)
	GameState.stats_changed.emit()

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("pause"):
		GameState.return_to_menu()
