import mido
import numpy as np
import matplotlib.pyplot as plt
import music21
import librosa
import librosa.display
import pygame.midi
from mido import MidiFile, Message, MidiTrack, MidiFile
from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton, QVBoxLayout, QWidget, QLabel, QSlider, QHBoxLayout, QComboBox
from PyQt5.QtCore import Qt

# Function to extract and simplify rhythm patterns from MIDI
def extract_simplified_rhythm(midi_path):
    mid = MidiFile(midi_path)
    beat_times = []
    ticks_per_beat = mid.ticks_per_beat
    
    for track in mid.tracks:
        time_counter = 0
        for msg in track:
            time_counter += msg.time
            if msg.type == 'note_on':
                beat_times.append(time_counter / ticks_per_beat)
    
    return np.round(np.array(beat_times) % 4, 2)  # Quantized beats normalized to a 4-beat measure

# Function to extract melody features with harmonic analysis
def extract_melody_features(midi_path):
    score = music21.converter.parse(midi_path)
    key = score.analyze('key')
    notes = []
    chords = []
    
    for part in score.parts:
        for element in part.flat.notes:
            if isinstance(element, music21.note.Note):
                notes.append((element.pitch.midi, element.offset, element.quarterLength))
            elif isinstance(element, music21.chord.Chord):
                chords.append((element.pitchedCommonName, element.offset))
    
    return {
        'key': key.name,
        'pitch_contour': notes,
        'chords': chords
    }

# Function to play extracted MIDI melody
def play_midi(melody_data):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(0)
    
    for pitch, onset, duration in melody_data['pitch_contour']:
        player.note_on(pitch, 127)
        pygame.time.wait(int(duration * 500))
        player.note_off(pitch, 127)
    
    pygame.midi.quit()

# Function to visualize piano roll with chord annotations
def plot_piano_roll(melody_data):
    fig, ax = plt.subplots(figsize=(12, 6))
    for pitch, onset, duration in melody_data['pitch_contour']:
        ax.barh(pitch, duration, left=onset, height=1, color='blue')
    
    for chord, onset in melody_data['chords']:
        ax.text(onset, 100, chord, fontsize=10, color='red', rotation=45)
    
    ax.set_xlabel("Time (beats)")
    ax.set_ylabel("MIDI Pitch")
    ax.set_title(f"Piano Roll - Key: {melody_data['key']}")
    ax.grid()
    return fig

# Function to extract rhythm features from audio
def extract_rhythm_from_audio(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = np.round(librosa.frames_to_time(beat_frames, sr=sr), 2)
    return {'tempo': tempo, 'beat_times': beat_times}

# Function to extract and plot spectral features from audio
def extract_and_plot_spectral_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    
    # Compute MFCCs
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    
    # Compute STFT
    stft = np.abs(librosa.stft(y))
    
    # Plot MFCCs
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(mfccs, sr=sr, x_axis='time')
    plt.colorbar()
    plt.title('MFCC')
    plt.tight_layout()
    plt.show()
    
    # Plot STFT
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.amplitude_to_db(stft, ref=np.max), sr=sr, y_axis='log', x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('STFT Magnitude')
    plt.tight_layout()
    plt.show()

# GUI Application using PyQt5
class FeatureExtractionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.zoom = 1.0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MIDI & Audio Feature Extraction')
        self.setGeometry(100, 100, 600, 400)
        
        layout = QVBoxLayout()
        
        self.label = QLabel('Select a MIDI or WAV file:')
        layout.addWidget(self.label)
        
        self.file_button = QPushButton('Choose File')
        self.file_button.clicked.connect(self.open_file)
        layout.addWidget(self.file_button)
        
        self.play_button = QPushButton('Play MIDI')
        self.play_button.clicked.connect(self.play_midi)
        layout.addWidget(self.play_button)
        
        zoom_layout = QHBoxLayout()
        self.zoom_label = QLabel("Zoom: 1.0x")
        self.zoom_slider = QSlider(Qt.Horizontal)
        self.zoom_slider.setMinimum(1)
        self.zoom_slider.setMaximum(10)
        self.zoom_slider.setValue(1)
        self.zoom_slider.valueChanged.connect(self.update_zoom)
        zoom_layout.addWidget(self.zoom_label)
        zoom_layout.addWidget(self.zoom_slider)
        layout.addLayout(zoom_layout)
        
        self.view_selector = QComboBox()
        self.view_selector.addItems(["Piano Roll", "Time Grid", "Spectrogram"])
        layout.addWidget(self.view_selector)
        
        self.extract_button = QPushButton('Extract Features')
        self.extract_button.clicked.connect(self.extract_features)
        layout.addWidget(self.extract_button)
        
        self.setLayout(layout)
    
    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "MIDI Files (*.mid);;Audio Files (*.wav)", options=options)
        if file_name:
            self.file_path = file_name
            self.label.setText(f'Selected: {file_name}')
    
    def update_zoom(self, value):
        self.zoom = value / 2.0
        self.zoom_label.setText(f"Zoom: {self.zoom}x")
    
    def extract_features(self):
        if hasattr(self, 'file_path'):
            if self.file_path.endswith('.mid'):
                melody_data = extract_melody_features(self.file_path)
                selected_view = self.view_selector.currentText()
                
                if selected_view == "Piano Roll":
                    fig = plot_piano_roll(melody_data)
                
                plt.show()
            elif self.file_path.endswith('.wav'):
                # Call the new function to extract and plot spectral features
                extract_and_plot_spectral_features(self.file_path)
                rhythm_data = extract_rhythm_from_audio(self.file_path)
                print("Detected Tempo:", rhythm_data['tempo'])
                print("Beat Times:", rhythm_data['beat_times'])
    
    def play_midi(self):
        if hasattr(self, 'file_path') and self.file_path.endswith('.mid'):
            melody_data = extract_melody_features(self.file_path)
            play_midi(melody_data)

# Run the Application
if __name__ == "__main__":
    app = QApplication([])
    window = FeatureExtractionApp()
    window.show()
    app.exec_()
