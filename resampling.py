import librosa

def resample_audio(audio, orig_sr, target_sr=16000):
    return librosa.resample(audio, orig_sr=orig_sr, target_sr=target_sr)
