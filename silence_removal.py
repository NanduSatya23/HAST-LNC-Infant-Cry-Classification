import librosa

def remove_silence(audio):
    intervals = librosa.effects.split(audio, top_db=20)
    non_silent_audio = []
    
    for start, end in intervals:
        non_silent_audio.extend(audio[start:end])
    
    return non_silent_audio
