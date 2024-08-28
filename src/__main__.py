import os 
import sys
import DASO
from rich.console import Console
from rich.table import Table
from colorama import Fore, Style
import questionary
from tqdm import tqdm
import time

# Initialize console
console = Console()

def truncate_string(s: str, max_length: int) -> str:
    """Truncate a string to a maximum length and add '...' if truncated.

    Args:
        s (str): The string to truncate.
        max_length (int): The maximum length of the truncated string.

    Returns:
        str: The truncated string.
    """
    return s if len(s) <= max_length else s[:max_length-3] + '...'

def main(arg: str) -> None:
    """Main function of the program.

    Args:
        arg (str): The search keyword.
    """
    result = DASO.search_yt_audio_from_keyword(arg)
    print(f"\nShowing results for '{arg}':\n")

    # Set fixed widths for each column
    title_width = 30
    duration_width = 10
    views_width = 15

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("No.", style="dim cyan", width=6)
    table.add_column("Title", width=title_width, overflow="ellipsis")
    table.add_column("Duration", justify="right", width=duration_width)
    table.add_column("Views", justify="right", width=views_width)

    for i, video in enumerate(result['result']):
        video_title = truncate_string(video.get('title', 'No Title'), title_width)
        video_duration = truncate_string(video.get('duration', 'N/A'), duration_width)
        video_view_count = truncate_string(video.get('viewCount', {}).get('short', 'N/A'), views_width)

        if video_view_count is not None and isinstance(video_view_count, str):
            video_view_count = video_view_count.replace('views','')
        else:
            video_view_count = 'N/A'  # Default value in case of None or non-string

        table.add_row(str(i + 1), video_title, video_duration, video_view_count)

    console.print(table)

    questions = [
        {
            'type': 'input',
            'name': 'choice',
            'message': 'Choose a video to play:',
        }
    ]

    choice = questionary.select(
        "Choose a video to play:",
        choices=[f"{i+1}. {video['title']}" for i, video in enumerate(result['result'])]
    ).ask()

    # Convert choice to index
    choice_index = int(choice.split('.')[0]) - 1
    url = result['result'][choice_index]['link']

    try:
        DASO.stream_youtube_audio(url)
    except Exception as e:
        print(f'An error occurred while trying to play the audio, {e}')

if __name__ == '__main__':
    argument = ' '.join(sys.argv[1:]) # Get the arguments passed to the program
    if argument == '':
        print('You must provide a search keyword as a argument.')
        print('Example: DASO never gonna give you up')
        sys.exit(1)

    main(argument)
    sys.exit(0) # Exit without errors
