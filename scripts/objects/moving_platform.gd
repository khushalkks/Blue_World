extends AnimatableBody2D

## Moving Platform (Kinematic hover platform)

@export var move_offset: Vector2 = Vector2(160, 0)
@export var speed: float = 65.0

var start_pos: Vector2 = Vector2.ZERO
var target_pos: Vector2 = Vector2.ZERO
var moving_to_target: bool = true

func _ready() -> void:
	start_pos = position
	target_pos = start_pos + move_offset

func _physics_process(delta: float) -> void:
	var dest := target_pos if moving_to_target else start_pos
	position = position.move_toward(dest, speed * delta)
	if position.distance_to(dest) < 2.0:
		moving_to_target = not moving_to_target

