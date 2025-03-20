import pretty_midi

def extract_midi_notes(midi_path):
    midi_data = pretty_midi.PrettyMIDI(midi_path)
    note_events = []

    for instrument in midi_data.instruments:
        for note in instrument.notes:
            note_events.append((note.pitch, note.start))  # (MIDI note number, start time)

    note_events.sort(key=lambda x: x[1])  # Sort by start time
    return note_events

# Replace with your MIDI file path
midi_file = "untitled.mid"
notes = extract_midi_notes(midi_file)

# Print extracted notes
for note, time in notes[:10]:  # Show first 10 notes
    print(f"Note: {note}, Start Time: {time}")

def midi_to_guitar_tab(midi_notes):
    standard_tuning = [40, 45, 50, 55, 59, 64]  # EADGBE MIDI numbers
    tabs = []

    for note, time in midi_notes:
        closest_string = min(standard_tuning, key=lambda x: abs(x - note))
        fret = note - closest_string
        string_number = standard_tuning.index(closest_string) + 1  # Strings are numbered 1-6
        tabs.append((string_number, fret, time))

    return tabs

guitar_tabs = midi_to_guitar_tab(notes)

# Print first few guitar tab notes
for string, fret, time in guitar_tabs[:10]:
    print(f"String: {string}, Fret: {fret}, Time: {time}")

def format_tabs(guitar_tabs):
    lines = ["E|", "B|", "G|", "D|", "A|", "E|"]

    for string, fret, time in guitar_tabs:
        lines[6 - string] += f"-{fret}-"

    return "\n".join(lines)

print(format_tabs(guitar_tabs))
