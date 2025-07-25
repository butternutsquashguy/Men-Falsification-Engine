# echo_detector_bilby.py (patched)
def main():
    import bilby
    import numpy as np
    import os

    print("🔍 Running Bilby Bayesian echo detector...")

    x = np.linspace(0, 1, 1000)
    y = np.sin(2 * np.pi * 200 * x) + np.random.normal(0, 0.1, len(x))

    priors = dict()
    priors["frequency"] = bilby.core.prior.Uniform(100, 300, name="frequency")
    priors["decay"] = bilby.core.prior.Uniform(0.1, 1.5, name="decay")
    priors["delay"] = bilby.core.prior.Uniform(0.0, 1.0, name="delay")
    priors["sigma"] = bilby.core.prior.Uniform(0.01, 0.5, name="sigma")  # patched

    likelihood = bilby.likelihood.GaussianLikelihood(x, y, sigma=0.1)

    result = bilby.run_sampler(
        likelihood=likelihood,
        priors=priors,
        sampler="dynesty",
        nlive=100,
        outdir="outputs",
        label="echo_candidates_bilby",
        resume=False,
        verbose=False
    )

    result.plot_corner()
    print("✅ Bilby echo detection complete.")