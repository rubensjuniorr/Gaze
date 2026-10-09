# Gaze

A Python desktop teleprompter prototype built with Flet.

## Features

- Splits speech into short word blocks.
- Click to advance; long press to go backward.
- Small, always-on-top window with centered text.

The speech is currently defined in screen.py.

## Setup on macOS

Developed with Python 3.14.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

```bash
python screen.py
```
Type or paste your speech and click Start reading.
Click the reading area to advance; long press to go backward.
Use Editar texto to return to the editor. Your text is preserved.
Starting again resets the reading position to the first block.

## Test

```bash
python -m unittest -v
```