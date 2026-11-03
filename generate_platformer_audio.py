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

# 1. Mario Jump Sound (Classic rising square/pulse chirp)
duration = 0.22
samples = []
for i in range(int(duration * SAMPLE_RATE)):
    t = float(i) / SAMPLE_RATE
    freq = 150.0 + (t / duration) * 450.0
    phase = 2.0 * math.pi * freq * t
    val = 1.0 if math.sin(phase) > 0 else -1.0
    val *= (1.0 - t / duration) * 0.4
    samples.append(val)
write_wav("mario_jump.wav", samples)

# 2. Coin Ding Sound (B5 -> E6 dual tone)
samples = []
# Part 1: B5 (987.77 Hz) for 0.07s
for i in range(int(0.07 * SAMPLE_RATE)):
    t = float(i) / SAMPLE_RATE
    val = math.sin(2.0 * math.pi * 987.77 * t) * 0.45
    val += math.sin(2.0 * math.pi * 1975.5 * t) * 0.15 # 2nd harmonic
    samples.append(val)
# Part 2: E6 (1318.5 Hz) for 0.35s with exponential decay
for i in range(int(0.35 * SAMPLE_RATE)):
    t = float(i) / SAMPLE_RATE
    decay = math.exp(-t * 8.0)
    val = (math.sin(2.0 * math.pi * 1318.5 * t) * 0.5 + math.sin(2.0 * math.pi * 2637.0 * t) * 0.15) * decay
    samples.append(val)
write_wav("mario_coin.wav", samples)

# 3. Enemy Stomp Sound (Punchy bass pop)
duration = 0.16
samples = []
for i in range(int(duration * SAMPLE_RATE)):
    t = float(i) / SAMPLE_RATE
    decay = (1.0 - t / duration) ** 2
    freq = 420.0 * (1.0 - t / duration) + 60.0
    val = (1.0 if math.sin(2.0 * math.pi * freq * t) > 0.2 else -1.0) * 0.55 * decay
    samples.append(val)
write_wav("mario_stomp.wav", samples)

# 4. Block Hit Bonk
duration = 0.12
samples = []
for i in range(int(duration * SAMPLE_RATE)):
    t = float(i) / SAMPLE_RATE
    decay = 1.0 - t / duration
    val = math.sin(2.0 * math.pi * 240.0 * t) * 0.6 * decay
    samples.append(val)
write_wav("mario_block.wav", samples)

# 5. Spring Bounce Sound
duration = 0.3
samples = []
for i in range(int(duration * SAMPLE_RATE)):
    t = float(i) / SAMPLE_RATE
    freq = 200.0 + math.sin(t * 30.0) * 150.0 + t * 400.0
    val = math.sin(2.0 * math.pi * freq * t) * 0.5 * (1.0 - t / duration)
    samples.append(val)
write_wav("mario_spring.wav", samples)

# 6. Hurt Sound
duration = 0.25
samples = []
for i in range(int(duration * SAMPLE_RATE)):
    t = float(i) / SAMPLE_RATE
    freq = 300.0 - t * 600.0
    if freq < 60.0: freq = 60.0
    noise = (t * 7919 % 1.0) * 2.0 - 1.0
    tone = 1.0 if math.sin(2.0 * math.pi * freq * t) > 0 else -1.0
    val = (tone * 0.4 + noise * 0.3) * (1.0 - t / duration)
    samples.append(val)
write_wav("mario_hurt.wav", samples)

# 7. Level Complete Fanfare
notes = [523.25, 659.25, 783.99, 1046.50, 783.99, 1046.50] # C5, E5, G5, C6, G5, C6
durations = [0.12, 0.12, 0.12, 0.2, 0.14, 0.5]
samples = []
for f, dur in zip(notes, durations):
    n_samples = int(dur * SAMPLE_RATE)
    for i in range(n_samples):
        t = float(i) / SAMPLE_RATE
        decay = 1.0 - (t / dur) * 0.3
        val = (math.sin(2.0 * math.pi * f * t) * 0.4 + math.sin(2.0 * math.pi * f * 2.0 * t) * 0.15) * decay
        samples.append(val)
write_wav("mario_clear.wav", samples)

# 8. Upbeat Catchy Mario BGM (4-bar seamless retro chiptune loop, 140 BPM)
bpm = 140.0
beat_len = 60.0 / bpm
bar_len = beat_len * 4.0
total_len = bar_len * 2.0 # 8 beats = ~3.43 seconds seamless loop
bgm_samples = []
total_count = int(total_len * SAMPLE_RATE)

# Melody notes (E5, E5, rest, E5, rest, C5, E5, G5, rest, G4)
melody = [
    (0.00, 659.25, 0.12), (0.25, 659.25, 0.12), (0.75, 659.25, 0.12),
    (1.25, 523.25, 0.14), (1.50, 659.25, 0.16), (2.00, 783.99, 0.28),
    (2.75, 392.00, 0.28),
    # Bar 2
    (3.50, 523.25, 0.18), (4.00, 392.00, 0.18), (4.50, 329.63, 0.18),
    (5.00, 440.00, 0.16), (5.50, 493.88, 0.16), (6.00, 466.16, 0.16),
    (6.50, 440.00, 0.22), (7.00, 783.99, 0.30)
]

# Bass line notes (C3, G3, A2, F2, C3, G3)
bass = [
    (0.00, 130.81), (0.50, 130.81), (1.00, 196.00), (1.50, 196.00),
    (2.00, 174.61), (2.50, 174.61), (3.00, 196.00),
    (3.50, 130.81), (4.00, 196.00), (4.50, 164.81), (5.00, 220.00),
    (5.50, 246.94), (6.00, 233.08), (6.50, 220.00), (7.00, 196.00)
]

for i in range(total_count):
    t = float(i) / SAMPLE_RATE
    beat = t / beat_len
    
    # Melody generator
    m_val = 0.0
    for start_b, freq, dur_b in melody:
        if start_b <= beat < start_b + dur_b:
            note_t = (beat - start_b) * beat_len
            env = max(0.0, 1.0 - note_t / (dur_b * beat_len))
            # Pulse wave with 25% duty cycle
            phase = (freq * note_t) % 1.0
            pulse = 1.0 if phase < 0.25 else -0.33
            m_val += pulse * 0.22 * env
            break
            
    # Bass generator (triangle wave)
    b_val = 0.0
    for idx in range(len(bass)):
        start_b, freq = bass[idx]
        next_b = bass[idx+1][0] if idx + 1 < len(bass) else 8.0
        if start_b <= beat < next_b:
            note_t = (beat - start_b) * beat_len
            env = max(0.0, 1.0 - note_t / ((next_b - start_b) * beat_len * 0.9))
            phase = (freq * note_t) % 1.0
            tri = 4.0 * abs(phase - 0.5) - 1.0
            b_val += tri * 0.24 * env
            break
            
    # Hi-hat drum on every 0.5 beat
    hat = 0.0
    sub_beat = (beat % 0.5) * beat_len
    if sub_beat < 0.04:
        noise = (float(i * 982451 % 1000) / 500.0) - 1.0
        hat = noise * 0.06 * (1.0 - sub_beat / 0.04)
        
    bgm_samples.append(m_val + b_val + hat)

# Smooth crossfade loop seam (0.05s)
fade = int(0.05 * SAMPLE_RATE)
for i in range(fade):
    w = float(i) / fade
    bgm_samples[i] = bgm_samples[i] * w + bgm_samples[-fade + i] * (1.0 - w)

write_wav("mario_bgm.wav", bgm_samples)
print("All Mario audio files generated successfully!")

