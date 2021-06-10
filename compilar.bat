@REM Ainda em desenvolvimento, pode mudar dependendo de como vá ficar a estrutura final das pastas
pyinstaller main.py -n Lolicalc --icon="packages/img/Lolicalc.ico" -w
mkdir "dist/Lolicalc/packages"
robocopy "./packages" "dist/Lolicalc/packages" /MIR
pause