extends CanvasLayer

## High-Contrast Clue Inspection Modal Dialog
## Shows crisp narrative logs, highlighted evidence badges, and extracted intel.

@onready var panel: PanelContainer = $RootControl/CenterContainer/DialogPanel
@onready var title_label: Label = $RootControl/CenterContainer/DialogPanel/MarginContainer/VBoxContainer/Header/TitleLabel
@onready var content_label: RichTextLabel = $RootControl/CenterContainer/DialogPanel/MarginContainer/VBoxContainer/ContentLabel
@onready var intel_label: RichTextLabel = $RootControl/CenterContainer/DialogPanel/MarginContainer/VBoxContainer/IntelPanel/IntelMargin/IntelLabel
@onready var close_button: Button = $RootControl/CenterContainer/DialogPanel/MarginContainer/VBoxContainer/Footer/CloseButton

func _ready() -> void:
	visible = false
	GameState.clue_inspected.connect(_on_clue_inspected)
	close_button.pressed.connect(close_dialog)

func _unhandled_input(event: InputEvent) -> void:
	if not visible:
		return
	if event.is_action_pressed("interact") or event.is_action_pressed("pause"):
		get_viewport().set_input_as_handled()
		close_dialog()

func _on_clue_inspected(title: String, content: String, clue_id: String) -> void:
	title_label.text = title.to_upper()
	content_label.text = content
	
	# Populate clear, high-contrast, story-driven intel summary box
	match clue_id:
		"terminal":
			intel_label.text = "[color=#00e5ff][b]EXTRACTED INTEL [DIGIT 1 OF 4]:[/b][/color] Escaped lifeform was locked in Pod [color=#ffdd44][b]#7[/b][/color]. First code slot is [color=#50fa7b][b]7[/b][/color]."
		"whiteboard":
			intel_label.text = "[color=#00e5ff][b]EXTRACTED INTEL [DIGITS 2 & 3 OF 4]:[/b][/color] Sedative Recipe is [color=#ffdd44][b]3[/b][/color] Blue Vials & [color=#ffdd44][b]9[/b][/color] Gold Dust. Middle slots are [color=#50fa7b][b]3[/b][/color] and [color=#50fa7b][b]9[/b][/color]."
		"bio_shelf":
			intel_label.text = "[color=#00e5ff][b]EXTRACTED INTEL [DIGIT 4 OF 4]:[/b][/color] Vance's active SOS radio distress signal is on Channel [color=#ffdd44][b]4[/b][/color]. Final slot is [color=#50fa7b][b]4[/b][/color]."
		_:
			intel_label.text = "[color=#00e5ff][b]EXTRACTED INTEL:[/b][/color] Intel recorded in field database."
	
	visible = true
	close_button.grab_focus()

func close_dialog() -> void:
	GameState.play_sfx("ui_click", -2.0)
	visible = false
	GameState.set_ui_blocking(false)
