extends Area2D

## Floating Collectible Gold Coin

@export var coin_value: int = 1

var time_offset: float = 0.0
var base_y: float = 0.0
var is_collected: bool = false

@onready var sprite: Sprite2D = $Sprite2D

func _ready() -> void:
	add_to_group("coin")
	base_y = position.y
	time_offset = randf() * 10.0
	body_entered.connect(_on_body_entered)

func _process(delta: float) -> void:
	if not is_collected:
		var t = Time.get_ticks_msec() / 1000.0 + time_offset
		# Magnetic attraction to player
		var player = get_tree().get_first_node_in_group("player")
		if player and "has_magnet_power" in player and player.has_magnet_power:
			var dist: float = global_position.distance_to(player.global_position)
			if dist < player.magnet_radius:
				var pull_dir = (player.global_position - global_position).normalized()
				var speed = lerpf(680.0, 300.0, dist / player.magnet_radius)
				global_position += pull_dir * speed * delta
				base_y = position.y
		
		position.y = base_y + sin(t * 5.0) * 4.0
		# Coin 3D spin effect by scaling X
		sprite.scale.x = sin(t * 7.0)

func _on_body_entered(body: Node2D) -> void:
	if is_collected:
		return
	if body.is_in_group("player"):
		collect()

func collect() -> void:
	is_collected = true
	GameState.add_coin(coin_value)
	
	# Pop upward animation and fade out
	var tw = create_tween().set_parallel(true)
	tw.tween_property(self, "position:y", position.y - 36.0, 0.3).set_trans(Tween.TRANS_QUAD).set_ease(Tween.EASE_OUT)
	tw.tween_property(self, "modulate:a", 0.0, 0.3)
	tw.tween_property(self, "scale", Vector2(1.5, 1.5), 0.3)
	await tw.finished
	queue_free()

