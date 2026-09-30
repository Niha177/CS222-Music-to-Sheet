# AI-Assisted Project Proposal

### From Audio to Sheet Music

## Project Overview
Sound to Score is a web application that takes an audio recording of a single melody and
turns it into readable sheet music the user can view and download as a PDF. \
**The problem** Musicians, songwriters, and students often want to write down a melody
they recorded or improvised. Transcribing by ear is slow, and many players, especially
beginners, can play by ear but never learned to read or write standard notation. \
**Intended users** While this is a relatively niche idea, it would be really useful for instrumentalists, music students, and composers or songwriters who
want a quick way to turn a simple recorded melody into standard notation. \
Something like this would save hours that musicians have to spend listening to songs
and writing the music and structure down, and more time can be spent on rehearsals!

## Major Functionality
The core of the system is a single pipeline: upload a recording, detect its notes, and
produce sheet music. Everything else supports or extends that.

### Essential
1. The user can upload a WAV file containing one clear melody.
2. The system detects the pitches and timing of the notes using Basic Pitch, then generates sheet music and
displays it on screen. The generated sheet music is the main expected outcome of the
project.
3. The user can export it as a PDF, which we produce with music21.

### Expected
1. The system shows a progress indicator while transcription runs.
2. The user can adjust basic settings such as tempo and key signature. We have not yet decided whether these
settings apply before transcription or are used to adjust the result afterward.
3. The software can have an option to create accounts and save sheet music
previously created - possibility
5. The software can support more instruments

### Possible
1. The system could accept more audio formats, such as MP3, once WAV support is working.
2. It could also transcribe multiple melodies, such as chords or several instruments, but this
depends on finding tools that make it feasible

### Deliberately Excluded
1. Real-time transcription from a microphone
2. Full orchestral scores with many instruments.

## Technical Approach
Our project will be a web app using the following technologies:
1. **Frontend**: React. This has been decided
2. **Transcription Language / Backend**: Python. This has been decided
3. **Pitch detection**: Basic Pitch, Spotify's open-source transcription library. It converts audio files to MIDI. We tested it and
the results were acceptable.
4. **Notation and export**: music21, It converts MIDI to MusicXML. We tested it and the results were acceptable.
5. **Input format**: WAV for the first version. This is decided.

### Unresolved Questions
1. Processing location. Our transcription code is in Python, but browsers do
not run Python natively. If processing stays on the user's machine, we need a way to
run it there, such as a browser-compatible version of Basic Pitch or a Python-in-the-
browser runtime. We could move processing to a server, but we haven't decided the specifics yet
2. PDF rendering dependency. music21 builds the score, but its PDF output relies on
separate notation software (such as MuseScore or LilyPond) being installed. We need
to confirm how that works in our setup, especially if processing happens on a server.

## Major Components / Areas of Work
The project breaks into six areas, running in order from upload to PDF. All three team
members are currently on audio processing; one of us will move to the frontend soon.
1. **Upload and interface (React)**. Accepts a WAV file, shows progress, and displays the
result. Not started yet; one teammate will pick this up soon.
2. **Pitch detection**. Finds which pitches are played and when. Working with Basic Pitch,
though accuracy can improve.
3. **Note segmentation and rhythm**. Turns detected pitches into notes with clear start times
and durations, snapped to rhythms like quarter and eighth notes. Needs investigation; we
have not worked on it directly yet.
4. **Notation building**. Places notes into measures with a key signature, time signature, and
tempo. Partly handled by music21, but the details need testing.
5. **PDF rendering and export**. Produces a readable, downloadable PDF. Working in our tests,
but the rendering setup is unconfirmed.

## Feasibility, Risks and Unknowns
1. Integration could be a challenge. We have done basic testing of Spotify Basic
Pitch and Music21 separately, and tested Music21 by using Basic Pitch’s
output. However, we haven’t thought about how they would work together - i.e.
what should be done so that there is no issue with Music21 waiting for Basic
Pitch to stop processing.
2. PDF rendering dependency. music21 needs external notation software to create PDFs,
which complicates deployment. We need to confirm which renderer we use and where it
runs.
3. Another risk is that the system might work well on some clean recordings but
performs poorly on others. We do not yet know how accurate Basic Pitch will be
for a variety of inputs, such as background noise, overtones, different recording
qualities, or multiple instruments playing at the same time. We could address
this by testing the system with a variety of recordings and, if necessary, requiring
higher-quality audio as an input.
4. Additional audio formats. Supporting MP3 and other formats may require extra
conversion. We will stay WAV-only until the pipeline is stable.


## Current Team Understanding
We have agreed on the project direction, and there have not been any disagreements so far. We are at the following juncture:

### Decided
- Sound to Score is a web application.
- Transcription is written in Python, using Basic Pitch for pitch detection and music21 for notation and PDF export.
- The first version accepts WAV files only.
- Single-melody transcription is the core scope. Real-time microphone input and orchestral scores are out.
- We have decided to focus on converting audio files into MIDI and then converting the MIDI into sheet music. We have also decided to initially use existing libraries rather
than developing our own audio-to-MIDI or MIDI-to-sheet-music systems from scratch.
- We have decided that we will use without React for the frontend

### Tentative
- Processing on the user's machine (current leaning).

### Needs Discussion
- Whether tempo and key settings are applied before transcription or used to adjust the
result afterward.
- The exact format for passing notes between components, so frontend and processing
work can proceed in parallel.
- Any other features that we should add, since our broad goal has been almost the same till now.
