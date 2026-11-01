extends Node

## Central GameState Singleton for "THE LAST SIGNAL"
## Manages global puzzle status, inventory/clues, and input registration.

signal puzzle_solved
signal clue_inspected(title: String, content: String, clue_id: String)
signal keypad_opened
signal ui_state_changed(is_open: bool)

# Story / Puzzle Data
const CORRECT_PASSCODE: String = "7394"
var is_puzzle_solved: bool = false
var clues_discovered: Dictionary = {
	"terminal": false,
	"whiteboard": false,
	"bio_shelf": false
}

# UI & Interaction Tracking
var is_ui_blocking: bool = false
var nearby_interactive: Node = null

func _ready() -> void:
	process_mode = Node.PROCESS_MODE_ALWAYS
	_setup_default_input_actions()

## Ensure required input actions are dynamically registered in Godot's InputMap
## so the game responds smoothly to WASD, Arrow keys, E, and Escape right away.
func _setup_default_input_actions() -> void:
	var default_actions: Dictionary = {
		"move_left": [KEY_A, KEY_LEFT],
		"move_right": [KEY_D, KEY_RIGHT],
		"move_up": [KEY_W, KEY_UP],
		"move_down": [KEY_S, KEY_DOWN],
		"interact": [KEY_E, KEY_SPACE, KEY_ENTER],
		"pause": [KEY_ESCAPE]
	}
	
	for action in default_actions:
		if not InputMap.has_action(action):
			InputMap.add_action(action)
		for keycode in default_actions[action]:
			var event := InputEventKey.new()
			event.physical_keycode = keycode
			# Only add if not already registered
			var existing := InputMap.action_get_events(action)
			var already_has: bool = false
			for e in existing:
				if e is InputEventKey and e.physical_keycode == keycode:
					already_has = true
					break
			if not already_has:
				InputMap.action_add_event(action, event)

func mark_clue_found(clue_id: String, title: String, content: String) -> void:
	clues_discovered[clue_id] = true
	clue_inspected.emit(title, content, clue_id)
	set_ui_blocking(true)

func verify_code(entered_code: String) -> bool:
	if entered_code == CORRECT_PASSCODE:
		is_puzzle_solved = true
		puzzle_solved.emit()
		return true
	return false

func set_ui_blocking(blocking: bool) -> void:
	is_ui_blocking = blocking
	ui_state_changed.emit(blocking)

func reset_progress() -> void:
	is_puzzle_solved = false
	clues_discovered = {
		"terminal": false,
		"whiteboard": false,
		"bio_shelf": false
	}
	is_ui_blocking = false
	nearby_interactive = null

func start_new_game() -> void:
	reset_progress()
	get_tree().change_scene_to_file("res://scenes/levels/lab_room.tscn")

func trigger_ending() -> void:
	get_tree().change_scene_to_file("res://scenes/ui/ending_screen.tscn")

func return_to_main_menu() -> void:
	reset_progress()
	get_tree().change_scene_to_file("res://scenes/ui/main_menu.tscn")
