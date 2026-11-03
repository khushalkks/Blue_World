extends Control

## Main Menu Controller for "THE LAST SIGNAL"
## Features atmospheric backdrop, glowing title, how-to-play modal, and scene launching.

@onready var new_game_btn: Button = $VBoxContainer/NewGameButton
@onready var how_to_play_btn: Button = $VBoxContainer/HowToPlayButton
@onready var quit_btn: Button = $VBoxContainer/QuitButton
@onready var how_to_play_panel: PanelContainer = $HowToPlayPanel
@onready var close_help_btn: Button = $HowToPlayPanel/MarginContainer/VBoxContainer/CloseHelpButton
@onready var title_label: Label = $TitleContainer/TitleLabel

var time_elapsed: float = 0.0

func _ready() -> void:
	GameState.play_bgm("ambient", -8.0)
	how_to_play_panel.visible = false
	new_game_btn.pressed.connect(_on_new_game_pressed)
	how_to_play_btn.pressed.connect(_on_how_to_play_pressed)
	quit_btn.pressed.connect(_on_quit_pressed)
	close_help_btn.pressed.connect(_on_close_help_pressed)
	
	new_game_btn.mouse_entered.connect(func(): GameState.play_sfx("ui_hover", -6.0))
	how_to_play_btn.mouse_entered.connect(func(): GameState.play_sfx("ui_hover", -6.0))
	quit_btn.mouse_entered.connect(func(): GameState.play_sfx("ui_hover", -6.0))
	close_help_btn.mouse_entered.connect(func(): GameState.play_sfx("ui_hover", -6.0))
	
	new_game_btn.grab_focus()

func _process(delta: float) -> void:
	time_elapsed += delta
	# Subtle atmospheric pulse on title glow
	var pulse := 0.85 + sin(time_elapsed * 2.0) * 0.15
	title_label.modulate = Color(pulse, pulse * 0.9, 1.0)

func _on_new_game_pressed() -> void:
	GameState.play_sfx("power_surge", -2.0)
	GameState.start_new_game()

func _on_how_to_play_pressed() -> void:
	GameState.play_sfx("ui_click")
	how_to_play_panel.visible = true
	close_help_btn.grab_focus()

func _on_close_help_pressed() -> void:
	GameState.play_sfx("ui_click")
	how_to_play_panel.visible = false
	new_game_btn.grab_focus()

func _on_quit_pressed() -> void:
	GameState.play_sfx("switch_flip")
	get_tree().quit()
