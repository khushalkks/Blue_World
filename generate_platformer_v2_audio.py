import os
import math
import wave
import struct

os.makedirs("assets/audio", exist_ok=True)
SAMPLE_RATE = 44100

def write_wav(filename, samples, sample_rate=SAMPLE_RATE):
    filepath = os.path.join("assets/audio", filename)
    with wave.open(filepath, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        packed = bytearray()
        for s in samples:
            val = max(-32767, min(32767, int(s * 32767)))
            packed.extend(struct.pack("<h", val))
        wf.writeframes(packed)
    print(f"Generated: {filepath} ({len(samples)} samples)")

# 1. Pipe Warp / Downward Slide (mario_pipe.wav)
# Classic stepped descending tone glide
dur = 0.42
samples = []
total_frames = int(dur * SAMPLE_RATE)
steps = [330.0, 260.0, 205.0, 155.0]
step_len = total_frames // len(steps)
for i in range(total_frames):
    step_idx = min(i // step_len, len(steps) - 1)
    base_freq = steps[step_idx]
    t = float(i) / SAMPLE_RATE
    # Slight micro downward vibrato
    freq = base_freq * (1.0 - 0.08 * ((i % step_len) / float(step_len)))
    # Warm square-sine blend
    val = (math.sin(2.0 * math.pi * freq * t) * 0.5 + 
           (1.0 if math.sin(2.0 * math.pi * freq * t) > 0 else -1.0) * 0.15)
    env = 1.0 - (float(i) / total_frames) * 0.3
    samples.append(val * env * 0.6)
write_wav("mario_pipe.wav", samples)

# 2. Checkpoint Fanfare (mario_checkpoint.wav)
# Ascending bright chime: C5 (523Hz), E5 (659Hz), G5 (784Hz), C6 (1046Hz)
dur = 0.55
samples = []
notes = [523.25, 659.25, 783.99, 1046.50]
note_frames = int(dur * SAMPLE_RATE / len(notes))
for note_idx, note_freq in enumerate(notes):
    for i in range(note_frames):
        t = float(i) / SAMPLE_RATE
        val = math.sin(2.0 * math.pi * note_freq * t) * 0.5 + math.sin(4.0 * math.pi * note_freq * t) * 0.25
        env = math.exp(-t * 8.0) if note_idx < len(notes) - 1 else math.exp(-t * 4.0)
        samples.append(val * env * 0.65)
write_wav("mario_checkpoint.wav", samples)

# 3. Cannon Launch Blast (mario_cannon.wav)
# Heavy acoustic kick boom + propellant whoosh
dur = 0.38
samples = []
total_frames = int(dur * SAMPLE_RATE)
for i in range(total_frames):
    t = float(i) / SAMPLE_RATE
    freq = 140.0 * math.exp(-t * 14.0) + 40.0
    bass = math.sin(2.0 * math.pi * freq * t) * 0.65
    noise = ((i * 12347 % 1000) / 500.0 - 1.0) * 0.35 * math.exp(-t * 12.0)
    samples.append((bass + noise) * (1.0 - t / dur))
write_wav("mario_cannon.wav", samples)

# 4. Combo Kill Ding (mario_combo.wav)
# High crystalline ping with shimmering harmonic
dur = 0.25
samples = []
total_frames = int(dur * SAMPLE_RATE)
for i in range(total_frames):
    t = float(i) / SAMPLE_RATE
    freq = 1200.0 + t * 400.0
    val = (math.sin(2.0 * math.pi * freq * t) * 0.4 + 
           math.sin(4.0 * math.pi * freq * t) * 0.3 + 
           math.sin(6.0 * math.pi * freq * t) * 0.15)
    env = math.exp(-t * 10.0)
    samples.append(val * env * 0.6)
write_wav("mario_combo.wav", samples)

# 5. Magnet Hum / Electric Chime (mario_magnet.wav)
dur = 0.32
samples = []
total_frames = int(dur * SAMPLE_RATE)
for i in range(total_frames):
    t = float(i) / SAMPLE_RATE
    carrier = math.sin(2.0 * math.pi * 660.0 * t)
    modulator = math.sin(2.0 * math.pi * 40.0 * t)
    val = carrier * (0.6 + 0.4 * modulator)
    env = math.exp(-t * 6.0)
    samples.append(val * env * 0.6)
write_wav("mario_magnet.wav", samples)

# 6. Invincibility Star Fanfare (mario_invincible.wav)
# Energetic looping jingle
dur = 1.2
samples = []
total_frames = int(dur * SAMPLE_RATE)
star_notes = [659.25, 659.25, 0, 659.25, 0, 523.25, 659.25, 0, 783.99]
tempo_len = total_frames // len(star_notes)
for i in range(total_frames):
    note_i = min(i // tempo_len, len(star_notes) - 1)
    f = star_notes[note_i]
    t = float(i) / SAMPLE_RATE
    if f > 0:
        val = (1.0 if math.sin(2.0 * math.pi * f * t) > 0 else -1.0) * 0.25 + math.sin(2.0 * math.pi * f * t) * 0.3
        env = 1.0 - ((i % tempo_len) / float(tempo_len)) * 0.4
    else:
        val = 0.0
        env = 0.0
    samples.append(val * env * 0.6)
write_wav("mario_invincible.wav", samples)

print("Generated Platformer V2 audio successfully!")

