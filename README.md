# MidiM MIDIMaestro - An Open Source Custom MIDI Controller Interface

MidiM MIDIMaestro is a customizable MIDI controller interface that empowers musicians and DJs to design their own control layouts. Using a simple drag-and-drop interface, users can assign sliders, buttons, and knobs to MIDI commands and save their layouts for later use.

## Features
- **Drag-and-Drop Interface**: Easily position sliders, buttons, and knobs on a canvas.
- **MIDI Mapping**: Assign MIDI commands (e.g., control change messages) to each control.
- **Save/Load Layouts**: Save your custom layouts to a JSON file and reload them anytime.
- **Cross-Platform**: Built with Python, works on Windows, macOS, and Linux.

## Why It’s Cool
MidiM (MidiMaestro) gives you the freedom to create a MIDI controller tailored to your workflow. Whether you're a DJ tweaking effects or a musician controlling synth parameters, this tool puts the power in your hands.

## Technologies
- **Python**: Core programming language.
- **mido**: Python library for MIDI communication.
- **tkinter**: Built-in Python library for the GUI.

## Installation
1. Install Python 3.x (if not already installed).
2. Install required libraries:
   ```bash
   pip install mido
   ```
3. Ensure you have a MIDI device or virtual MIDI port set up (e.g., loopMIDI on Windows or IAC Driver on macOS).
4. Clone or download this repository:
   ```bash
   git clone https://github.com/frangedev/MidiM
   cd MidiM
   ```
5. Run the app:
   ```bash
   python midim.py
   ```

## Usage
1. Launch the app with `python midim.py`.
2. Drag the colored rectangles (Slider, Button, Knob) to your desired positions.
3. Click a control, then press "Map MIDI" to assign a MIDI command (currently hardcoded as an example).
4. Use "File > Save Layout" to save your design and "File > Load Layout" to restore it.
5. Test your MIDI output with a connected device or software (e.g., a DAW like Ableton Live).

## Future Improvements
- Add a web version using JavaScript and Web MIDI API.
- Allow users to customize MIDI message types (e.g., note on/off, program change).
- Improve the UI with more control types and visual feedback.
- Support real-time MIDI input for testing mappings.

## License
This project is licensed under the MIT License. Feel free to modify and distribute it!

---
Happy controlling, Maestro!
