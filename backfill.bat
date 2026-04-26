@echo off
echo =======================================================
echo [*] Starting Historical Data Backfill Process
echo =======================================================

echo.
echo [*] Backfilling Scoop ^& Shovel Ecosystem...
uv run python scripts/generate_seed.py --ecosystem scoop_shovel

echo.
echo [*] Backfilling Chocolatey Ecosystem...
uv run python scripts/generate_seed.py --ecosystem chocolatey

echo.
echo [*] Backfilling WinGet Ecosystem...
echo Note: This may take a while due to the massive size of the official repository.
uv run python scripts/generate_seed.py --ecosystem winget

echo.
echo =======================================================
echo [*] Backfill Complete!
echo [*] The next crawler run will automatically merge this 
echo [*] historical data into your growth charts.
echo =======================================================
pause
