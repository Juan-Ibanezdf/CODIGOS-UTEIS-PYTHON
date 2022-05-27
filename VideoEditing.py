# Video Editing
# pip install moviepy
# pip install ffmpeg-python
# Video Editor
import moviepy.editor as vid
from moviepy.editor import clips_array, vfx
# get video info
clip = vid.VideoFileClip("video.mp4")
print(clip.duration)
print(clip.fps)
print(clip.size)
# Trim Video
clip = vid.VideoFileClip("video.mp4")
clip = clip.subclip(0, 5)
clip.write_videofile("trimmed.mp4")
#Speed up video
clip = vid.VideoFileClip("video.mp4")
clip = clip.speedx(2)
clip.write_videofile("speed_up.mp4")
#Add Transition
clip = vid.VideoFileClip("video.mp4")
clip = clip.fx( vfx.fadein, duration=2)
clip.write_videofile("transition.mp4")
#Add Audio
clip = vid.VideoFileClip("my_video.mp4")
audio = vid.AudioFileClip("my_audio.mp3")
clip = clip.set_audio(audio)
clip.write_videofile("output.mp4")
#Crop Video
clip = vid.VideoFileClip("video.mp4")
clip = clip.crop(x1=0, y1=0, x2=100, y2=100)
clip.write_videofile("cropped.mp4")
#Resize Video
clip = vid.VideoFileClip("video.mp4")
clip = clip.resize(width=200)
clip.write_videofile("resized.mp4")
# Fade in/out
clip = vid.VideoFileClip("video.mp4")
clip = clip.fx( vfx.fadein, duration=2)
clip = clip.fx( vfx.fadeout, duration=2)
clip.write_videofile("fade_in_out.mp4")
# Stack Video Clips
clip1 = vid.VideoFileClip("test_vid.mp4").margin(10)
clip2 = clip1.fx( vfx.mirror_x)
clip3 = clip1.fx( vfx.mirror_y)
clip4 = clip1.resize(0.30)
final_clip = clips_array([[clip1, clip2],[clip3, clip4]])
final_clip.resize(width=720).write_videofile("stacked.mp4")
# Concatenate Video Clips
clip1 = vid.VideoFileClip("test_vid1.mp4")
clip2 = vid.VideoFileClip("test_vid2.mp4")
output = vid.concatenate_videoclips([clip1, clip2])
output.write_videofile("concatenated.mp4")