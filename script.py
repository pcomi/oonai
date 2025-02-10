import os
import mido

def kalimba_to_standard_notation(tab):
    """Converts kalimba tab notation to MIDI note numbers."""
    kalimba_mapping = {
        "1": 60, "2": 62, "3": 64, "4": 65, "5": 67, "6": 69, "7": 71,
        "1'": 72, "2'": 74, "3'": 76, "4'": 77, "5'": 79, "6'": 81, "7'": 83,
        "1''": 84, "2''": 86, "3''": 88
    }
    return [kalimba_mapping.get(note, note) for note in tab.split()]

def kalimba_to_piano(kalimba_tabs):
    """Converts kalimba tabs to piano note names."""
    mapping = {
        "1": "C4", "2": "D4", "3": "E4", "4": "F4", "5": "G4", "6": "A4", "7": "B4",
        "1'": "C5", "2'": "D5", "3'": "E5", "4'": "F5", "5'": "G5", "6'": "A5", "7'": "B5",
        "1''": "C6", "2''": "D6", "3''": "E6"
    }
    return " ".join([mapping.get(note, note) for note in kalimba_tabs.split()])

def read_midi_file(file_path):
    """Reads a MIDI file and extracts note information."""
    try:
        midi = mido.MidiFile(file_path)
        notes = []
        for track in midi.tracks:
            for msg in track:
                if msg.type == 'note_on' and msg.velocity > 0:
                    notes.append(msg.note)
        return notes
    except Exception as e:
        print(f"Error reading MIDI file {file_path}: {e}")
        return []

def main():
    """Processes kalimba and piano tabs, converting between formats."""
    kalimba_dir = 'kalimba tabs'
    if os.path.exists(kalimba_dir):
        for file in os.listdir(kalimba_dir):
            file_path = os.path.join(kalimba_dir, file)
            try:
                with open(file_path, 'r') as f:
                    tab = f.read().strip()
                    print(f"Kalimba {file}: {kalimba_to_piano(tab)}")
            except Exception as e:
                print(f"Error reading {file}: {e}")

    midi_dir = 'piano tabs'
    midi_notes = {}
    if os.path.exists(midi_dir):
        for file in os.listdir(midi_dir):
            if file.endswith('.mid') or file.endswith('.midi'):
                file_path = os.path.join(midi_dir, file)
                midi_notes[file] = read_midi_file(file_path)
    
    for filename, notes in midi_notes.items():
        print(f"MIDI {filename}: {notes}")

if __name__ == "__main__":
    main()
