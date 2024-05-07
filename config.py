
TOKEN = "Put your Li_AT token here"

URLS = [
    "https://www.linkedin.com/learning/html-essential-training-4",
    # "https://www.linkedin.com/learning/css-essential-training-22688362",
    # "https://www.linkedin.com/learning/javascript-essential-training-3",
    # "https://www.linkedin.com/learning/python-essential-training-2",
    # "https://www.linkedin.com/learning/java-essential-training-3"
]
SUBTITLES = False # Set to True to download subtitles

DOWNLOAD_DIRECTORY = None # Set the download directory here ex: "C:/Users/Username/Desktop/LinkedIn Learning Courses"


def load_config():
    return [TOKEN, URLS, SUBTITLES, DOWNLOAD_DIRECTORY] if TOKEN else None




