extends Control

## Main Menu for "SUPER BLUE RUNNER"

@onready var title_label: Label = $CenterContainer/VBoxContainer/TitleContainer/TitleLabel
@onready var start_btn: Button = $CenterContainer/VBoxContainer/MenuVBox/StartButton
@onready var lvl1_btn: Button = $CenterContainer/VBoxContainer/MenuVBox/LevelSelectHBox/Level1Btn
@onready var lvl2_btn: Button = $CenterContainer/VBoxContainer/MenuVBox/LevelSelectHBox/Level2Btn
@onready var lvl3_btn: Button = $CenterContainer/VBoxContainer/MenuVBox/LevelSelectHBox/Level3Btn
@onready var help_btn: Button = $CenterContainer/VBoxContainer/MenuVBox/HelpButton
@onready var quit_btn: Button = $CenterContainer/VBoxContainer/MenuVBox/QuitButton
@onready var help_dialog: PanelContainer = $HelpDialog
@onready var close_help_btn: Button = $HelpDialog/MarginContainer/VBoxContainer/CloseHelpBtn

var time_elapsed: float = 0.0

func _ready() -> void:
	help_dialog.visible = false
	GameState.play_bgm("bgm", -6.0)
	
	start_btn.pressed.connect(_on_start_pressed)
	lvl1_btn.pressed.connect(func(): _load_level(1))
	lvl2_btn.pressed.connect(func(): _load_level(2))
	lvl3_btn.pressed.connect(func(): _load_level(3))
	help_btn.pressed.connect(_on_help_pressed)
	quit_btn.pressed.connect(func(): get_tree().quit())
	close_help_btn.pressed.connect(func(): help_dialog.visible = false)
	
	start_btn.grab_focus()

func _process(delta: float) -> void:
	time_elapsed += delta
	# Title bounce / glow pulsation
	var s := 1.0 + sin(time_elapsed * 3.0) * 0.04
	title_label.scale = Vector2(s, s)

func _on_start_pressed() -> void:
	GameState.play_sfx("jump")
	GameState.start_new_game()

func _load_level(lvl: int) -> void:
	GameState.play_sfx("jump")
	GameState.score = 0
	GameState.coins = 0
	GameState.lives = 3
	GameState.load_level(lvl)

func _on_help_pressed() -> void:
	GameState.play_sfx("block")
	help_dialog.visible = true
	close_help_btn.grab_focus()

