extends Node2D

## Rotating Fire Bar Hazard (Bowser Castle classic)

@export var rotation_speed: float = 2.2
@export var orb_count: int = 4
@export var orb_spacing: float = 22.0

var orbs: Array[Area2D] = []

func _ready() -> void:
	var fire_tex = load("res://assets/platformer/fire_orb.png")
	for i in range(1, orb_count + 1):
		var area = Area2D.new()
		area.collision_layer = 32
		area.collision_mask = 1
		area.add_to_group("hazard")
		
		var spr = Sprite2D.new()
		spr.texture = fire_tex
		area.add_child(spr)
		
		var col = CollisionShape2D.new()
		var shape = CircleShape2D.new()
		shape.radius = 9.0
		col.shape = shape
		area.add_child(col)
		
		area.position = Vector2(i * orb_spacing, 0)
		area.body_entered.connect(_on_orb_hit)
		add_child(area)
		orbs.append(area)

func _process(delta: float) -> void:
	rotation += rotation_speed * delta

func _on_orb_hit(body: Node2D) -> void:
	if body.is_in_group("player") and body.has_method("take_damage"):
		body.take_damage(0.0)

