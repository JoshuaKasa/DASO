from pytube import YouTube
from youtubesearchpython import VideosSearch
import time
import vlc
import keyboard

def format_time(seconds):
    """Convert seconds to MM:SS format."""
    minutes, seconds = divmod(int(seconds), 60)
    return f"{minutes:02d}:{seconds:02d}"

def stream_youtube_audio(url):
    # Fetching the YouTube video
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').first()  # Highest bitrate
    audio_url = audio_stream.url  # Get the audio url

    # Using VLC to play the audio
    player = vlc.MediaPlayer(audio_url)
    player.play()
    time.sleep(1)  # Wait for player to start

    is_playing = True  # Variable to track play/pause state
    volume = 100  # Initial volume set to 100%
    player.audio_set_volume(volume) # Set the initial volume

    try:
        while True:
            time.sleep(0.1)  # A shorter sleep time for more responsive keyboard interaction

            # Adjust volume with up/down arrows
            if keyboard.is_pressed('down'):
                volume = max(0, volume - 5)  # Decrease volume, but not less than 0%
                player.audio_set_volume(volume)
                while keyboard.is_pressed('down'):
                    time.sleep(0.1)

            if keyboard.is_pressed('up'):
                volume = min(100, volume + 5)  # Increase volume, but not more than 100%
                player.audio_set_volume(volume)
                while keyboard.is_pressed('up'):
                    time.sleep(0.1)

            # Check if spacebar is pressed for play/pause
            if keyboard.is_pressed('space'):
                if is_playing:
                    player.pause()
                    is_playing = False
                    print("[Paused]", end='\r')
                else:
                    player.play()
                    is_playing = True
                    print("[Playing]", end='\r')
                while keyboard.is_pressed('space'):  # Wait until space is released
                    time.sleep(0.1)

            if is_playing:
                # We can print over the previous line using \r and end='\r', which is the carriage return character
                current_time = player.get_time() // 1000
                total_time = yt.length
                print(f"[Playing] {format_time(current_time)}/{format_time(total_time)} - Volume: {volume}%", end='\r')

    except KeyboardInterrupt:
        pass  # Press Ctrl+C to stop
    finally:
        print()  # Ensure the next print starts on a new line
        player.stop()  # Stop the player


def search_yt_audio_from_keyword(keyword: str) -> str | dict:
    # Search the keyword on YouTube
    videosSearch = VideosSearch(keyword, limit=10)
    result = videosSearch.result()

    return result
