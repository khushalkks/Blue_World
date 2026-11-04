extends CharacterBody2D

## Bouncing Plasma Fireball Projectile (Shot by player with [F] key)

@export var speed: float = 420.0
@export var bounce_strength: float = -240.0
@export var gravity: float = 900.0

var dir: float = 1.0
var bounces: int = 0
var max_bounces: int = 4

@onready var sprite: Sprite2D = $Sprite2D

func _ready() -> void:
	velocity.x = dir * speed
	$HitArea.body_entered.connect(_on_hit_body)
	$HitArea.area_entered.connect(_on_hit_area)

func _physics_process(delta: float) -> void:
	velocity.y += gravity * delta
	velocity.x = dir * speed
	sprite.rotation += dir * 16.0 * delta
	
	move_and_slide()
	
	if is_on_floor():
		velocity.y = bounce_strength
		bounces += 1
		if bounces >= max_bounces:
			_explode()
			
	if is_on_wall():
		_explode()

func _on_hit_body(body: Node2D) -> void:
	if body.is_in_group("enemy"):
		if body.has_method("die_from_stomp"):
			body.die_from_stomp()
		_explode()

func _on_hit_area(area: Area2D) -> void:
	if area.is_in_group("stompable"):
		var enemy = area.get_parent()
		if enemy and enemy.has_method("die_from_stomp"):
			enemy.die_from_stomp()
		_explode()

func _explode() -> void:
	GameState.play_sfx("block", -2.0, 1.4)
	queue_free()

