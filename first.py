from pytube import YouTube

def get_youtube_video_views(url):
    try:
        yt = YouTube(url)
        views = yt.views
        print(f"Views: {views}")
        return views
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with any video URL
print(get_youtube_video_views(video_url))
