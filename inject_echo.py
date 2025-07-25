# inject_echo.py
# Injects MEN echo signal into clean strain for benchmarking

def main():
    import numpy as np
    import matplotlib.pyplot as plt
    import os

    print("🧪 Injecting synthetic echo signal...")

    size = 4096
    delta_t = 1.0 / size
    t = np.linspace(0, size * delta_t, size)
    noise = np.random.normal(0, 1e-21, size)

    # Load template
    template_path = "outputs/templates/template_f150_d0.5_l0.3.npy"
    if not os.path.exists(template_path):
        print(f"⚠️ Missing template: {template_path}")
        return

    template = np.load(template_path)
    injected = noise + 5e-21 * template

    os.makedirs("outputs", exist_ok=True)
    np.save("outputs/injected_strain.npy", injected)

    plt.plot(t, injected, label="Injected Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Strain")
    plt.title("Synthetic MEN Echo Injection")
    plt.legend()
    plt.savefig("outputs/injected_echo_plot.png")

    print("✅ Synthetic echo injected and saved.")