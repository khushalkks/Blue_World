extends CharacterBody2D

## Player controller for "THE LAST SIGNAL"
## Features smooth top-down physics movement, directional flashlight,
## and context-sensitive interaction prompt.

@export var move_speed: float = 190.0
@export var acceleration: float = 1400.0
@export var friction: float = 1200.0

@onready var sprite: Sprite2D = $Sprite2D
@onready var flashlight: PointLight2D = $FlashlightLight
@onready var prompt_label: Label = $PromptLabel

var facing_direction: Vector2 = Vector2.DOWN
var step_timer: float = 0.0
var step_toggle: bool = false

func _ready() -> void:
	add_to_group("player")
	if prompt_label:
		prompt_label.visible = false

func _physics_process(delta: float) -> void:
	# If a modal UI dialog or puzzle keypad is open, freeze movement
	if GameState.is_ui_blocking:
		velocity = velocity.move_toward(Vector2.ZERO, friction * delta)
		move_and_slide()
		return
	
	# Fetch input vector (WASD or Arrow Keys)
	var input_vec: Vector2 = Input.get_vector("move_left", "move_right", "move_up", "move_down")
	
	if input_vec != Vector2.ZERO:
		velocity = velocity.move_toward(input_vec * move_speed, acceleration * delta)
		facing_direction = input_vec.normalized()
		_update_facing(facing_direction)
		
		# Play soft footsteps while moving
		step_timer += delta
		if step_timer >= 0.35:
			step_timer = 0.0
			step_toggle = not step_toggle
			GameState.play_sfx("footstep1" if step_toggle else "footstep2", -12.0, randf_range(0.92, 1.08))
	else:
		velocity = velocity.move_toward(Vector2.ZERO, friction * delta)
		step_timer = 0.28 # Ready for immediate first step when resuming
	
	move_and_slide()
	_handle_interaction()

func _update_facing(dir: Vector2) -> void:
	# Point the flashlight towards the facing vector
	# In our light_cone texture, beam points straight Up (-Y), so angle from -Y is dir.angle() + PI/2
	if flashlight:
		flashlight.rotation = dir.angle() + (PI / 2.0)
	
	# Visual rotation / tilt of the investigator sprite
	if sprite:
		sprite.rotation = lerp_angle(sprite.rotation, dir.angle() + (PI / 2.0), 0.25)

func _handle_interaction() -> void:
	if GameState.nearby_interactive != null and not GameState.is_ui_blocking:
		if prompt_label:
			prompt_label.visible = true
			prompt_label.text = GameState.nearby_interactive.prompt_text
		
		if Input.is_action_just_pressed("interact"):
			GameState.nearby_interactive.interact()
	else:
		if prompt_label:
			prompt_label.visible = false
