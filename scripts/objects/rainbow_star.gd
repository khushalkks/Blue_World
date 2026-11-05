extends Area2D

## Rainbow Invincibility Star
## Grants player temporary invulnerability, speed boost, and enemy insta-destruction!

@onready var sprite: Sprite2D = $Sprite2D
var base_y: float = 0.0
var t: float = 0.0

func _ready() -> void:
	base_y = position.y
	body_entered.connect(_on_body_entered)

func _process(delta: float) -> void:
	t += delta
	position.y = base_y + sin(t * 5.0) * 8.0
	sprite.rotation = sin(t * 4.0) * 0.25
	
	# Rainbow color cycle
	var hue = fmod(t * 1.5, 1.0)
	sprite.modulate = Color.from_hsv(hue, 0.85, 1.3)

func _on_body_entered(body: Node2D) -> void:
	if body.is_in_group("player"):
		GameState.play_sfx("invincible", 3.0)
		GameState.add_score(1000)
		if body.has_method("grant_invincible_power"):
			body.grant_invincible_power(10.0)
			
		set_deferred("monitoring", false)
		var tw := create_tween().set_parallel(true)
		tw.tween_property(self, "scale", Vector2(2.0, 2.0), 0.25)
		tw.tween_property(self, "modulate:a", 0.0, 0.25)
		tw.chain().tween_callback(queue_free)

