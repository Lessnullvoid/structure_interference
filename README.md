# MIDI & Audio Feature Extraction Tool

## Overview

This Python-based tool extracts and visualizes musical features from MIDI and WAV files. It provides insights into melody, rhythm, chords, and spectral analysis using advanced signal processing and MIDI analysis techniques.

## 🚀 Current Features Implemented

### 🎼 MIDI Analysis & Processing

- **Melody Extraction**: Detects pitch contour, note onset times, and durations.
- **Chord Detection**: Extracts chords and labels them with their names and positions.

### 🥁 Rhythm Analysis

- **MIDI Rhythm Extraction**: Identifies beat positions and normalizes them into a 4-beat measure.
- **Audio Rhythm Extraction**: Uses `librosa.beat.beat_track()` to detect tempo and beat positions.

### 📊 Visualization & UI

- **Piano Roll with Chord Labels**:
  - Notes are displayed with blue bars.
  - Chords are labeled above their onset points.
- **Time Grid for Beat Visualization**:
  - Displays detected beats as red markers on a structured time grid.
- **Spectrogram & MFCCs for Audio**:
  - Visualizes spectrogram (STFT) and MFCCs for audio feature analysis.
- **Zoom Feature**: Adjust visualization scale dynamically using a slider.
- **View Selector Dropdown**:
  - Toggle between Piano Roll, Time Grid, and Spectrogram.

### 🎵 Playback Features

- **MIDI Playback**:
  - Extracted melodies can be played using `pygame.midi`.
  - Implements note on/off but needs precise timing refinement.

## 🛠️ TODO List

### 🔹 Essential Improvements

- [ ] Improve timing precision for MIDI playback.
- [ ] Enhance chord detection accuracy.

### 🔹 Additional Enhancements

- [ ] Add support for additional audio file formats.
- [ ] Implement more advanced visualization options.

## 🚀 How to Use

### Requirements

- **Python 3.x**

### Required Libraries:
