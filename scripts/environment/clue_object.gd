extends Area2D

## Interactive Clue Object in "THE LAST SIGNAL"
## Triggers an inspection modal when the player approaches and presses [E].

@export var clue_id: String = "terminal"
@export var clue_title: String = "Research Log #084"
@export_multiline var clue_content: String = "..."
@export var prompt_text: String = "[E] Inspect"
@export var custom_texture: Texture2D = null
@export var custom_glow_color: Color = Color(0.2, 0.85, 1.0, 1.0)

@onready var sprite: Sprite2D = $Sprite2D
@onready var glow_light: PointLight2D = get_node_or_null("GlowLight")

var is_player_nearby: bool = false
var time_elapsed: float = 0.0

func _ready() -> void:
	if custom_texture and sprite:
		sprite.texture = custom_texture
	if glow_light:
		glow_light.color = custom_glow_color
	
	body_entered.connect(_on_body_entered)
	body_exited.connect(_on_body_exited)

func _process(delta: float) -> void:
	time_elapsed += delta
	# Subtle atmospheric pulse on the clue glow light
	if glow_light:
		glow_light.energy = 0.5 + sin(time_elapsed * 2.5) * 0.15

func _on_body_entered(body: Node2D) -> void:
	if body.is_in_group("player"):
		is_player_nearby = true
		GameState.nearby_interactive = self

func _on_body_exited(body: Node2D) -> void:
	if body.is_in_group("player"):
		is_player_nearby = false
		if GameState.nearby_interactive == self:
			GameState.nearby_interactive = null

func interact() -> void:
	GameState.mark_clue_found(clue_id, clue_title, clue_content)
