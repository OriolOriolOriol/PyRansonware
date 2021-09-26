# Ransonware in Python3 (Tested for Windows)

## Hint


<ul>
  <li>Line 103: #print('Password generata: {}'.format(password_generata)). Uncomment this print to see the generated password and decrypt. </li>
  <li>I wanted to encrypt only one folder that I called "ciao". You can see the paths to the folder that will be encrypted on line 99-100</li>
  <li>there is a **ransonware.exe**</li>
</ul>

## Dependencies

```
python -m pip install pyinstaller
python -m pip install pyAesCrypt
python -m pip install webbrowser
```

## How to run?

```
cd C:\Users
mkdir ciao
echo some-text  > filename.txt
click on Don't_open_me.pdf
```
## Info

If you want to change something, just edit the file in python and then

```
pyinstaller Ransonware.py --onefile
```
