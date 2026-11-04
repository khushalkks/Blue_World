extends Area2D

## Power-Up Star (Grants Player Plasma Fireball Blaster Ability!)

@onready var sprite: Sprite2D = $Sprite2D

var time_offset: float = 0.0
var base_y: float = 0.0

func _ready() -> void:
	base_y = position.y
	time_offset = randf() * 5.0
	body_entered.connect(_on_body_entered)

func _process(delta: float) -> void:
	var t = Time.get_ticks_msec() / 1000.0 + time_offset
	position.y = base_y + sin(t * 4.0) * 6.0
	sprite.rotation = sin(t * 3.0) * 0.2

func _on_body_entered(body: Node2D) -> void:
	if body.is_in_group("player"):
		GameState.play_sfx("powerup", 2.0)
		GameState.add_score(500)
		if body.has_method("grant_plasma_power"):
			body.grant_plasma_power()
			
		var tw = create_tween().set_parallel(true)
		tw.tween_property(self, "scale", Vector2(1.8, 1.8), 0.25)
		tw.tween_property(self, "modulate:a", 0.0, 0.25)
		await tw.finished
		queue_free()

