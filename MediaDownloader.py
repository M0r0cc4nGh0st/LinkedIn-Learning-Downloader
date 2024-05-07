import os
import requests


class ContentDownloader:
    def __init__(self, base_directory):
        self.base_directory = base_directory

    def download_subtitle(self, subtitle, full_path, file_name):
        file_path = os.path.join(self.base_directory, full_path, file_name)
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))

        with open(file_path, 'w', encoding='utf-8') as file:
            count = 1
            for i, line in enumerate(subtitle):
                start = line['transcriptStartAt'] // 1000  # Convert milliseconds to seconds
                start_ms = line['transcriptStartAt'] % 1000  # Remainder as milliseconds

                if i < len(subtitle) - 1:
                    end = subtitle[i + 1]['transcriptStartAt'] // 1000
                    end_ms = subtitle[i + 1]['transcriptStartAt'] % 1000
                else:
                    end = start + 5
                    end_ms = 0

                start_hours, start_remainder = divmod(start, 3600)
                start_minutes, start_seconds = divmod(start_remainder, 60)

                end_hours, end_remainder = divmod(end, 3600)
                end_minutes, end_seconds = divmod(end_remainder, 60)

                file.write(f"{count}\n")
                file.write(
                    f"{start_hours:02}:{start_minutes:02}:{start_seconds:02},{start_ms:03} --> {end_hours:02}:{end_minutes:02}:{end_seconds:02},{end_ms:03}\n")
                file.write(f"{line['caption']}\n\n")
                count += 1

    def download_video(self, url, full_path, file_name):
        file_path = os.path.join(self.base_directory, full_path, file_name)
        if os.path.exists(file_path):
            print(f"\033[31m[!] ------ The video already exists, skipping download.\033[0m")
            return

        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))

        reply = requests.get(url, stream=True)
        with open(file_path, 'wb') as f:
            for chunk in reply.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
