extends Area2D

## Checkpoint Flag
## Saves player respawn point for the current level with a celebratory chime.

var is_activated: bool = false
@onready var sprite: Sprite2D = $Sprite2D
@onready var anim_tween: Tween = null

func _ready() -> void:
	add_to_group("checkpoint")
	body_entered.connect(_on_body_entered)
	
	# If this level already has this checkpoint active, show green
	if GameState.checkpoint_level == GameState.current_level and GameState.checkpoint_position.distance_to(global_position) < 30.0:
		is_activated = true
		if sprite:
			sprite.modulate = Color(0.2, 1.4, 0.6, 1.0)

func _on_body_entered(body: Node2D) -> void:
	if not is_activated and body.is_in_group("player"):
		activate()

func activate() -> void:
	is_activated = true
	GameState.set_checkpoint(global_position + Vector2(0, -16), GameState.current_level)
	
	# Visual flare: flash and turn glowing neon green
	if sprite:
		var tw := create_tween().set_parallel(true)
		tw.tween_property(sprite, "modulate", Color(0.3, 1.5, 0.6, 1.0), 0.3)
		tw.tween_property(sprite, "scale", Vector2(1.25, 1.25), 0.15).set_trans(Tween.TRANS_BACK)
		tw.chain().tween_property(sprite, "scale", Vector2(1.0, 1.0), 0.2)

