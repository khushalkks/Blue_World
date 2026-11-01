extends CanvasLayer

## Interactive 4-Digit Security Keypad Modal with Live Intel Memory Bank
## Supports mouse button clicks and physical keyboard entry (0-9, Backspace, Enter, Esc).

@onready var display_label: Label = $RootControl/CenterContainer/KeypadPanel/MarginContainer/HBoxRoot/KeypadVBox/DisplayPanel/DisplayLabel
@onready var status_label: Label = $RootControl/CenterContainer/KeypadPanel/MarginContainer/HBoxRoot/KeypadVBox/StatusLabel
@onready var keypad_grid: GridContainer = $RootControl/CenterContainer/KeypadPanel/MarginContainer/HBoxRoot/KeypadVBox/KeypadGrid
@onready var close_button: Button = $RootControl/CenterContainer/KeypadPanel/MarginContainer/HBoxRoot/KeypadVBox/CloseButton
@onready var intel_readout: RichTextLabel = $RootControl/CenterContainer/KeypadPanel/MarginContainer/HBoxRoot/IntelVBox/IntelCard/IntelCardMargin/IntelReadout

var current_input: String = ""
var max_digits: int = 4
var is_submitting: bool = false

func _ready() -> void:
	visible = false
	GameState.keypad_opened.connect(_on_keypad_opened)
	close_button.pressed.connect(close_keypad)
	
	# Connect keypad number buttons dynamically
	for child in keypad_grid.get_children():
		if child is Button:
			var btn_text: String = child.text
			if btn_text in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
				child.pressed.connect(func(): _press_digit(btn_text))
			elif btn_text == "CLEAR":
				child.pressed.connect(_clear_input)
			elif btn_text == "ENTER":
				child.pressed.connect(_submit_code)

func _unhandled_input(event: InputEvent) -> void:
	if not visible or is_submitting:
		return
	
	if event is InputEventKey and event.pressed and not event.echo:
		if event.physical_keycode >= KEY_0 and event.physical_keycode <= KEY_9:
			var digit_str: String = str(event.physical_keycode - KEY_0)
			_press_digit(digit_str)
			get_viewport().set_input_as_handled()
		elif event.physical_keycode >= KEY_KP_0 and event.physical_keycode <= KEY_KP_9:
			var digit_str: String = str(event.physical_keycode - KEY_KP_0)
			_press_digit(digit_str)
			get_viewport().set_input_as_handled()
		elif event.physical_keycode == KEY_BACKSPACE:
			_backspace()
			get_viewport().set_input_as_handled()
		elif event.physical_keycode == KEY_ENTER or event.physical_keycode == KEY_KP_ENTER:
			_submit_code()
			get_viewport().set_input_as_handled()
		elif event.physical_keycode == KEY_ESCAPE:
			close_keypad()
			get_viewport().set_input_as_handled()

func _on_keypad_opened() -> void:
	current_input = ""
	is_submitting = false
	status_label.text = "ENTER 4-DIGIT SECURITY OVERRIDE"
	status_label.modulate = Color(0.8, 0.9, 1.0)
	display_label.modulate = Color(0.1, 1.0, 0.65)
	_update_display()
	_update_intel_bank()
	visible = true

func _update_intel_bank() -> void:
	var text := "[b]DECRYPTED FIELD INTEL:[/b]\n\n"
	
	var has_t: bool = bool(GameState.clues_discovered.get("terminal", false))
	var has_w: bool = bool(GameState.clues_discovered.get("whiteboard", false))
	var has_b: bool = bool(GameState.clues_discovered.get("bio_shelf", false))
	
	if has_t:
		text += "[color=#50fa7b][b]• CLUE 1 (Vance Terminal):[/b][/color]\n  Sector Number is [color=#ffdd44][b]7[/b][/color] (Digit 1 = [b]7[/b])\n\n"
	else:
		text += "[color=#667799]• CLUE 1: Unanalyzed (Check terminal)[/color]\n\n"
		
	if has_w:
		text += "[color=#50fa7b][b]• CLUE 2 (Cryo Whiteboard):[/b][/color]\n  Stabilizer [color=#ffdd44][b]3[/b][/color] & Peak [color=#ffdd44][b]9[/b][/color] (Digits 2, 3 = [b]3[/b], [b]9[/b])\n\n"
	else:
		text += "[color=#667799]• CLUE 2: Unanalyzed (Check whiteboard)[/color]\n\n"
		
	if has_b:
		text += "[color=#50fa7b][b]• CLUE 3 (Audio Console):[/b][/color]\n  Active Telemetry Channel [color=#ffdd44][b]4[/b][/color] (Digit 4 = [b]4[/b])\n\n"
	else:
		text += "[color=#667799]• CLUE 3: Unanalyzed (Check console)[/color]\n\n"
	
	var all_found: bool = has_t and has_w and has_b
	if all_found:
		text += "[color=#00e5ff][b]>>> OVERRIDE SEQUENCE DEDUCED <<<[/b][/color]\n[color=#50fa7b][b]CODE: 7  3  9  4[/b][/color]"
	else:
		text += "[color=#ffb86c][i]Tip: Inspect all 3 lab fixtures to confirm the full code.[/i][/color]"
		
	intel_readout.text = text

func _press_digit(d: String) -> void:
	if is_submitting or current_input.length() >= max_digits:
		return
	current_input += d
	_update_display()

func _backspace() -> void:
	if is_submitting or current_input.is_empty():
		return
	current_input = current_input.substr(0, current_input.length() - 1)
	_update_display()

func _clear_input() -> void:
	if is_submitting:
		return
	current_input = ""
	_update_display()

func _update_display() -> void:
	var display_str: String = ""
	for i in range(max_digits):
		if i < current_input.length():
			display_str += current_input[i] + "  "
		else:
			display_str += "_  "
	display_label.text = "[ " + display_str.strip_edges() + " ]"

func _submit_code() -> void:
	if is_submitting or current_input.length() != max_digits:
		status_label.text = "CODE REQUIRES EXACTLY 4 DIGITS"
		status_label.modulate = Color(1.0, 0.8, 0.3)
		return
	
	is_submitting = true
	if GameState.verify_code(current_input):
		status_label.text = ">> ACCESS GRANTED <<\nBLAST DOORS UNLOCKED"
		status_label.modulate = Color(0.2, 1.0, 0.4)
		display_label.modulate = Color(0.2, 1.0, 0.4)
		
		await get_tree().create_timer(1.2).timeout
		close_keypad()
	else:
		status_label.text = ">> ACCESS DENIED <<\nINVALID PASSCODE"
		status_label.modulate = Color(1.0, 0.25, 0.25)
		display_label.modulate = Color(1.0, 0.25, 0.25)
		
		await get_tree().create_timer(1.0).timeout
		current_input = ""
		display_label.modulate = Color(0.1, 1.0, 0.65)
		status_label.modulate = Color(0.8, 0.9, 1.0)
		status_label.text = "ENTER 4-DIGIT SECURITY OVERRIDE"
		_update_display()
		is_submitting = false

func close_keypad() -> void:
	visible = false
	GameState.set_ui_blocking(false)
