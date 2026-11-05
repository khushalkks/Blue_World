extends CharacterBody2D

## Goomba-style Patrol Enemy
## Walks back and forth, reverses on walls or ledge raycasts, squashes when stomped.

@export var move_speed: float = 75.0
@export var patrol_distance: float = 180.0

@onready var sprite: Sprite2D = $Sprite2D
@onready var stomp_area: Area2D = $StompZone
@onready var hurt_area: Area2D = $HurtZone

var direction: float = -1.0
var origin_x: float = 0.0
var is_dead: bool = false
var gravity: float = 980.0

func _ready() -> void:
	add_to_group("enemy")
	origin_x = position.x
	if stomp_area:
		stomp_area.add_to_group("stompable")
	if hurt_area:
		hurt_area.body_entered.connect(_on_hurt_body_entered)

func _physics_process(delta: float) -> void:
	if is_dead:
		return
		
	# Apply gravity
	if not is_on_floor():
		velocity.y += gravity * delta
		
	# Check patrol boundary
	if abs(position.x - origin_x) >= patrol_distance:
		direction = -direction
		origin_x = position.x
		
	# Check wall collision
	if is_on_wall():
		direction = -direction
		
	velocity.x = direction * move_speed
	sprite.flip_h = direction > 0.0
	
	# Walking wobble
	var t = Time.get_ticks_msec() / 1000.0
	sprite.scale.y = 1.0 + sin(t * 10.0) * 0.08
	
	move_and_slide()

func die_from_stomp() -> void:
	if is_dead:
		return
	is_dead = true
	GameState.play_sfx("stomp", 2.0)
	GameState.add_stomp_combo(global_position)
	
	# Disable collisions
	$CollisionShape2D.set_deferred("disabled", true)
	if stomp_area: stomp_area.set_deferred("monitoring", false)
	if hurt_area: hurt_area.set_deferred("monitoring", false)
	
	# Squash flat animation
	var tw = create_tween()
	tw.tween_property(sprite, "scale", Vector2(1.4, 0.2), 0.12)
	tw.tween_property(self, "modulate:a", 0.0, 0.3).set_delay(0.15)
	await tw.finished
	queue_free()

func _on_hurt_body_entered(body: Node2D) -> void:
	if is_dead:
		return
	if body.is_in_group("player"):
		var knock_dir = -1.0 if position.x > body.position.x else 1.0
		if body.has_method("take_damage"):
			body.take_damage(knock_dir)

