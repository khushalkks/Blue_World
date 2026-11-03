extends StaticBody2D

## Mario-style Question Block (?)
## When hit from below, bumps up, dispenses a coin, and becomes an empty block.

@onready var sprite: Sprite2D = $Sprite2D
@onready var bottom_area: Area2D = $BottomHitArea

var empty_tex: Texture2D = null
var is_spent: bool = false
var base_pos: Vector2 = Vector2.ZERO

func _ready() -> void:
	base_pos = position
	empty_tex = load("res://assets/platformer/block_empty.png")
	if bottom_area:
		bottom_area.body_entered.connect(_on_bottom_entered)

func _on_bottom_entered(body: Node2D) -> void:
	if is_spent:
		return
	if body.is_in_group("player") and body.velocity.y < 0.0:
		bump()

func bump() -> void:
	if is_spent:
		return
	is_spent = true
	GameState.play_sfx("block", 0.0)
	
	# Block bump animation
	var tw = create_tween()
	tw.tween_property(self, "position:y", base_pos.y - 12.0, 0.08).set_trans(Tween.TRANS_QUAD).set_ease(Tween.EASE_OUT)
	tw.tween_property(self, "position:y", base_pos.y, 0.08).set_trans(Tween.TRANS_QUAD).set_ease(Tween.EASE_IN)
	
	# Switch to empty texture
	if empty_tex:
		sprite.texture = empty_tex
		
	# Pop out coin
	_spawn_coin_popup()

func _spawn_coin_popup() -> void:
	GameState.add_coin(1)
	var coin_sprite = Sprite2D.new()
	coin_sprite.texture = load("res://assets/platformer/coin.png")
	coin_sprite.position = Vector2(0, -20)
	add_child(coin_sprite)
	
	var c_tw = create_tween().set_parallel(true)
	c_tw.tween_property(coin_sprite, "position:y", -60.0, 0.35).set_trans(Tween.TRANS_QUAD).set_ease(Tween.EASE_OUT)
	c_tw.chain().tween_property(coin_sprite, "position:y", -24.0, 0.2).set_trans(Tween.TRANS_QUAD).set_ease(Tween.EASE_IN)
	c_tw.parallel().tween_property(coin_sprite, "modulate:a", 0.0, 0.25).set_delay(0.3)
	await c_tw.finished
	coin_sprite.queue_free()

