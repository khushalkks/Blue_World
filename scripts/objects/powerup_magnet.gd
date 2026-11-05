extends Area2D

## Coin Magnet Power-Up
## Collect to activate magnetic field that draws all nearby coins to the player!

@onready var sprite: Sprite2D = $Sprite2D
var start_y: float = 0.0
var t: float = 0.0

func _ready() -> void:
	start_y = position.y
	body_entered.connect(_on_body_entered)

func _process(delta: float) -> void:
	t += delta
	position.y = start_y + sin(t * 4.0) * 5.0
	if sprite:
		# Electric spark pulse
		sprite.scale = Vector2.ONE * (1.0 + sin(t * 8.0) * 0.08)

func _on_body_entered(body: Node2D) -> void:
	if body.is_in_group("player"):
		GameState.play_sfx("magnet", 2.0)
		GameState.add_score(500)
		if body.has_method("grant_magnet_power"):
			body.grant_magnet_power(12.0)
		
		# Pickup pop animation
		set_deferred("monitoring", false)
		var tw := create_tween().set_parallel(true)
		tw.tween_property(self, "scale", Vector2(1.8, 1.8), 0.2)
		tw.tween_property(self, "modulate:a", 0.0, 0.2)
		tw.chain().tween_callback(queue_free)

