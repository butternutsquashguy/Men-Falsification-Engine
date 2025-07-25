# MEN_Falsification_Engine.py (patched controller)
import importlib
import traceback
import datetime

modules = [
    "template_generator",
    "inject_echo",
    "echo_detector_pycbc",
    "echo_detector_bilby",
    "echo_detector_comb",
    "load_cmb",
    "ring_detector",
    "ring_classifier_ml",
    "crossmatch",
    "null_model",
    "chirplet_transform_overlay",
    "summary_stats_generator",
    "pca_clustering_visualizer",
    "correlation_heatmap_generator",
    "composite_summary_generator",
    "simulate_cmb_men"
]

def log(msg):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {msg}")

def run_module(name):
    try:
        log(f"▶️ Running: {name}")
        mod = importlib.import_module(name)
        if hasattr(mod, 'main'):
            mod.main()
            log(f"✅ Finished: {name}")
        else:
            log(f"⚠️ Skipped (no main()): {name}")
    except Exception as e:
        log(f"❌ Error in module '{name}': {e}")
        traceback.print_exc()

def main():
    log("🚀 Starting MEN Falsification Engine (SEQUENTIAL MODE)")
    for name in modules:
        run_module(name)
    log("🏁 Pipeline complete.")

if __name__ == "__main__":
    main()