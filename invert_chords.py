scales = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
capo_fret = int(input("Which fret do you want to keep the capo in? "))
no_of_chords = int(input("How many chords do you wanna invert? "))

init_chords = []
final_chords = []

for i in range(no_of_chords):
    init_chords.append(str(input("Enter the chord: ")))
    
for j in init_chords:
    final_chords.append(scales[scales.index(j) - capo_fret])

print(final_chords)
