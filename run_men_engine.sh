#!/bin/bash
# Full MEN Falsification Engine Launcher for Linux/macOS
echo "Building Docker container..."
docker build -t men_superpipe_full .
echo "Running container..."
docker run -v $(pwd):/app -it men_superpipe_full