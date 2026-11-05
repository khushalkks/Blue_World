extends StaticBody2D

## Warp Pipe
## Classic Mario warp pipe. Stand on top and press DOWN (or S) to slide down and warp!

@export var target_scene: String = ""
@export var target_position: Vector2 = Vector2.ZERO
@export var is_exit_only: bool = false

@onready var enter_area: Area2D = $EnterArea
var player_inside: Node2D = null
var is_warping: bool = false

func _ready() -> void:
	if enter_area and not is_exit_only:
		enter_area.body_entered.connect(_on_enter_area_body_entered)
		enter_area.body_exited.connect(_on_enter_area_body_exited)

func _process(_delta: float) -> void:
	if is_warping or is_exit_only:
		return
	if player_inside and Input.is_action_pressed("move_down"):
		_trigger_warp()

func _on_enter_area_body_entered(body: Node2D) -> void:
	if body.is_in_group("player"):
		player_inside = body

func _on_enter_area_body_exited(body: Node2D) -> void:
	if body == player_inside:
		player_inside = null

func _trigger_warp() -> void:
	if not player_inside or is_warping:
		return
	is_warping = true
	var player = player_inside
	
	# Lock player physics and slide down into the pipe
	player.set_physics_process(false)
	GameState.play_sfx("pipe", 2.0)
	
	var tw := create_tween()
	# Center player horizontally with pipe and slide down
	tw.tween_property(player, "global_position:x", global_position.x, 0.15)
	tw.tween_property(player, "global_position:y", global_position.y + 24.0, 0.45)
	
	await tw.finished
	
	if target_scene == "RETURN":
		GameState.load_level(GameState.current_level)
	elif target_scene != "":
		get_tree().change_scene_to_file(target_scene)
	elif target_position != Vector2.ZERO:
		player.global_position = target_position
		player.set_physics_process(true)
		is_warping = false
	else:
		# Default fallback
		player.set_physics_process(true)
		is_warping = false
