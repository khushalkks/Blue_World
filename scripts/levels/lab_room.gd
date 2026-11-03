extends Node2D

## Laboratory Sector A - Main Level Controller
## Handles room initialization, ambient lighting, HUD clue counter, and audio/visual cues.

@onready var hud_clue_counter: Label = $HUD/ClueTrackerLabel
@onready var hud_status_banner: Label = $HUD/StatusBannerLabel

func _ready() -> void:
	GameState.play_bgm("ambient", -6.0)
	GameState.clue_inspected.connect(_on_clue_inspected)
	GameState.puzzle_solved.connect(_on_puzzle_solved)
	_update_hud()
	
	if hud_status_banner:
		hud_status_banner.visible = true
		hud_status_banner.text = "MISSION: INSPECT 3 LAB STATIONS TO DECODE BLAST DOOR PASSCODE"
		await get_tree().create_timer(5.0).timeout
		if is_instance_valid(hud_status_banner) and not GameState.is_puzzle_solved:
			hud_status_banner.visible = false

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("pause") and not GameState.is_ui_blocking:
		GameState.return_to_main_menu()

func _on_clue_inspected(_title: String, _content: String, _id: String) -> void:
	_update_hud()

func _update_hud() -> void:
	if hud_clue_counter:
		var found_count: int = 0
		for k in GameState.clues_discovered:
			if GameState.clues_discovered[k]:
				found_count += 1
		hud_clue_counter.text = "RESEARCH INTEL: %d / 3 CLUES ANALYZED" % found_count

func _on_puzzle_solved() -> void:
	if hud_status_banner:
		hud_status_banner.visible = true
		hud_status_banner.text = ">> SECURITY BLAST DOOR UNLOCKED - PROCEED TO EXIT <<"
		hud_status_banner.modulate = Color(0.2, 1.0, 0.4)
