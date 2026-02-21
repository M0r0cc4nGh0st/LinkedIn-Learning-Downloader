[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://youneswinter.xyz) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://youneswinter.xyz) [![forthebadge](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://youneswinter.xyz)
# LinkedIn Learning Downloader [Updated V1.4] [![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/YonesWinter)

> Welcome to the LinkedIn Learning Downloader, an innovative tool designed to enhance your learning experience by enabling offline access to LinkedIn Learning courses. This powerful tool is designed for learners who seek flexibility in their educational pursuits, allowing them to access content anywhere, anytime.

## Patch Update V1.4
This major update introduces a seamless login experience, improved download controls, and enhanced reliability.
- 🔐 **Unified LinkedIn Login**: No more manual cookie copying. Log in directly through the app.
- ⏸ **Pause / Resume / Cancel**: Full control over your download queue.
- 🌐 **Auto-Pause & Resume**: Automatically pauses downloads if the internet cuts out and resumes once power is restored.
- 📂 **Learning Path Support**: Download entire Learning Paths with a single URL.
- 🍪 **Secure Session**: Encrypted cookie storage with OS keyring integration for a safer experience.

## Core Features:

* **Comprehensive Course Extraction :** Easily extract and download full courses, including video content and accompanying materials, directly from course URLs or Learning Paths.
* **Advanced Downloading Capabilities :** Manages videos, descriptions, and exercise files. Content is organized by chapters in a structured directory.
* **Support for Subtitles and Transcripts :** Download subtitles and detailed transcripts for each video for diverse learning needs.
* **Parallel & Sequential Downloads :** Choose between downloading multiple courses at once or one by one to optimize your resources.
* **Robust Error Handling :** Intelligent management of network issues and server errors.
* **Exercise File Scraping :** Utilizes a headless browser to ensure exercise files are correctly extracted even when restricted.
> 🆕 **Freemium Beta:** Includes a server-controlled freemium mode for free course downloads.

## Screenshot of the Tool
[![ScreenShot](https://youneswinter.xyz/media/static/v1.4.png)](https://youneswinter.xyz)

## [![forthebadge](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://youneswinter.xyz) [![forthebadge](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://youneswinter.xyz)
Currently, the tool is supported only on Windows.
<p><a href="https://github.com/M0r0cc4nGh0st/LinkedIn-Learning-Downloader/releases/" ><img src="https://raw.githubusercontent.com/Hacking4Arabs/19f49d852660fe0a079cbf95c3efb34ba88de911/main/images/download.png" width="300" height="100" alt="download" ></a> to download the Tool.</p>


## Compatibility
The LinkedIn Learning Downloader is built as a standalone application. There is no need to install Python or any specific libraries. Simply download and run the installer.

### System Requirements
- **Operating System:** Windows 7 or later.
- **Web Browser:** Chrome, Brave, or Edge must be installed for the login process.
- **Hard Disk Space:** At least 100 MB for installation + space for downloaded courses.
- **Internet Connection:** Required for initialization and downloading.

## How to Use

1. **Launch the App**: Open the LinkedIn Learning Downloader.
2. **Login**: Click the **Login with LinkedIn** button. A secure browser window will open for you to enter your credentials. No manual token or cookie pasting is required!
3. **Add Course**: Paste the LinkedIn Learning course or Learning Path URL.
4. **Download**: Choose your quality and click "Download". Use the **Pause**, **Resume**, or **Cancel** buttons to manage your progress.

## Demo
[![Demonstration](https://raw.githubusercontent.com/Hacking4Arabs/19f49d852660fe0a079cbf95c3efb34ba88de911/main/images/video.png)](https://youtu.be/XU-fWn6ewA4)


## Technology Stack:
Built using **Python** and **PyQt6**. It leverages Selenium for secure authentication and exercise file extraction, and `requests` for fast media downloads.


## Target Audience:
Perfect for students, professionals, and lifelong learners who need offline access to LinkedIn Learning materials for flexible studying.


## FAQ / Troubleshooting
- **Q: Why do I need Chrome/Edge/Brave installed?**
  - A: The tool uses a secure headless browser to handle the LinkedIn login process and to scrape exercise files that aren't available via standard APIs.
- **Q: Does the app save my password?**
  - A: No. The app uses your browser session to authenticate and stores only the session cookie (`li_at`) in an encrypted format using your OS keyring.
- **Q: What happens if my internet disconnects?**
  - A: V1.4 features **Auto-Pause**. The downloader will detect the loss of connection, pause your queue, and automatically resume once you are back online.


## Help fuel my genius — every little bit helps!

[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/YonesWinter)

## Join the Discussion
[GitHub Discussions Page](https://github.com/M0r0cc4nGh0st/LinkedIn-Learning-Downloader/discussions)


## License
GNU Affero General Public License (AGPL) v3.


## Disclaimer
This tool is intended for users with valid subscriptions. Users are responsible for complying with LinkedIn's Terms of Service. The author is not responsible for any misuse.

[![forthebadge](https://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://youneswinter.xyz)
