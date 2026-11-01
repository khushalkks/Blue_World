# Blue_World - THE LAST SIGNAL

**THE LAST SIGNAL** is an original 2D atmospheric mystery-adventure PC game developed using **Godot Engine 4.x** and **GDScript**.

---

## 🎮 Concept & Story

You play as **Ellis Parker**, an investigator who intercepts a cryptic radio transmission from missing colleague **Dr. Aris Vance**. The signal leads you into the subterranean depths of the decommissioned **Aethelgard Bio-Acoustics Facility**.

In Sector A, the facility has triggered an emergency quarantine protocol, locking down the primary blast doors to Sub-Level 4. To descend deeper, you must investigate Vance's research fixtures, deduce the 4-digit security override code, and unlock the blast doors.

---

## 🚀 Milestone 1 Features

- **Main Menu**: Interactive title screen with controls guide and game startup.
- **Atmospheric 2D Lighting**: Real-time `PointLight2D` directional flashlight cone, ambient glow, and high-visibility sci-fi laboratory environment.
- **Top-Down Player Physics**: Smooth 8-directional movement with acceleration and friction.
- **Environmental Investigation**: 3 interactive fixtures with narrative lore logs and extracted intel badges:
  - *Vance's Terminal (Log #084)* -> Sector Number (**7**)
  - *Cryo-Resonance Whiteboard* -> Stabilizer (**3**) & Peak (**9**)
  - *Telemetry Oscilloscope* -> Active Transmission Channel (**4**)
- **Cybernetic Keypad Puzzle**: Interactive security keypad supporting mouse clicks and physical keyboard entry, complete with a live **Field Intel Memory Bank** sidebar.
- **Locked Blast Door**: Solid barrier that automatically retracts and switches indicator lights from red to green upon entering `7394`.
- **Mission Debrief Ending**: Narrative victory screen leading into Milestone 2.

---

## 🕹️ Controls

| Action | Key(s) |
|---|---|
| **Move** | `W, A, S, D` or `Arrow Keys` |
| **Interact / Inspect** | `E` or `Space` / `Enter` |
| **Cancel / Menu** | `Esc` |
| **Numpad Input** | Mouse clicks or `0-9`, `Backspace`, `Enter` on keyboard |

---

## 🛠️ How to Run

1. **Direct Game Launch**:
   Run `launch_game.bat` or execute in PowerShell:
   ```powershell
   .\launch_game.bat
   ```
2. **Open in Godot 4 Editor**:
   Run `launch_editor.bat` or open `project.godot` inside Godot Engine 4.x.

---

*Built with Godot Engine 4.x*
