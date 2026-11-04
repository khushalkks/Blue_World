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

# 1. Fireball / Plasma Shoot
dur = 0.16
samples = []
for i in range(int(dur * SAMPLE_RATE)):
    t = float(i) / SAMPLE_RATE
    freq = 950.0 * math.exp(-t * 18.0) + 180.0
    val = (math.sin(2.0 * math.pi * freq * t) * 0.5 + math.sin(2.0 * math.pi * freq * 2.0 * t) * 0.2) * (1.0 - t / dur)
    samples.append(val)
write_wav("mario_fireball.wav", samples)

# 2. Thwomp Slam Impact
dur = 0.35
samples = []
for i in range(int(dur * SAMPLE_RATE)):
    t = float(i) / SAMPLE_RATE
    bass = math.sin(2.0 * math.pi * (110.0 - t * 160.0) * t) * 0.65
    noise = ((i * 9871 % 1000) / 500.0 - 1.0) * 0.35
    env = math.exp(-t * 9.0)
    samples.append((bass + noise) * env)
write_wav("mario_thwomp.wav", samples)

# 3. Platform Crumble / Crack
dur = 0.28
samples = []
for i in range(int(dur * SAMPLE_RATE)):
    t = float(i) / SAMPLE_RATE
    crack = math.sin(2.0 * math.pi * (350.0 + (i % 80) * 15.0) * t) * 0.4
    noise = ((i * 7411 % 1000) / 500.0 - 1.0) * 0.4
    env = (1.0 - t / dur) ** 1.5
    samples.append((crack + noise) * env)
write_wav("mario_crumble.wav", samples)

# 4. Power-Up Fanfare
notes = [392.00, 523.25, 659.25, 783.99, 1046.50] # G4, C5, E5, G5, C6
durations = [0.08, 0.08, 0.08, 0.08, 0.25]
samples = []
for f, d_note in zip(notes, durations):
    count = int(d_note * SAMPLE_RATE)
    for i in range(count):
        t = float(i) / SAMPLE_RATE
        val = math.sin(2.0 * math.pi * f * t) * 0.4 + math.sin(2.0 * math.pi * f * 2.0 * t) * 0.15
        samples.append(val * (1.0 - (t / d_note) * 0.3))
write_wav("mario_powerup.wav", samples)

# 5. Suspense BGM (Dark, mysterious, pulsing subterranean theme, 128 BPM)
bpm = 128.0
beat_len = 60.0 / bpm
total_len = beat_len * 16.0 # 4 bars = ~7.5 seconds
total_count = int(total_len * SAMPLE_RATE)
suspense_samples = []

# Dark minor arpeggios (D minor / F / Bb / A)
chords = [
    (0.0, 146.83), (2.0, 174.61), (4.0, 116.54), (6.0, 110.00)
]

for i in range(total_count):
    t = float(i) / SAMPLE_RATE
    beat = t / beat_len
    
    # Pulsing Bass Drone
    chord_idx = int(beat / 4.0) % 2
    root = 73.42 if chord_idx == 0 else 65.41 # D2 vs C2
    bass_pulse = math.sin(2.0 * math.pi * root * t) * 0.3 * (0.8 + 0.2 * math.sin(2.0 * math.pi * 4.0 * t))
    
    # Eerie synth stabs on 16th notes
    sub_beat = beat % 0.5
    synth_env = max(0.0, 1.0 - sub_beat / 0.35)
    arp_note = 293.66 + math.sin(beat * math.pi) * 80.0
    synth = (1.0 if math.sin(2.0 * math.pi * arp_note * t) > 0.3 else -0.3) * 0.15 * synth_env
    
    # Heartbeat kick on beats 0, 0.75, 2, 2.75
    sub4 = beat % 2.0
    kick = 0.0
    if sub4 < 0.18:
        kick = math.sin(2.0 * math.pi * (80.0 - sub4 * 300.0) * sub4) * 0.35 * (1.0 - sub4 / 0.18)
    elif 0.75 <= sub4 < 0.93:
        k_t = sub4 - 0.75
        kick = math.sin(2.0 * math.pi * (70.0 - k_t * 260.0) * k_t) * 0.28 * (1.0 - k_t / 0.18)
        
    suspense_samples.append(bass_pulse + synth + kick)

# Loop crossfade
fade = int(0.06 * SAMPLE_RATE)
for i in range(fade):
    w = float(i) / fade
    suspense_samples[i] = suspense_samples[i] * w + suspense_samples[-fade + i] * (1.0 - w)

write_wav("mario_suspense.wav", suspense_samples)
print("All suspense audio files generated successfully!")
