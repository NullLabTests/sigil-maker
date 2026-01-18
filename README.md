# Simple Chaos Sigil Maker

A Python-based tool to generate chaos sigils from statements of intent using Gradio for a web interface or CLI.

## How it Works
- Input a statement (e.g., "May all beings be at peace").
- Vowels are stripped, duplicates removed.
- Letters placed on a circle with random offsets.
- Connected with lines and optional curves.
- Saved as `sigil.png` or displayed in web UI.

## Example
![Example Sigil](sigil.png)

## Usage
For CLI:
```bash
python sigil_maker.py "Your statement here"
```
For web UI:
```bash
python sigil_maker.py
```
Visit http://localhost:7860

## Installation
Requires Python 3, gradio, and pillow:
```bash
pip install gradio pillow
```
