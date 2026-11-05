extends CharacterBody2D

## Bullet Bill / Cyber Plasma Missile
## Flies straight horizontally. Can be stomped to launch player extra high!

@export var speed: float = 210.0
@export var dir: float = -1.0 # -1 is Left, 1 is Right

@onready var sprite: Sprite2D = $Sprite2D
@onready var stomp_area: Area2D = $StompArea
@onready var hurtbox: Area2D = $Hurtbox

var is_dead: bool = false
var lifetime: float = 6.0

func _ready() -> void:
	add_to_group("enemy")
	if stomp_area:
		stomp_area.add_to_group("stompable")
		stomp_area.body_entered.connect(_on_stomp_body_entered)
	if hurtbox:
		hurtbox.body_entered.connect(_on_hurtbox_body_entered)
		hurtbox.area_entered.connect(_on_hurtbox_area_entered)
	if dir > 0:
		if sprite:
			sprite.flip_h = true

func _physics_process(delta: float) -> void:
	if is_dead:
		return
	
	lifetime -= delta
	if lifetime <= 0.0:
		queue_free()
		return
		
	# Thruster flicker
	if sprite:
		sprite.scale = Vector2(1.0 + randf_range(-0.04, 0.04), 1.0 + randf_range(-0.04, 0.04))
	
	velocity = Vector2(dir * speed, 0.0)
	move_and_slide()

func die_from_stomp() -> void:
	if is_dead:
		return
	is_dead = true
	GameState.add_stomp_combo(global_position)
	
	# Death spin & fall
	set_collision_layer_value(1, false)
	set_collision_mask_value(1, false)
	if stomp_area:
		stomp_area.queue_free()
	if hurtbox:
		hurtbox.queue_free()
		
	var tw := create_tween().set_parallel(true)
	tw.tween_property(self, "position:y", position.y + 120.0, 0.45)
	tw.tween_property(self, "rotation", PI * 2.0 * dir, 0.45)
	tw.tween_property(self, "modulate:a", 0.0, 0.45)
	tw.chain().tween_callback(queue_free)

func _on_stomp_body_entered(body: Node2D) -> void:
	if is_dead:
		return
	if body.is_in_group("player") and body.velocity.y > 0.0:
		die_from_stomp()
		if body.has_method("bounce"):
			body.bounce(-460.0) # Extra high bounce!

func _on_hurtbox_body_entered(body: Node2D) -> void:
	if is_dead:
		return
	if body.is_in_group("player"):
		if body.has_method("take_damage"):
			body.take_damage(dir)

func _on_hurtbox_area_entered(area: Area2D) -> void:
	if is_dead:
		return
	if area.is_in_group("player_projectile"):
		area.get_parent().queue_free()
		die_from_stomp()

