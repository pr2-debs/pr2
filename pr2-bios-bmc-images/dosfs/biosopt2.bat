beep
beep
sleep 1
beep
beep
beep
beep
choice /T:y,5 Writing BIOS settings to C2 settings in 5 seconds.
if errorlevel 2 goto end
beep
beep
beep
biosopt\smcmos -w biosopt\c2-bios.bin
:end
