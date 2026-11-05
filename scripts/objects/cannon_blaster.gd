extends StaticBody2D

## Cannon Blaster
## Cyber cannon turret that periodically launches Bullet Bills towards the player.

@export var fire_interval: float = 3.2
@export var fire_dir: float = -1.0 # -1.0 = Left, 1.0 = Right

@onready var sprite: Sprite2D = $Sprite2D
var timer: float = 0.0
var bullet_scene: PackedScene = preload("res://scenes/objects/bullet_bill.tscn")
var is_priming: bool = false

func _ready() -> void:
	timer = randf_range(0.5, 2.0) # Jitter initial shot
	if fire_dir > 0 and sprite:
		sprite.flip_h = true

func _physics_process(delta: float) -> void:
	timer -= delta
	
	# Recoil recovery
	if sprite:
		sprite.scale = sprite.scale.lerp(Vector2.ONE, delta * 8.0)
		
	if timer <= 0.35 and not is_priming:
		is_priming = true
		_prime_cannon()
		
	if timer <= 0.0:
		timer = fire_interval + randf_range(-0.4, 0.4)
		is_priming = false
		_fire()

func _prime_cannon() -> void:
	if sprite:
		var tw := create_tween()
		tw.tween_property(sprite, "modulate", Color(1.8, 1.2, 0.5, 1.0), 0.3)

func _fire() -> void:
	# Reset sprite modulate
	if sprite:
		sprite.modulate = Color(1.0, 1.0, 1.0, 1.0)
		sprite.scale = Vector2(0.8, 1.2) # Recoil squash
	
	# Check if player is within range
	var player = get_tree().get_first_node_in_group("player")
	if player:
		var dist = global_position.distance_to(player.global_position)
		if dist < 65.0 or dist > 680.0:
			return # Don't fire if player is right on top or off-screen
	
	GameState.play_sfx("cannon", 1.0)
	
	var bullet = bullet_scene.instantiate()
	bullet.dir = fire_dir
	bullet.global_position = global_position + Vector2(26.0 * fire_dir, -4.0)
	get_parent().add_child(bullet)

