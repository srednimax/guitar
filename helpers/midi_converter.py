class MidiConverter:
    def __init__(self):
        # Standard tuning: string 1: E4 (MIDI 64), 2: B3 (59), 3: G3 (55), 4: D3 (50), 5: A2 (45), 6: E2 (40)
        self.string_tuning = {1: 64, 2: 59, 3: 55, 4: 50, 5: 45, 6: 40}
        self.max_fret = 22

    def convert(self, note):
        """
        Convert a MIDI note number (or numpy scalar) to a tuple (string, fret).
        Chooses the position with the lowest fret.
        Returns None if note is out of range.
        """
        # Ensure note is a Python int
        note_int = int(note)

        # Calculate possible positions
        positions = []
        for string, open_note in self.string_tuning.items():
            fret = note_int - open_note
            if 0 <= fret <= self.max_fret:
                positions.append((string, fret))

        if not positions:
            return None

        # Select the position with the smallest fret number
        string, fret = min(positions, key=lambda x: x[1])
        return string, fret
