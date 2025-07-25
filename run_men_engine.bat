@echo off
REM Full MEN Falsification Engine Launcher for Windows
echo Building Docker container...
docker build -t men_superpipe_full .
echo Running container...
docker run -v %cd%:/app -it men_superpipe_full
pause