@echo off
echo ============================================================
echo Testing Intranet Daily Digest Task
echo ============================================================
echo.
echo Running the scheduled task manually...
echo.

schtasks /Run /TN "IntranetDailyDigest"

if %errorlevel% equ 0 (
    echo.
    echo Task triggered successfully!
    echo.
    echo Check your email at krkavi@microsoft.com
    echo.
    echo To view task history:
    echo   1. Open Task Scheduler
    echo   2. Find "IntranetDailyDigest"
    echo   3. Click on "History" tab
    echo.
) else (
    echo.
    echo ERROR! Task not found or failed to run
    echo.
    echo Make sure the task is created first by running:
    echo   setup_task_scheduler.bat
    echo.
)

pause
