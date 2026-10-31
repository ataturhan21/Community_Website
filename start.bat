@echo off
chcp 65001 >nul
pushd "%~dp0" || exit /b 1
poetry run streamlit run "community_website\👋Hoşgeldiniz.py"
set "launch_result=%errorlevel%"
popd
exit /b %launch_result%
