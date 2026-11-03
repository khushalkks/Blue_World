extends Area2D

## Spring Bounce Pad

@onready var sprite: Sprite2D = $Sprite2D

func _ready() -> void:
	body_entered.connect(_on_body_entered)

func _on_body_entered(body: Node2D) -> void:
	if body.is_in_group("player") and body.has_method("spring_launch"):
		body.spring_launch()
		
		# Spring compression & release animation
		var tw = create_tween()
		tw.tween_property(sprite, "scale", Vector2(1.3, 0.4), 0.06)
		tw.tween_property(sprite, "scale", Vector2(0.8, 1.4), 0.12)
		tw.tween_property(sprite, "scale", Vector2.ONE, 0.1)

