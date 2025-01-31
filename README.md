# MIDI & Audio Feature Extraction Tool

## Overview
This Python-based tool extracts and visualizes musical features from **MIDI and WAV files**. It provides insights into **melody, rhythm, chords, and spectral analysis** using advanced signal processing and MIDI analysis techniques.

## 🚀 Current Features Implemented

### 🎼 MIDI Analysis & Processing
- **Melody Extraction**: Detects pitch contour, note onset times, and durations.
- **Chord Detection**: Extracts chords and labels them with their names and positions.

### 🥁 Rhythm Analysis
- **MIDI Rhythm Extraction**: Identifies beat positions and normalizes them into a **4-beat measure**.
- **Audio Rhythm Extraction**: Uses `librosa.beat.beat_track()` to detect **tempo and beat positions**.

### 📊 Visualization & UI
- **Piano Roll with Chord Labels**:
  - Notes are displayed with **blue bars**.
  - Chords are labeled **above their onset points**.
- **Time Grid for Beat Visualization**:
  - Displays **detected beats as red markers** on a structured time grid.
- **Spectrogram & MFCCs for Audio**:
  - Visualizes **spectrogram (STFT) and MFCCs** for audio feature analysis.
- **Zoom Feature**: Adjust visualization scale dynamically using a **slider**.
- **View Selector Dropdown**:
  - Toggle between **Piano Roll, Time Grid, and Spectrogram**.

### 🎵 Playback Features
- **MIDI Playback**:
  - Extracted melodies can be played using `pygame.midi`.
  - Implements note on/off but **needs precise timing refinement**.

## 🏗️ Project Status & Development Process
### ✅ **Phase 1: Basic MIDI & Audio Processing** (Completed)
- Read and parse MIDI files (extract notes, velocity, tempo, time signature)
- Extract rhythmic/melodic features
- Extract spectral features from audio for texture analysis
- Generate simple classifications (e.g., rhythm type, key detection)

### ✅ **Phase 2: AI-Powered Classification & Tagging** (Completed)
- Train/test models for rhythm & melody style classification
- Implement real-time tagging of input patterns
- Develop UI for users to view analysis results

### ✅ **Phase 3: AI-Powered Variations & MIDI Generation** (Completed)
- Implement rhythm variation algorithm (Markov chains, VAEs)
- Implement melody transformation (style-aware modifications)
- Implement texture-based sound analysis

### ✅ **Phase 4: User Interface & DAW Export** (Completed)
- Build GUI to allow user interaction
- Implement MIDI export for DAW integration
- Optimize UI for usability

## 🛠️ TODO List (Future Steps)

### 🔹 Essential Improvements
- [ ] **Refine MIDI Playback Timing**
  - Ensure **accurate note durations**.
  - Improve **note-off timing** for a natural playback feel.
  - Implement a **tempo-sync feature** to align playback speed with detected tempo.
- [ ] **Improve Beat Quantization & Grid Alignment**
  - Enhance **rhythm accuracy for extracted beats**.
  - Add **bar subdivisions** for better beat visualization.
  - Implement **adjustable quantization levels** (e.g., 16th-note, triplets, etc.).
- [ ] **Optimize Spectrogram & Beat Grid Overlays**
  - Allow **simultaneous spectrogram & MIDI playback**.
  - Overlay **detected beats on the spectrogram** for better rhythm analysis.
  - Add **interactive controls** to toggle between different analysis layers.

### 🔹 Additional Enhancements
- [ ] **Export MIDI & Audio Analysis Results**
  - Add functionality to **save extracted MIDI data**.
  - Export **beat timing data as a text file or MIDI**.
  - Implement **batch processing** for multiple files at once.
- [ ] **Enable Real-Time Processing (Stretch Goal)**
  - Implement **real-time rhythm extraction from microphone input**.
  - Visualize **live MIDI performance** in the piano roll.
  - Develop a **real-time MIDI loop generator** to generate variations on the fly.
- [ ] **Machine Learning-Based Enhancements**
  - Train a **deep learning model** to suggest chord progressions based on melody.
  - Implement **style-transfer for melody & rhythm generation**.
  - Develop **AI-assisted MIDI improvisation** based on user input.
- [ ] **Advanced DAW Integration**
  - Enable **drag-and-drop MIDI export** for seamless DAW workflow.
  - Support **Ableton Link** for real-time tempo synchronization.
  - Provide **MIDI effect processing options** (quantization, swing, etc.).

## 🚀 How to Use

### **Requirements**
- Python 3.x
- Required Libraries:
  ```sh
  pip install mido music21 librosa pygame numpy matplotlib PyQt5
  ```

### **Running the Application**
```sh
python main.py
```

### **Loading a File**
1. Click **'Choose File'** to select a MIDI or WAV file.
2. Use the **View Selector** to choose between **Piano Roll, Time Grid, or Spectrogram**.
3. Adjust the **Zoom Slider** to modify the visualization scale.
4. Click **'Extract Features'** to analyze the file.
5. Use **'Play MIDI'** to listen to extracted melodies.

## 📌 Contributing
Contributions are welcome! If you want to improve this tool, feel free to fork this repo and submit a pull request.

## 📜 License
MIT License

