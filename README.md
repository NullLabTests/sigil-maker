# Simple Chaos Sigil Maker

A Gradio-based Python tool to generate artistic chaos sigils from statements of intent. Vowels are removed, letters are uniquely selected and placed on a circle, connected with colorful lines and optional curves for a mystical, polished glyph.

## About the Project
This app creates sigils inspired by chaos magic principles: Enter your intent, and it transforms the consonants into a visual symbol. Perfect for manifestation, art, or fun experimentation. Includes a web UI for easy generation and a CLI mode for quick saves.

## Features
- Interactive Gradio UI with input, clear/submit buttons, and sigil output.
- Random artistic elements: Offsets, colors, thicknesses, and flourish curves.
- Outer circle seal for a complete look.
- CLI fallback: Save sigils directly to PNG.
- Dark theme with modern styling.

## Screenshot
![App Screenshot](Screenshot%20From%202026-01-18%2002-41-27.png)

## Ishtar Star Symbol (Inspiration)
![Ishtar Star](Ishtar-star-symbol.svg.png)

## How it Works
- Input a statement (e.g., "May all beings be at peace").
- Vowels stripped, duplicates removed, letters sorted.
- Letters placed on a circle with random offsets.
- Connected with lines (random color/thickness) and optional arcs.
- Saved as `sigil.png` or displayed in UI.

## Example Sigil
![Example Sigil](sigil.png)

## Usage
For web UI:
```bash
python sigil_maker.py
```
Visit http://localhost:7860 in your browser.

For CLI:
```bash
python sigil_maker.py "Your intent here"
```
Generates and saves to `sigil.png`.

## Installation
Requires Python 3, Gradio, and Pillow:
```bash
pip install gradio pillow
```

## Contributing
Fork the repo, make changes, and submit a pull request. Ideas for enhancements welcome!
