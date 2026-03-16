import librosa
import numpy as np

def generate_mel_spectrogram(audio, sr=16000):
    mel_spec = librosa.feature.melspectrogram(
        y=audio,
        sr=sr,
        n_mels=128,
        hop_length=512
    )

    mel_db = librosa.power_to_db(mel_spec, ref=np.max)
    return mel_db
