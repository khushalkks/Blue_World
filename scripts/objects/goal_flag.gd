extends Area2D

## Victory Flagpole (Level Exit Gate)

@onready var sprite: Sprite2D = $Sprite2D

var is_reached: bool = false

func _ready() -> void:
	body_entered.connect(_on_body_entered)

func _on_body_entered(body: Node2D) -> void:
	if is_reached:
		return
	if body.is_in_group("player"):
		is_reached = true
		
		# Flag celebrate effect
		var tw = create_tween().set_parallel(true)
		tw.tween_property(sprite, "scale", Vector2(1.2, 1.2), 0.2)
		tw.chain().tween_property(sprite, "scale", Vector2.ONE, 0.2)
		
		# Freeze player
		if "velocity" in body:
			body.velocity = Vector2.ZERO
		
		GameState.win_level()

