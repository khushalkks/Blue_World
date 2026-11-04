extends CharacterBody2D

## King Boss Monster (Level 3 Boss)
## Jumps across arena, charges, takes 3 stomps to defeat, spawns Victory Goal!

@export var max_hp: int = 3
var hp: int = 3

@onready var sprite: Sprite2D = $Sprite2D
@onready var stomp_area: Area2D = $StompArea
@onready var hurt_area: Area2D = $HurtArea

var jump_timer: float = 2.0
var shoot_timer: float = 3.0
var move_dir: float = -1.0
var is_invuln: bool = false
var is_dead: bool = false
var gravity: float = 980.0
var speed: float = 120.0

func _ready() -> void:
	add_to_group("enemy")
	hp = max_hp
	if stomp_area:
		stomp_area.add_to_group("stompable")
	if hurt_area:
		hurt_area.body_entered.connect(_on_hurt_body_entered)

func _physics_process(delta: float) -> void:
	if is_dead:
		return
		
	# Gravity
	if not is_on_floor():
		velocity.y += gravity * delta
		
	# Jump AI timer
	jump_timer -= delta
	if jump_timer <= 0.0 and is_on_floor():
		jump_timer = randf_range(1.6, 2.4)
		velocity.y = -520.0
		if randf() > 0.4:
			move_dir = -move_dir
		GameState.play_sfx("spring", -4.0, 0.7)
		
	# Phase 2 Fireball Attack
	if hp < max_hp:
		shoot_timer -= delta
		if shoot_timer <= 0.0:
			shoot_timer = randf_range(2.5, 3.8)
			_boss_shoot_fireball()
		
	# Reverse on walls
	if is_on_wall():
		move_dir = -move_dir
		
	velocity.x = move_dir * speed
	sprite.flip_h = move_dir > 0.0
	
	move_and_slide()

func _boss_shoot_fireball() -> void:
	GameState.play_sfx("fireball", 2.0, 0.75)
	var proj_scene = load("res://scenes/objects/plasma_projectile.tscn")
	if proj_scene:
		var p = proj_scene.instantiate()
		p.dir = move_dir
		p.position = position + Vector2(24.0 * move_dir, 0)
		get_parent().add_child(p)

func die_from_stomp() -> void:
	if is_invuln or is_dead:
		return
		
	hp -= 1
	GameState.play_sfx("stomp", 3.0, 0.8)
	GameState.add_score(500)
	
	if hp <= 0:
		_die_boss()
		return
		
	# Boss hit reaction (invuln flash, faster speed, enrage color!)
	is_invuln = true
	speed += 50.0
	velocity.y = -320.0
	
	# Summon a flying bat minion in phase 2!
	var flyer_scene = load("res://scenes/objects/enemy_flyer.tscn")
	if flyer_scene:
		var f = flyer_scene.instantiate()
		f.position = position + Vector2(randf_range(-60, 60), -80)
		get_parent().add_child(f)
	
	var tw = create_tween()
	tw.tween_property(sprite, "modulate", Color(1.5, 0.3, 0.2, 1.0), 0.15)
	tw.tween_property(sprite, "modulate", Color(1.0, 1.0, 1.0, 1.0), 0.15)
	tw.tween_property(sprite, "modulate", Color(1.5, 0.3, 0.2, 1.0), 0.15)
	tw.tween_property(sprite, "modulate", Color(1.2, 0.4, 0.3, 1.0), 0.2)
	
	await get_tree().create_timer(1.2).timeout
	is_invuln = false

func _die_boss() -> void:
	is_dead = true
	GameState.play_sfx("clear", 3.0)
	GameState.add_score(2500)
	
	$CollisionShape2D.set_deferred("disabled", true)
	if stomp_area: stomp_area.set_deferred("monitoring", false)
	if hurt_area: hurt_area.set_deferred("monitoring", false)
	
	# Epic defeat spin & fall
	var tw = create_tween().set_parallel(true)
	tw.tween_property(sprite, "rotation", 6.28 * 2.0, 1.2)
	tw.tween_property(sprite, "scale", Vector2.ZERO, 1.2)
	tw.tween_property(self, "position:y", position.y - 80.0, 0.4).set_ease(Tween.EASE_OUT)
	tw.chain().tween_property(self, "position:y", position.y + 400.0, 0.8).set_ease(Tween.EASE_IN)
	await tw.finished
	
	# Spawn Goal Flag at boss arena center!
	var flag_scene = load("res://scenes/objects/goal_flag.tscn")
	if flag_scene:
		var flag_inst = flag_scene.instantiate()
		flag_inst.position = position
		get_parent().add_child(flag_inst)
		
	queue_free()

func _on_hurt_body_entered(body: Node2D) -> void:
	if is_dead:
		return
	if body.is_in_group("player") and body.has_method("take_damage"):
		var knock = -1.0 if position.x > body.position.x else 1.0
		body.take_damage(knock)

