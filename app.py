from flask import Flask, jsonify, request, session, make_response
from flask_cors import CORS     # for connecting to react
from basic_pitch.inference import predict_and_save
from basic_pitch import ICASSP_2022_MODEL_PATH
from music21 import converter, note, chord

app = Flask(__name__)

@app.route("/")
def main():
    # get audio file

    # convert audio to MIDI
    predict_and_save(
        ["Sample_audio.mp3"],   # to be replaced with the audio file imported
        "./",
        True,
        True,
        False,
        True,
        ICASSP_2022_MODEL_PATH
    )

    # Convert MIDI to MusicXML

    # Parse and load the MIDI file into a Stream object
    score = converter.parse("./Sample_audio_basic_pitch.mid")

    # Extract all sequential musical elements (Notes and Chords)
    for element in score.recurse().notes:
        if isinstance(element, note.Note):
            print(f"Note: {element.pitch} | Duration: {element.quarterLength} | Offset: {element.offset}")
            
        elif isinstance(element, chord.Chord):
            pitches = [str(p) for p in element.pitches]
            print(f"Chord: {pitches} | Duration: {element.quarterLength} | Offset: {element.offset}")

    # Estimate the key of the MIDI file
    estimated_key = score.analyze('key')
    print(f"Estimated Key: {estimated_key.tonic.name} {estimated_key.mode}") # e.g., "C major"

    # Find tempo/BPM markings
    for tempo_marking in score.recurse().getElementsByClass('MetronomeMark'):
        print(f"BPM: {tempo_marking.number}")

    # Open and display the file as standard sheet music
    score.show()

    # Export your stream data back into a new MIDI file
    score.write('midi', fp='output_song.mid')