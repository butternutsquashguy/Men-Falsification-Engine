# echo_detector_comb.py
# Frequency-domain comb-style periodic echo detection

def main():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("🔍 Running Comb-method echo detection...")

    # Simulated frequency-domain data
    freq = np.linspace(0, 1024, 2048)
    power_spectrum = np.random.rand(len(freq)) * 1e-21
    power_spectrum[::50] += 1e-20  # Inject periodic bump

    # Comb method: look for regularly spaced peaks
    spacing = 50
    peaks = power_spectrum[::spacing]
    score = peaks.mean()

    df = pd.DataFrame({
        "frequency": freq[::spacing],
        "power": peaks
    })
    df.to_csv("outputs/echo_candidates_comb.csv", index=False)

    plt.plot(freq, power_spectrum)
    plt.title("Comb Echo Candidate Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power")
    plt.savefig("outputs/comb_spectrum_plot.png")

    print(f"📈 Comb detection score: {score:.2e}")
    print("✅ Comb candidates and plot saved.")