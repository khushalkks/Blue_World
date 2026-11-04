extends CharacterBody2D

## Player Controller for "SUPER BLUE RUNNER"
## Tight, responsive Mario-style 2D platformer movement, jumping, stomping & squash-stretch.

signal player_died

@export var move_speed: float = 260.0
@export var acceleration: float = 1800.0
@export var friction: float = 1400.0
@export var jump_velocity: float = -470.0
@export var bounce_velocity: float = -420.0
@export var spring_velocity: float = -680.0
@export var gravity: float = 1100.0
@export var fall_gravity_mult: float = 1.35

@onready var sprite: Sprite2D = $Sprite2D
@onready var stomp_area: Area2D = $StompArea
@onready var hurtbox: Area2D = $Hurtbox

var coyote_timer: float = 0.0
var jump_buffer_timer: float = 0.0
var is_invulnerable: bool = false
var invuln_timer: float = 0.0
var facing_right: bool = true
var target_scale: Vector2 = Vector2.ONE
var is_dead: bool = false
var has_plasma_power: bool = false
var shoot_cooldown: float = 0.0

@onready var camera: Camera2D = get_node_or_null("Camera2D")

func _ready() -> void:
	add_to_group("player")
	if stomp_area:
		stomp_area.area_entered.connect(_on_stomp_area_entered)
		stomp_area.body_entered.connect(_on_stomp_body_entered)
	if hurtbox:
		hurtbox.body_entered.connect(_on_hurtbox_body_entered)
		hurtbox.area_entered.connect(_on_hurtbox_area_entered)

func _physics_process(delta: float) -> void:
	if is_dead:
		return
		
	# Fall into bottomless pit
	if position.y > 600.0:
		_die()
		return
	
	# Plasma power cooldown & shooting
	if has_plasma_power:
		shoot_cooldown -= delta
		if Input.is_action_just_pressed("fire") and shoot_cooldown <= 0.0:
			shoot_plasma()
			shoot_cooldown = 0.28
	
	# Invulnerability timer & blinking
	if is_invulnerable:
		invuln_timer -= delta
		sprite.visible = int(invuln_timer * 14.0) % 2 == 0
		if invuln_timer <= 0.0:
			is_invulnerable = false
			sprite.visible = true
	
	# Coyote time & Jump buffer timers
	if is_on_floor():
		coyote_timer = 0.12
	else:
		coyote_timer -= delta
		
	jump_buffer_timer -= delta
	if Input.is_action_just_pressed("jump"):
		jump_buffer_timer = 0.12
		
	# Apply Gravity (with heavier fast fall for crisp platforming)
	var current_grav: float = gravity
	if velocity.y > 0.0:
		current_grav *= fall_gravity_mult
	velocity.y += current_grav * delta
	
	# Horizontal Movement
	var input_x: float = Input.get_axis("move_left", "move_right")
	if input_x != 0.0:
		velocity.x = move_toward(velocity.x, input_x * move_speed, acceleration * delta)
		facing_right = input_x > 0.0
		sprite.flip_h = not facing_right
	else:
		velocity.x = move_toward(velocity.x, 0.0, friction * delta)
	
	# Jump Trigger (Coyote + Buffer)
	if jump_buffer_timer > 0.0 and coyote_timer > 0.0:
		velocity.y = jump_velocity
		jump_buffer_timer = 0.0
		coyote_timer = 0.0
		GameState.play_sfx("jump", -2.0)
		target_scale = Vector2(0.8, 1.25) # Jump stretch
		
	# Variable Jump Height (cutting jump short when button released)
	if Input.is_action_just_released("jump") and velocity.y < -120.0:
		velocity.y *= 0.5
		
	# Landing detection squash
	var was_in_air: bool = not is_on_floor()
	move_and_slide()
	if was_in_air and is_on_floor():
		target_scale = Vector2(1.25, 0.75) # Land squash
		
	# Smooth squash & stretch lerp back to 1.0
	target_scale = target_scale.lerp(Vector2.ONE, delta * 12.0)
	sprite.scale = target_scale

func bounce(custom_force: float = 0.0) -> void:
	velocity.y = custom_force if custom_force != 0.0 else bounce_velocity
	target_scale = Vector2(0.85, 1.25)

func spring_launch() -> void:
	velocity.y = spring_velocity
	GameState.play_sfx("spring", 1.0)
	target_scale = Vector2(0.7, 1.35)

func grant_plasma_power() -> void:
	has_plasma_power = true
	# Golden glowing aura
	sprite.modulate = Color(1.3, 1.2, 0.4, 1.0)
	target_scale = Vector2(1.3, 1.3)

func shoot_plasma() -> void:
	GameState.play_sfx("fireball", 1.0)
	var proj_scene = load("res://scenes/objects/plasma_projectile.tscn")
	if proj_scene:
		var p = proj_scene.instantiate()
		p.dir = 1.0 if facing_right else -1.0
		p.position = position + Vector2(18.0 * p.dir, 0)
		get_parent().add_child(p)

func take_damage(knockback_dir: float = 0.0) -> void:
	if is_invulnerable or is_dead:
		return
		
	var fatal := GameState.take_damage()
	if fatal:
		_die()
		return
		
	is_invulnerable = true
	invuln_timer = 1.3
	velocity.y = -260.0
	velocity.x = knockback_dir * 220.0
	target_scale = Vector2(1.2, 0.8)

func _die() -> void:
	if is_dead:
		return
	is_dead = true
	GameState.play_sfx("hurt", 3.0)
	player_died.emit()
	
	# Check lives
	GameState.lives -= 1
	GameState.stats_changed.emit()
	
	await get_tree().create_timer(0.8).timeout
	if GameState.lives <= 0:
		GameState.handle_game_over()
	else:
		GameState.restart_current_level()

func _on_stomp_area_entered(area: Area2D) -> void:
	if area.is_in_group("stompable"):
		var enemy = area.get_parent()
		if enemy and enemy.has_method("die_from_stomp"):
			enemy.die_from_stomp()
			bounce()

func _on_stomp_body_entered(body: Node2D) -> void:
	if body.is_in_group("stompable"):
		if body.has_method("die_from_stomp"):
			body.die_from_stomp()
			bounce()

func _on_hurtbox_body_entered(body: Node2D) -> void:
	if body.is_in_group("enemy") and not is_invulnerable:
		var dir: float = -1.0 if body.global_position.x > global_position.x else 1.0
		take_damage(dir)
	elif body.is_in_group("hazard"):
		take_damage(0.0)

func _on_hurtbox_area_entered(area: Area2D) -> void:
	if area.is_in_group("hazard"):
		take_damage(0.0)

