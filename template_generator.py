# template_generator.py
# Generates MEN echo waveform templates for various modes

def main():
    import numpy as np
    import os

    print("🔧 Generating echo templates...")

    param_ranges = {
        "frequency": [100, 150, 200],
        "decay": [0.2, 0.5, 0.8],
        "delay": [0.1, 0.3, 0.5]
    }

    size = 4096
    delta_t = 1.0 / size
    t = np.linspace(0, size * delta_t, size)

    os.makedirs("outputs/templates", exist_ok=True)

    count = 0
    for f in param_ranges["frequency"]:
        for d in param_ranges["decay"]:
            for l in param_ranges["delay"]:
                template = np.sin(2 * np.pi * f * (t - l)) * np.exp(-d * (t - l)) * (t > l)
                filename = f"outputs/templates/template_f{f}_d{d}_l{l}.npy"
                np.save(filename, template)
                count += 1

    print(f"✅ Generated {count} echo templates.")