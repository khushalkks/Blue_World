extends Node

## Global GameState Singleton for "SUPER BLUE RUNNER"
## Manages score, coins, lives, level progression, and audio playback.

signal stats_changed
signal level_completed(level_num: int)
signal game_over
signal game_won

var score: int = 0
var coins: int = 0
var lives: int = 3
var max_lives: int = 3
var current_level: int = 1
var total_levels: int = 3
var unlocked_level: int = 1

# Audio
var sfx_player: AudioStreamPlayer = null
var bgm_player: AudioStreamPlayer = null
var audio_streams: Dictionary = {}

func _ready() -> void:
	process_mode = Node.PROCESS_MODE_ALWAYS
	_setup_inputs()
	_setup_audio()

func _setup_inputs() -> void:
	var mapping := {
		"move_left": [KEY_A, KEY_LEFT],
		"move_right": [KEY_D, KEY_RIGHT],
		"move_up": [KEY_W, KEY_UP],
		"move_down": [KEY_S, KEY_DOWN],
		"jump": [KEY_SPACE, KEY_W, KEY_UP],
		"pause": [KEY_ESCAPE]
	}
	
	for action in mapping:
		if not InputMap.has_action(action):
			InputMap.add_action(action)
		for code in mapping[action]:
			var ev := InputEventKey.new()
			ev.physical_keycode = code
			var existing := InputMap.action_get_events(action)
			var has_it := false
			for e in existing:
				if e is InputEventKey and e.physical_keycode == code:
					has_it = true
					break
			if not has_it:
				InputMap.action_add_event(action, ev)

func _setup_audio() -> void:
	sfx_player = AudioStreamPlayer.new()
	sfx_player.name = "SFX"
	add_child(sfx_player)
	
	bgm_player = AudioStreamPlayer.new()
	bgm_player.name = "BGM"
	add_child(bgm_player)
	
	var files := {
		"jump": "res://assets/audio/mario_jump.wav",
		"coin": "res://assets/audio/mario_coin.wav",
		"stomp": "res://assets/audio/mario_stomp.wav",
		"block": "res://assets/audio/mario_block.wav",
		"spring": "res://assets/audio/mario_spring.wav",
		"hurt": "res://assets/audio/mario_hurt.wav",
		"clear": "res://assets/audio/mario_clear.wav",
		"bgm": "res://assets/audio/mario_bgm.wav"
	}
	
	for k in files:
		if ResourceLoader.exists(files[k]):
			audio_streams[k] = load(files[k])

func play_sfx(s_name: String, vol_db: float = 0.0, pitch: float = 1.0) -> void:
	if audio_streams.has(s_name) and sfx_player:
		sfx_player.stream = audio_streams[s_name]
		sfx_player.volume_db = vol_db
		sfx_player.pitch_scale = pitch
		sfx_player.play()

func play_bgm(m_name: String = "bgm", vol_db: float = -6.0) -> void:
	if audio_streams.has(m_name) and bgm_player:
		if bgm_player.stream != audio_streams[m_name] or not bgm_player.playing:
			bgm_player.stream = audio_streams[m_name]
			bgm_player.volume_db = vol_db
			bgm_player.play()

func stop_bgm() -> void:
	if bgm_player and bgm_player.playing:
		bgm_player.stop()

func add_coin(amount: int = 1) -> void:
	coins += amount
	score += amount * 100
	play_sfx("coin", -2.0)
	# 100 coins = extra life!
	if coins >= 100:
		coins -= 100
		lives = mini(lives + 1, max_lives)
		play_sfx("clear", 0.0)
	stats_changed.emit()

func add_score(amount: int) -> void:
	score += amount
	stats_changed.emit()

func take_damage() -> bool:
	lives -= 1
	play_sfx("hurt", 2.0)
	stats_changed.emit()
	if lives <= 0:
		handle_game_over()
		return true
	return false

func handle_game_over() -> void:
	stop_bgm()
	game_over.emit()
	get_tree().change_scene_to_file("res://scenes/ui/platform_game_over.tscn")

func win_level() -> void:
	stop_bgm()
	play_sfx("clear", 3.0)
	add_score(1000 * current_level)
	level_completed.emit(current_level)
	
	if current_level >= total_levels:
		unlocked_level = total_levels
		get_tree().change_scene_to_file("res://scenes/ui/platform_win.tscn")
	else:
		unlocked_level = maxi(unlocked_level, current_level + 1)
		get_tree().change_scene_to_file("res://scenes/ui/platform_level_clear.tscn")

func next_level() -> void:
	current_level += 1
	load_level(current_level)

func restart_current_level() -> void:
	load_level(current_level)

func start_new_game() -> void:
	score = 0
	coins = 0
	lives = 3
	current_level = 1
	stats_changed.emit()
	load_level(1)

func load_level(lvl: int) -> void:
	current_level = lvl
	var path := "res://scenes/levels/platform_level_%d.tscn" % lvl
	if ResourceLoader.exists(path):
		get_tree().change_scene_to_file(path)
	else:
		get_tree().change_scene_to_file("res://scenes/levels/platform_level_1.tscn")

func return_to_menu() -> void:
	stop_bgm()
	get_tree().change_scene_to_file("res://scenes/ui/platform_main_menu.tscn")
