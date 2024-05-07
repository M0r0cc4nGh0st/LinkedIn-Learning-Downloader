import concurrent
import os
import sys
import requests
import re
import json
from HTTPManager import HTTPManager
from MediaDownloader import ContentDownloader
from DirectoryManager import DirectoryManager
from concurrent.futures import ThreadPoolExecutor
from config import load_config

def extract_courses_names(urls):
    pattern = r"https://[a-z]{2,3}\.linkedin\.com/learning/(.*?)(\?|$)"

    # Extract the course name from each URL
    course_names = []
    for url in urls:
        if "linkedin.com/learning/" not in url:
            # Handle the error case where the URL is not from LinkedIn Learning
            print(f"Error: URL '{url}' is not a valid LinkedIn Learning URL.")
            continue

        match = re.search(pattern, url)
        if match:
            course_names.append(match.group(1))
        else:
            # If no valid course name is found, handle this case as well
            print(f"Error: Could not extract course name from URL '{url}'.")

    return course_names


def extract_course(course, cookies, headers, download_directory, downloader, token, subtitles):

    print('')
    print(f"Starting download for: {course}")
    course_url = 'https://www.linkedin.com/learning-api/detailedCourses' \
                 '??fields=videos&addParagraphsToTranscript=true&courseSlug={0}&q=slugs'.format(course)
    r = requests.get(course_url, cookies=cookies, headers=headers)
    if r.status_code == 200:
        try:
            course_data = r.json()['elements'][0]
            course_name = re.sub(r'[\\/*?:"<>|]', "", course_data['title'])
            course_title = r.json()['elements'][0]['slug']
            course_link = "https://www.linkedin.com/learning/{}".format(course_title)
            course_description = r.json()['elements'][0]['selectedVideo']['course']['description']
            chapters = course_data['chapters']
            print('[*] Parsing "%s" course\'s chapters' % course_name)
            print('[*] [%d chapters found]' % len(chapters))

            # Use a dictionary to map chapter titles to their designated numbers
            chapter_numbers = {}
            for index, chapter in enumerate(chapters):
                if chapter['title'].lower() == 'introduction':
                    chapter_numbers[chapter['title']] = 0
                elif chapter['title'].lower() == 'conclusion':
                    chapter_numbers[chapter['title']] = len(chapters) - 1
                else:
                    chapter_numbers[chapter['title']] = index

            for chapter in chapters:
                chapter_name = re.sub(r'[\\/*?:"<>|]', "", chapter['title'])
                videos = chapter['videos']
                print('[*] --- Parsing "%s" chapters\'s videos' % chapter_name)
                print('[*] --- [%d videos found]' % len(videos))
                counter = 0
                for video in videos:
                    video_name = re.sub(r'[\\/*?:"<>|]', "", video['title'])
                    video_slug = video['slug']
                    video_url = 'https://www.linkedin.com/learning-api/detailedCourses' \
                                '?addParagraphsToTranscript=false&courseSlug={0}&q=slugs&resolution=_720&videoSlug={1}' \
                        .format(course, video_slug)
                    r = requests.get(video_url, cookies=cookies, headers=headers)
                    counter += 1
                    try:
                        download_url = re.search('"progressiveUrl":"(.+)","expiresAt"', r.text).group(1)
                    except AttributeError:
                        print(
                            '[!] ------ Can\'t download the video "%s", probably is only for premium users' % video_name)
                        continue

                    try:
                        # Attempt to extract the transcript
                        transcript = r.json()['elements'][0]['selectedVideo']['transcript']['lines']
                    except (KeyError, IndexError):
                        # Handle missing transcript
                        print('[!] ------ Transcript not available for video "%s".' % video_name)
                        transcript = None  # Proceed with no transcript

                    chapter_number = chapter_numbers[chapter['title']]
                    chapter_name = re.sub(r'^\d+\.\s*', '', chapter_name)
                    chapter_dir = '%s - %s' % (str(chapter_number), chapter_name)
                    filename = '%s. %s.mp4' % (str(counter), video_name)
                    filename_srt = '%s. %s.srt' % (str(counter), video_name)
                    full_path = os.path.join(download_directory, course_name, chapter_dir)
                    print('[*] ------ Downloading video "%s"' % video_name)
                    downloader.download_video(download_url, full_path, filename)
                    if subtitles and transcript is not None:
                        downloader.download_subtitle(transcript, full_path, filename_srt)

            # Download description into the specified path
            downloader.download_description(course_description,
                                            '<p><strong>Course Link</strong> : <a href={0} target="_blank" style="text-decoration:none;">{0}</a>'.format(
                                                course_link), os.path.join(course_name, 'description.html'))

        except (KeyError, IndexError, json.JSONDecodeError) as e:
            print(f"Error processing course {course}: {str(e)}")
    else:
        print(f"Failed to fetch course data for {course}, Status Code: {r.status_code}")
    print(f"Completed download for: {course}")
    print('')


def main():
    config = load_config()
    if config is None:
        sys.exit("Error: Config file not found or invalid.")
    token, urls, subtitles, download_directory = config
    directory_path = DirectoryManager()
    directory_path.set_directory(download_directory)
    download_directory = directory_path.get_directory()

    http_manager = HTTPManager()
    cookies = http_manager.authenticate(token)

    headers = {'Csrf-Token': cookies['JSESSIONID']}
    downloader = ContentDownloader(download_directory)
    courses = extract_courses_names(urls)

    # Set up ThreadPoolExecutor to handle downloads in parallel
    with ThreadPoolExecutor(
            max_workers=5) as executor:  # You can adjust max_workers based on your needs and system capabilities
        # Prepare a list of partial functions each bound to a specific course
        futures = [
            executor.submit(extract_course, course, cookies, headers, download_directory, downloader, token, subtitles)
            for course
            in courses]

        # Optionally, wait for all futures to complete and handle exceptions
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()  # You can use this to handle the results or confirm completion
            except Exception as exc:
                print(f"An error occurred: {exc}")


if __name__ == '__main__':
    main()
