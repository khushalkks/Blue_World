import os
import math
import wave
import struct
import random

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

# 1. Ambient Drone Loop (3.5 seconds seamless loop)
# Deep sci-fi resonant reactor rumble with pulsing harmonic overtones
duration = 3.5
samples_count = int(duration * SAMPLE_RATE)
ambient = []
for i in range(samples_count):
    t = float(i) / SAMPLE_RATE
    # Base 55Hz sub-bass drone (A1)
    s1 = math.sin(2.0 * math.pi * 55.0 * t) * 0.4
    # Harmonic 110Hz (A2) with slow phase pulsation
    s2 = math.sin(2.0 * math.pi * 110.0 * t + 0.5 * math.sin(2.0 * math.pi * 0.5 * t)) * 0.25
    # Resonance 165Hz (E3)
    s3 = math.sin(2.0 * math.pi * 165.0 * t) * 0.12
    # Subtle electrical hum 220Hz
    s4 = math.sin(2.0 * math.pi * 220.0 * t) * 0.06 * (0.8 + 0.2 * math.sin(2.0 * math.pi * 2.0 * t))
    # Soft filtered white noise for air ventilation / room tone
    noise = (random.random() * 2.0 - 1.0) * 0.02
    val = (s1 + s2 + s3 + s4 + noise) * 0.7
    ambient.append(val)
# Apply smooth cross-fade window to loop seam
fade_len = int(0.1 * SAMPLE_RATE)
for i in range(fade_len):
    w = float(i) / fade_len
    # Blend start and end
    ambient[i] = ambient[i] * w + ambient[-fade_len + i] * (1.0 - w)
write_wav("ambient_lab.wav", ambient)

# 2. UI Hover Beep (0.05s) - Soft high-tech pip
samples = []
for i in range(int(0.04 * SAMPLE_RATE)):
    t = float(i) / SAMPLE_RATE
    env = 1.0 - (float(i) / (0.04 * SAMPLE_RATE))
    s = math.sin(2.0 * math.pi * 880.0 * t) * env * 0.25
    samples.append(s)
write_wav("ui_hover.wav", samples)

# 3. UI Click Sound (0.08s) - Crisp digital select
samples = []
total = int(0.08 * SAMPLE_RATE)
for i in range(total):
    t = float(i) / SAMPLE_RATE
    env = math.exp(-i / (0.015 * SAMPLE_RATE))
    s = (math.sin(2.0 * math.pi * 1200.0 * t) * 0.6 + math.sin(2.0 * math.pi * 2400.0 * t) * 0.4) * env * 0.4
    samples.append(s)
write_wav("ui_click.wav", samples)

# 4. Keypad Button Beep (0.09s) - High-tech telephone / DTMF feel
samples = []
total = int(0.09 * SAMPLE_RATE)
for i in range(total):
    t = float(i) / SAMPLE_RATE
    env = 1.0 if i < int(total * 0.7) else (1.0 - (i - total * 0.7) / (total * 0.3))
    s = (math.sin(2.0 * math.pi * 941.0 * t) * 0.5 + math.sin(2.0 * math.pi * 1336.0 * t) * 0.5) * env * 0.35
    samples.append(s)
write_wav("key_beep.wav", samples)

# 5. Access Granted (0.8s) - Major chord fanfare (C5 -> E5 -> G5 -> C6)
samples = []
notes = [523.25, 659.25, 783.99, 1046.50]
note_dur = 0.18
for idx, freq in enumerate(notes):
    n_samples = int(note_dur * SAMPLE_RATE)
    for i in range(n_samples):
        t = float(i) / SAMPLE_RATE
        env = math.exp(-i / (n_samples * 0.7))
        s = (math.sin(2.0 * math.pi * freq * t) * 0.6 + math.sin(2.0 * math.pi * (freq * 2.0) * t) * 0.2) * env * 0.45
        samples.append(s)
write_wav("access_granted.wav", samples)

# 6. Access Denied (0.45s) - Harsh low dual-buzz
samples = []
total = int(0.45 * SAMPLE_RATE)
for i in range(total):
    t = float(i) / SAMPLE_RATE
    # Stutter envelope (two pulses)
    pulse = 1.0 if (i < total * 0.45 or i > total * 0.55) else 0.0
    env = math.exp(-((i % int(total * 0.5)) / (total * 0.35))) * pulse
    # Low dissonant square wave
    s = (1.0 if math.sin(2.0 * math.pi * 140.0 * t) > 0 else -1.0) * 0.3
    s += (1.0 if math.sin(2.0 * math.pi * 148.0 * t) > 0 else -1.0) * 0.2
    samples.append(s * env * 0.4)
write_wav("access_denied.wav", samples)

# 7. Switch / Breaker Flip (0.12s) - Heavy mechanical snap
samples = []
total = int(0.12 * SAMPLE_RATE)
for i in range(total):
    t = float(i) / SAMPLE_RATE
    env = math.exp(-i / (0.012 * SAMPLE_RATE))
    click = (random.random() * 2.0 - 1.0) * env * 0.7
    thud = math.sin(2.0 * math.pi * 180.0 * t) * math.exp(-i / (0.04 * SAMPLE_RATE)) * 0.5
    samples.append((click + thud) * 0.6)
write_wav("switch_flip.wav", samples)

# 8. Power Surge / Online (1.2s) - Rising frequency pitch + bass hum
samples = []
total = int(1.2 * SAMPLE_RATE)
for i in range(total):
    t = float(i) / SAMPLE_RATE
    norm = float(i) / total
    freq = 60.0 + 350.0 * (norm ** 2)
    s = math.sin(2.0 * math.pi * freq * t) * 0.4
    hum = math.sin(2.0 * math.pi * 60.0 * t) * 0.35
    # Crackle
    crackle = ((random.random() * 2.0 - 1.0) * 0.15) if (random.random() < 0.08) else 0.0
    env = min(1.0, norm * 4.0) * (1.0 - norm * 0.3)
    samples.append((s + hum + crackle) * env * 0.5)
write_wav("power_surge.wav", samples)

# 9. Radio Tuning Static (0.5s) - Heterodyne sweep
samples = []
total = int(0.5 * SAMPLE_RATE)
for i in range(total):
    t = float(i) / SAMPLE_RATE
    norm = float(i) / total
    whine_freq = 1500.0 + 800.0 * math.sin(norm * math.pi * 4.0)
    whine = math.sin(2.0 * math.pi * whine_freq * t) * 0.25
    static = (random.random() * 2.0 - 1.0) * 0.3
    samples.append((whine + static) * 0.3)
write_wav("radio_tune.wav", samples)

# 10. Signal Lock Chime (0.7s) - Resonant pure sine chime
samples = []
total = int(0.7 * SAMPLE_RATE)
for i in range(total):
    t = float(i) / SAMPLE_RATE
    env = math.exp(-i / (total * 0.35))
    s1 = math.sin(2.0 * math.pi * 1760.0 * t) * 0.5
    s2 = math.sin(2.0 * math.pi * 2640.0 * t) * 0.3
    samples.append((s1 + s2) * env * 0.45)
write_wav("signal_lock.wav", samples)

# 11. Door Slide (1.5s) - Heavy pneumatic hiss and motor groaning
samples = []
total = int(1.5 * SAMPLE_RATE)
for i in range(total):
    t = float(i) / SAMPLE_RATE
    norm = float(i) / total
    # Motor rumble 80Hz - 60Hz
    motor = math.sin(2.0 * math.pi * (80.0 - 20.0 * norm) * t) * 0.35
    # Air release hiss
    hiss = (random.random() * 2.0 - 1.0) * 0.25 * math.exp(-((norm - 0.2)**2) / 0.05)
    # End metallic latch clunk at 1.3s
    clunk = 0.0
    if norm > 0.85:
        clunk_t = t - 1.27
        clunk = math.sin(2.0 * math.pi * 120.0 * clunk_t) * math.exp(-(norm - 0.85) / 0.03) * 0.6
    env = min(1.0, norm * 5.0) * (1.0 if norm < 0.9 else (1.0 - (norm - 0.9)/0.1))
    samples.append((motor + hiss + clunk) * env * 0.55)
write_wav("door_slide.wav", samples)

# 12. Footstep 1 & 2 (0.1s each) - Subtle soft rubber boots on metal
for step_idx in [1, 2]:
    samples = []
    total = int(0.09 * SAMPLE_RATE)
    base_f = 90.0 if step_idx == 1 else 105.0
    for i in range(total):
        t = float(i) / SAMPLE_RATE
        env = math.exp(-i / (0.015 * SAMPLE_RATE))
        thud = math.sin(2.0 * math.pi * base_f * t) * 0.4
        scuff = (random.random() * 2.0 - 1.0) * 0.15
        samples.append((thud + scuff) * env * 0.3)
    write_wav(f"footstep{step_idx}.wav", samples)

print("All audio files generated successfully!")
