import subprocess

scripts = [
    "src.compare_uncertainty_vs_spread",
    "src.animate_wavepacket_spread",
    "src.animate_wavepacket_wavenumber",
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", "-m", script], check=True)