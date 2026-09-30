# AI-Assisted Project Proposal

### From Audio to Sheet Music

## Project Overview
The idea of this project is to output sheet music for pitched instruments by inputting
audio files.
As a drummer, I often like to read drum notation when learning or playing along with a
song, but transcriptions are often not available online or are not accurate. However,
since getting accurate drum transcription is more difficult, we are currently planning to
focus on pitched instruments that audio-to-MIDI models such as Basic Pitch are better
suited for.
I imagine that any musician could benefit from this, since it eliminates the need for
writing down sheet music manually, or trying to remember the whole song from the first
time one starts to play it.
While this is a relatively niche idea, it would be really useful for instrumentalists.
Something like this would save hours that musicians have to spend listening to songs
and writing the music and structure down, and more time can be spent on rehearsals!

## Functionalities
1. The user should be able to upload an audio file in various formats (MP3, WAV,
M4A, etc.) - essential
2. The system should first convert the input file into MIDI using an audio-to-MIDI
model, and then convert the MIDI into sheet music - essential
3. The sheet music should be converted into MusicXML or a PDF, which the user
can view and download - expected
4. The software could have an option to create accounts and save sheet music
previously created - possibility
5. The software could support more instruments, and have an option for selecting
tempo and time signature - possibility

## Technical Approach
1. We found two open source libraries to help with our project:
◦ Spotify Basic Pitch: This library handles converting audio files into MIDI
◦ Music21: This library handles converting MIDI to sheet music
2. These libraries are in Python, so that is what we will be using for the backend.
3. We would also create a frontend to handle audio inputs and a way to output the
sheet music.

## Major Components / Areas of Work
1. We may look at and test other libraries for the audio file to MIDI conversion,
since Spotify Basic Pitch, though usable, is not very accurate.
2. The Music21 library seems fine to us; it seemed accurate when it printed the
notes. However, opening the MusicXML file in MuseScore crashed for me, so we
will have to look into that.
3. We know that we need to create a frontend for handling audio inputs and the
sheet music output. We haven’t decided the specifics yet - that includes the
language/framework we should use, how the UI should look, if we would need
any libraries for taking care of uploads and downloads, etc.

## Feasibility, Risks and Unknowns
1. Integration could be a challenge - we have done basic testing of Spotify Basic
Pitch and Music21 separately, and tested Music21 by using Basic Pitch’s
output. However, we haven’t thought about how they would work together - i.e.
what should be done so that there is no issue with Music21 waiting for Basic
Pitch to stop processing.
2. Another risk is that the system might work well on some clean recordings but
performs poorly on others. We do not yet know how accurate Basic Pitch will be
for a variety of inputs, such as background noise, overtones, different recording
qualities, or multiple instruments playing at the same time. We could address
this by testing the system with a variety of recordings and, if necessary, requiring
higher-quality audio as an input.
3. Another risk is that not all features are completed on time. In such a case, we
could change the scope of project to be one of the two main parts - either
converting the audio file to MIDI, or MIDI to sheet music. Eithercould still be a
complete project and have its own use cases.

## Current Team Understanding
We have decided to focus on converting audio files into MIDI and then converting the
MIDI into sheet music. We have also decided to initially use existing libraries rather
than developing our own audio-to-MIDI or MIDI-to-sheet-music systems from scratch.
We have not yet decided what frontend technology to use, or exactly how the frontend
and backend will communicate. We also still need to investigate how accurate Basic
Pitch is for different types of audio and how we would handle the integration between
Basic Pitch and Music21.