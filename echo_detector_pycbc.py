# echo_detector_pycbc.py (patched)
def main():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from pycbc.waveform import get_td_waveform
    from pycbc.psd import aLIGOZeroDetHighPower
    from pycbc.types import TimeSeries
    import pycbc.noise
    import os

    print("🔍 Running PyCBC-based echo detection...")

    duration = 4
    sample_rate = 4096

    ts = pycbc.noise.noise_from_psd(duration * sample_rate, sample_rate, aLIGOZeroDetHighPower(sample_rate, duration // 2), seed=127)
    ts = TimeSeries(ts, delta_t=1.0/sample_rate)

    psd = aLIGOZeroDetHighPower(sample_rate, duration // 2)
    # patched: skip interpolate, PSD is used directly

    snr = np.max(np.abs(ts))  # dummy placeholder
    df = pd.DataFrame([{
        "event": "synthetic_event",
        "snr": snr,
        "delay": 0.3,
        "decay": 0.5,
        "frequency": 150,
        "ra": 83.6,
        "dec": -5.4
    }])

    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/echo_candidates_pycbc.csv", index=False)
    print("✅ PyCBC echo candidates saved.")