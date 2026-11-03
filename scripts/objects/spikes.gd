extends Area2D

## Danger Spikes Hazard

func _ready() -> void:
	add_to_group("hazard")
	body_entered.connect(_on_body_entered)

func _on_body_entered(body: Node2D) -> void:
	if body.is_in_group("player") and body.has_method("take_damage"):
		body.take_damage(0.0)

