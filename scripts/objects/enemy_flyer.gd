extends Area2D

## Flying Bat/Beetle Enemy (Sine-wave flight, stompable)

@export var fly_speed: float = 90.0
@export var wave_amplitude: float = 30.0
@export var wave_frequency: float = 3.5
@export var patrol_range: float = 240.0

@onready var sprite: Sprite2D = $Sprite2D
@onready var stomp_zone: Area2D = $StompZone

var start_x: float = 0.0
var base_y: float = 0.0
var dir: float = 1.0
var is_dead: bool = false

func _ready() -> void:
	add_to_group("enemy")
	start_x = position.x
	base_y = position.y
	if stomp_zone:
		stomp_zone.add_to_group("stompable")
	body_entered.connect(_on_body_entered)

func _process(delta: float) -> void:
	if is_dead:
		return
		
	var t = Time.get_ticks_msec() / 1000.0
	position.x += dir * fly_speed * delta
	position.y = base_y + sin(t * wave_frequency) * wave_amplitude
	
	if abs(position.x - start_x) >= patrol_range:
		dir = -dir
		sprite.flip_h = dir < 0.0

func die_from_stomp() -> void:
	if is_dead:
		return
	is_dead = true
	GameState.play_sfx("stomp", 2.0)
	GameState.add_score(300)
	
	# Falling defeat animation
	var tw = create_tween().set_parallel(true)
	tw.tween_property(self, "position:y", position.y + 120.0, 0.4).set_trans(Tween.TRANS_QUAD).set_ease(Tween.EASE_IN)
	tw.tween_property(sprite, "rotation", 3.14, 0.4)
	tw.tween_property(self, "modulate:a", 0.0, 0.4)
	await tw.finished
	queue_free()

func _on_body_entered(body: Node2D) -> void:
	if is_dead:
		return
	if body.is_in_group("player") and body.has_method("take_damage"):
		var knock = -1.0 if position.x > body.position.x else 1.0
		body.take_damage(knock)

