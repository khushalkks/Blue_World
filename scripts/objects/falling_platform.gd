extends AnimatableBody2D

## Crumbling / Falling Platform (Suspense Trap)
## When stepped on, shakes violently for 0.75s, plays crumble SFX, falls down, and respawns.

@export var shake_duration: float = 0.75
@export var respawn_time: float = 3.2

@onready var sprite: Sprite2D = $Sprite2D
@onready var detector: Area2D = $StepDetector
@onready var col_shape: CollisionShape2D = $CollisionShape2D

var initial_pos: Vector2 = Vector2.ZERO
var is_triggered: bool = false
var is_falling: bool = false
var fall_velocity: float = 0.0

func _ready() -> void:
	initial_pos = position
	if detector:
		detector.body_entered.connect(_on_stepped)

func _physics_process(delta: float) -> void:
	if is_falling:
		fall_velocity += 980.0 * delta
		position.y += fall_velocity * delta

func _on_stepped(body: Node2D) -> void:
	if is_triggered or is_falling:
		return
	if body.is_in_group("player"):
		_trigger_collapse()

func _trigger_collapse() -> void:
	is_triggered = true
	GameState.play_sfx("crumble", -2.0)
	
	# Shaking animation & warning red modulate
	var elapsed := 0.0
	while elapsed < shake_duration:
		var shake := sin(elapsed * 45.0) * 3.5
		sprite.position.x = shake
		sprite.modulate = Color(1.0, 0.4 + 0.6 * (1.0 - elapsed / shake_duration), 0.4)
		await get_tree().process_frame
		elapsed += get_process_delta_time()
		
	sprite.position.x = 0.0
	is_falling = true
	fall_velocity = 80.0
	col_shape.set_deferred("disabled", true)
	
	await get_tree().create_timer(respawn_time).timeout
	_respawn()

func _respawn() -> void:
	is_falling = false
	is_triggered = false
	fall_velocity = 0.0
	position = initial_pos
	sprite.modulate = Color(1.0, 1.0, 1.0, 0.0)
	col_shape.set_deferred("disabled", false)
	
	var tw = create_tween()
	tw.tween_property(sprite, "modulate:a", 1.0, 0.35)

