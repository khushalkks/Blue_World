extends Node2D

## Heavy Blast Door & Security Keypad in "THE LAST SIGNAL"
## Blocks progress until the 4-digit code (7394) is entered on the security keypad.

@export var prompt_text: String = "[E] Access Security Keypad"

@onready var door_sprite: Sprite2D = $DoorSprite
@onready var collider: CollisionShape2D = $DoorStaticBody/CollisionShape2D
@onready var status_light: PointLight2D = $StatusLight
@onready var keypad_area: Area2D = $KeypadArea
@onready var exit_area: Area2D = $ExitArea

var closed_texture: Texture2D = null
var open_texture: Texture2D = null

func _ready() -> void:
	closed_texture = load("res://assets/textures/blast_door_closed.png")
	open_texture = load("res://assets/textures/blast_door_open.png")
	
	GameState.puzzle_solved.connect(_on_puzzle_solved)
	
	keypad_area.body_entered.connect(_on_keypad_entered)
	keypad_area.body_exited.connect(_on_keypad_exited)
	
	exit_area.body_entered.connect(_on_exit_entered)
	
	_update_door_visuals()

func _update_door_visuals() -> void:
	if GameState.is_puzzle_solved:
		if open_texture and door_sprite:
			door_sprite.texture = open_texture
		if collider:
			collider.set_deferred("disabled", true)
		if status_light:
			status_light.color = Color(0.2, 1.0, 0.4) # Green access
			status_light.energy = 1.2
	else:
		if closed_texture and door_sprite:
			door_sprite.texture = closed_texture
		if collider:
			collider.set_deferred("disabled", false)
		if status_light:
			status_light.color = Color(1.0, 0.15, 0.2) # Red locked
			status_light.energy = 1.0

func _on_keypad_entered(body: Node2D) -> void:
	if body.is_in_group("player") and not GameState.is_puzzle_solved:
		GameState.nearby_interactive = self

func _on_keypad_exited(body: Node2D) -> void:
	if body.is_in_group("player"):
		if GameState.nearby_interactive == self:
			GameState.nearby_interactive = null

func interact() -> void:
	if not GameState.is_puzzle_solved:
		GameState.set_ui_blocking(true)
		GameState.keypad_opened.emit()

func _on_puzzle_solved() -> void:
	GameState.play_sfx("door_slide", 1.0)
	_update_door_visuals()
	if GameState.nearby_interactive == self:
		GameState.nearby_interactive = null

func _on_exit_entered(body: Node2D) -> void:
	if body.is_in_group("player") and GameState.is_puzzle_solved:
		GameState.trigger_ending()
