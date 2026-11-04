extends CharacterBody2D

## Thwomp Slammer Trap (Suspense Hazard)
## Hangs on ceiling, detects player underneath, slams down with impact, then returns slowly.

@export var slam_speed: float = 750.0
@export var return_speed: float = 120.0
@export var wait_at_bottom: float = 0.75

@onready var trigger_area: Area2D = $TriggerArea
@onready var hurt_area: Area2D = $CrushHurtArea
@onready var sprite: Sprite2D = $Sprite2D

enum State { IDLE, SLAMMING, WAITING, RETURNING }
var current_state: State = State.IDLE
var origin_pos: Vector2 = Vector2.ZERO

func _ready() -> void:
	origin_pos = position
	if trigger_area:
		trigger_area.body_entered.connect(_on_player_detected)
	if hurt_area:
		hurt_area.body_entered.connect(_on_crush_body_entered)

func _physics_process(delta: float) -> void:
	match current_state:
		State.SLAMMING:
			velocity.y = slam_speed
			move_and_slide()
			if is_on_floor():
				current_state = State.WAITING
				GameState.play_sfx("thwomp", 3.0)
				_wait_and_return()
		State.RETURNING:
			position.y = move_toward(position.y, origin_pos.y, return_speed * delta)
			if abs(position.y - origin_pos.y) < 2.0:
				position.y = origin_pos.y
				current_state = State.IDLE

func _on_player_detected(body: Node2D) -> void:
	if current_state == State.IDLE and body.is_in_group("player"):
		current_state = State.SLAMMING

func _wait_and_return() -> void:
	await get_tree().create_timer(wait_at_bottom).timeout
	if current_state == State.WAITING:
		current_state = State.RETURNING

func _on_crush_body_entered(body: Node2D) -> void:
	if body.is_in_group("player") and current_state == State.SLAMMING:
		if body.has_method("take_damage"):
			body.take_damage(0.0)

