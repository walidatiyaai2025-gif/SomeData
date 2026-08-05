@echo off
setlocal EnableExtensions
title Get or Update SomeData Repository

set "REPO_URL=https://github.com/walidatiyaai2025-gif/SomeData.git"
set "REPO_FOLDER=SomeData"

echo =====================================================
echo   SomeData Repository - Clone or Update
echo =====================================================
echo.

where git >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or is not available in PATH.
    echo Install Git for Windows, then run this file again.
    echo https://git-scm.com/download/win
    echo.
    pause
    exit /b 1
)

if exist "%REPO_FOLDER%\.git" (
    echo Repository already exists. Updating it now...
    pushd "%REPO_FOLDER%"

    git fetch origin
    if errorlevel 1 goto :git_error_inside

    git checkout main
    if errorlevel 1 goto :git_error_inside

    git pull --ff-only origin main
    if errorlevel 1 goto :git_error_inside

    echo.
    echo Repository updated successfully:
    echo %CD%
    popd
    goto :success
)

if exist "%REPO_FOLDER%" (
    echo ERROR: A folder named "%REPO_FOLDER%" already exists,
    echo but it is not a valid Git repository.
    echo Rename or delete that folder, then run this file again.
    echo.
    pause
    exit /b 1
)

echo Cloning repository...
git clone "%REPO_URL%" "%REPO_FOLDER%"
if errorlevel 1 goto :git_error

echo.
echo Repository downloaded successfully:
echo %CD%\%REPO_FOLDER%
goto :success

:git_error_inside
popd

:git_error
echo.
echo ERROR: Git operation failed.
echo Check your internet connection and GitHub access, then try again.
echo.
pause
exit /b 1

:success
echo.
echo Done.
echo You can open the repository folder now.
echo.
pause
exit /b 0
