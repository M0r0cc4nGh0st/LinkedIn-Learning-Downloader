[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://youneswinter.pro) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://forthebadge.com)
# LinkedIn Learning Downloader [Updated V1.2]

> Welcome to the introduction of the LinkedIn Learning Courses Downloader, an innovative tool designed to enhance your learning experience by enabling offline access to LinkedIn Learning courses. This powerful tool is designed for learners who seek flexibility in their educational pursuits, allowing them to access content anywhere, anytime, without the need for continuous internet connectivity.

## Core Features:

* **Comprehensive Course Extraction :** Users can easily extract and download full courses, including video content and accompanying materials, directly from provided URLs.
* **Advanced Downloading Capabilities :** The downloader manages video, description, and crucially, exercise files which are often pivotal for hands-on learning experiences. The tool organizes content by chapters and maintains a structured directory of downloaded materials.
* **Support for Subtitles and Transcripts :** Enhancing accessibility, the tool supports the download of subtitles and detailed transcripts for each video, catering to diverse learning needs and preferences.
* **Concurrent Downloads :** Utilizing a ThreadPoolExecutor, the tool allows multiple courses to be downloaded simultaneously, optimizing time and system resources efficiently.
* **Robust Error Handling and Security :** The tool is equipped with robust error handling to manage and relay issues effectively. Secure authentication via a token-based system ensures user credentials are protected.
* **Installer with Enhanced Features :** The custom installer not only sets up the tool seamlessly but also enables the download of exercise files, making it a complete learning package for users who require comprehensive educational resources.

## Screenshot of the Tool
[![ScreenShot](https://private-user-images.githubusercontent.com/157702486/348448784-f159d0c7-5562-417b-b840-cc70dd1558c7.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjA4NDU1MDYsIm5iZiI6MTcyMDg0NTIwNiwicGF0aCI6Ii8xNTc3MDI0ODYvMzQ4NDQ4Nzg0LWYxNTlkMGM3LTU1NjItNDE3Yi1iODQwLWNjNzBkZDE1NThjNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNzEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDcxM1QwNDMzMjZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02MTJlYjA5NjgxMGJjMzU4Y2IzYjUwYTdkOGFkODAxYjM0NjkwZWI0OTk5MGI5YTI4NjJiMDgxODljODRhYmJlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.MonPMbjWyPUH_527q7weaXuAoDGIdnydRpoSdClm8Zc)](https://youneswinter.pro)



## [![forthebadge](https://forthebadge.com/images/badges/platform-windows.svg)](https://youneswinter.pro)
For now, the tool is supported only on Windows, but there will be support for other operating systems in future updates.
<p><a href="https://github.com/M0r0cc4nGh0st/LinkedIn-Learning-Downloader/releases/" ><img src="https://raw.githubusercontent.com/Hacking4Arabs/19f49d852660fe0a079cbf95c3efb34ba88de911/main/images/download.png" width="300" height="100" alt="download" ></a> to download the Tool.</p>


## Compatibility
The LinkedIn Learning Downloader is built as a standalone application using Nuitka, which means it includes all necessary Python and PyQt libraries. There is no need to install Python or any specific libraries on your system to run this tool. Simply download and run the installer, and the application will operate smoothly on any Windows system that meets the basic operating requirements.

### System Requirements
- Operating System: Windows 7 or later.
- Hard Disk Space: At least 100 MB free for installation and additional space for downloaded courses.
- Internet Connection: Required for downloading courses and updates.

## How to Use the Open Source Scripts

To use the open-source scripts, follow these steps:

1. **Install Python 3.12**:
   - Download Python 3.12 from the [official Python website](https://www.python.org/downloads/release/python-3124/).
   - Follow the installation instructions for your operating system.
   - Ensure that Python is added to your PATH during the installation process.

2. **Configuration**:
   - Add your token and course link in the `config.py` file.

3. **Run the Script**:
   - Execute the script using the following command:
     ```bash
     python main.py
     ```

## How to Obtain Your `li_at` Token Using EditThisCookie

The `li_at` token is a LinkedIn authentication token that is necessary for the LinkedIn Learning Downloader to function. You can retrieve this token from your browser by using the EditThisCookie extension. Here's a step-by-step guide:

### Step 1: Install the EditThisCookie Extension
1. Go to your browser's web store (Chrome Web Store, Firefox Add-ons, Brave, etc.).
2. Search for "EditThisCookie" and select the extension.
3. Click "Add to Browser" to install the extension.

### Step 2: Access LinkedIn
1. Open your browser and navigate to [LinkedIn Learning](https://www.linkedin.com/learning).
2. Log in with your LinkedIn credentials.

### Step 3: Use EditThisCookie to Retrieve the `li_at` Token
1. Once logged in, click on the EditThisCookie icon in your browser's toolbar. It usually appears as a cookie or a pencil icon.
2. A list of cookies will appear. Scroll through them or use the search bar to find the cookie named `li_at`.
3. Click on the `li_at` cookie to expand its details.
4. Copy the Value field of the `li_at` cookie. This is the token needed by the LinkedIn Learning Downloader.

### Step 4: Use the Token in the LinkedIn Learning Downloader
1. Open the LinkedIn Learning Downloader.
2. Navigate to the settings or authentication section where the `li_at` token is required.
3. Paste the token into the designated field and save your settings.

### Note
- **Keep your `li_at` token secure** and do not share it with others. This token gives access to your LinkedIn account.
- If you encounter issues with the token or it appears to be invalid, try logging out of LinkedIn and then logging back in to generate a new token.


## Demo
[![Demonstration](https://raw.githubusercontent.com/Hacking4Arabs/19f49d852660fe0a079cbf95c3efb34ba88de911/main/images/video.png)](https://youtu.be/pjEK_JEFwJ0)


## Technology Stack:
The LinkedIn Learning Courses Downloader is built entirely using Python, leveraging the PyQt framework for its graphical user interface. This choice of technology ensures that the tool is not only efficient but also flexible and customizable, allowing for rapid enhancements and updates. The use of Python, a powerful and versatile programming language, facilitates complex operations and data handling, while PyQt provides a robust platform for developing user-friendly interfaces.


## Target Audience:
This tool is perfect for students, professionals, and anyone engaged in continuous learning who utilizes LinkedIn Learning but requires or prefers offline access to their training materials.


## Upcoming Enhancements:
* Expansion to support additional operating systems beyond Windows.
* Development of a user-friendly interface to simplify interaction and setup.
* Increased customization options to tailor download preferences.


## FAQ / Troubleshooting
- **Q: The downloader is stuck at 'Initializing...' What should I do?**
  - A: Check your internet connection and ensure you're logged in correctly. If the issue persists, restart the tool.
- **Q: Can I download multiple courses at once?**
  - A: Yes, the tool supports concurrent downloads. Just add the courses to the queue.
- **Q: Is it possible to download exercise files along with the courses?**
  - A: Yes, our tool uniquely supports the download of exercise files even when they are not accessible through the standard API. This is accomplished using Selenium to simulate user interactions on the website, ensuring you have all necessary materials for a complete learning experience.



## Help fuel my genius — every little bit helps!

If you please, keep my creative gears oiled.

You can support its development by contributing through Ko-fi or PayPal. Your donations help keep the project alive and kicking, fund new features, and maintain the high level of support. Every little bit counts!

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/youneswinter)
[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/YonesWinter)

## Join the Discussion

Engage with the community on the GitHub Discussions page! Whether you have questions, suggestions, or need support, this is the perfect place to connect and share.

### How to Participate
- **Ask a Question:** Need help? Post your questions and get assistance.
- **Share Ideas:** Have suggestions? I'm eager to hear your innovative ideas.
- **Report Bugs:** Found a problem? Let me know and help improve the tool.

### Access Discussions
Visit the [Discussions Page](https://github.com/M0r0cc4nGh0st/LinkedIn-Learning-Downloader/discussions) and start engaging today!

I look forward to your contributions!


## Antivirus Notifications

### Why Might This Happen?
The LinkedIn Learning Downloader may sometimes be flagged by antivirus software as potentially suspicious. This is a common occurrence with many legitimate software tools, especially those that automate downloads or manipulate files and network interactions, like this tool does.

### What Should You Do?
1. **Verify the Source:** Always ensure you download the tool directly from the official [GitHub repository](https://github.com/M0r0cc4nGh0st/LinkedIn-Learning-Downloader) or the project's website to guarantee you're using the authentic version.
2. **Whitelist the Application:** If you trust the tool and understand the alert, consider adding an exception in your antivirus software to prevent future interruptions. Here's how you can typically whitelist an application:
   - Open your antivirus software.
   - Go to the settings or quarantine section.
   - Find the option to add exceptions or exclusions.
   - Add the LinkedIn Learning Downloader executable to the list of exclusions.


## License
This software is released under the GNU Affero General Public License (AGPL), version 3. This means that any modifications to the code or derivative work must also be made available under the same license. For more details, see the LICENSE file included with the program or visit [GNU AGPL v3](https://www.gnu.org/licenses/agpl-3.0.en.html).


## Disclaimer
This tool is intended to help users download LinkedIn Learning courses for which they have valid subscriptions and access rights. Users are responsible for ensuring their use of the tool complies with LinkedIn's Terms of Service and applicable laws. The author is not responsible for any misuse of this software.  

[![forthebadge](https://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://forthebadge.com)

