# Audio Editing
# pip install pydub
import pydub as audio
# Load audio file
audio_file = audio.AudioSegment.from_wav("audio.wav")
# Playing an audio
audio_file.play()
# Remove Noise
audio_file = audio.AudioSegment.from_mp3("audio.mp3")
audio_file.low_pass_filter(5000).high_pass_filter(200)
audio_file.export("audio_noise_removed.mp3", format="mp3")
#combine two audio files
audio_file_1 = audio.AudioSegment.from_mp3("audio1.mp3")
audio_file_2 = audio.AudioSegment.from_mp3("audio2.mp3")
combine_audio = audio_file_1 + audio_file_2
combine_audio.export("combine_audio.mp3", format="mp3")
# Extract Audio from Video
video_file = audio.AudioSegment.from_file("my_video.mp4", format="mp4")
video_file.export("video.wav", format="wav")
# Split Audio
audio_file = audio.AudioSegment.from_mp3("audio.mp3")
audio_file[:10000].export("audio_1.mp3", format="mp3")
audio_file[10000:].export("audio_2.mp3", format="mp3")
# Audio to Text
audio_file = audio.AudioSegment.from_mp3("audio.mp3")
text = audio_file.split_to_mono()
print(text)
# Text to Audio
text = "Hi From Medium"
audio_file = audio.AudioSegment.from_wav("audio.wav")
audio_file = audio_file.overlay(text)
audio_file.export("audio_text.mp3", format="mp3")
# Increase Volume
audio_file = audio.AudioSegment.from_mp3("audio.mp3")
audio_file = audio_file + 3
audio_file.export("audio_volume_increased.mp3", format="mp3")