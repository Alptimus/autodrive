# Autodrive: Automating Google Drive Backup with Python

## Introduction

This script automates the process of backing up files from a local directory to a Google Drive folder. By leveraging the Google Drive API, it ensures that only new or modified files are uploaded, saving time and bandwidth. This guide walks you through setting up the necessary API credentials and using the script for automated backups.

## Setting Up Google Drive API

1. **Create a Project on Google Cloud Platform**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Click on the project dropdown in the top left corner and select "New Project".
   - Give your project a name and create it.

2. **Enable Google Drive API**:
   - In the Google Cloud Console, navigate to "API & Services" > "Library".
   - Search for "Google Drive API" and enable it.

3. **Create OAuth 2.0 Credentials**:
   - Go to "API & Services" > "Credentials".
   - Click on "Create Credentials" and select "OAuth 2.0 Client ID".
   - You might be prompted to configure the OAuth consent screen. Fill out the necessary information and save.
   - Choose "Desktop app" as the application type and provide a name.
   - Click "Create" to generate your credentials.
   - Download the `credentials.json` file and save it in your project directory.

4. **Add Test Users**:
   - Navigate to "API & Services" > "OAuth consent screen".
   - Scroll down to the "Test users" section and click "Add users".
   - Enter the email addresses of users who should have access to the app during testing and save the changes.

## Script Workflow

1. **Authenticate**:
   - The script uses OAuth 2.0 to authenticate users. The `credentials.json` file contains the client ID and client secret.
   - If the token file (`token.json`) exists, it loads the credentials from it. If not, it initiates the OAuth 2.0 flow and saves the obtained token for future use.

2. **List Files in Google Drive Folder**:
   - The script retrieves the list of files currently in the specified Google Drive folder and stores their metadata in a dictionary.

3. **Upload New or Modified Files**:
   - It iterates over the local files in the source directory, checks if they already exist in the Google Drive folder, and compares their sizes.
   - Only files that do not exist or have different sizes are uploaded, avoiding redundant uploads.

## Advantages

- **Efficiency**: By uploading only new or modified files, the script saves time and bandwidth.
- **Automation**: Once set up, the script can be run as a scheduled task or cron job, ensuring regular backups without manual intervention.
- **Simplicity**: The script is straightforward and easy to understand, making it accessible for users with basic Python knowledge.

## How to Contribute

We welcome contributions to improve and optimize this script. Here are a few ways you can help:

1. **Enhance Error Handling**: Improve the script's robustness by adding more comprehensive error handling.
2. **Optimize File Comparison**: Implement more sophisticated file comparison methods, such as hash-based comparison.
3. **Add Features**: Introduce new features like email notifications after backups, support for multiple source directories, or improved logging.
4. **Improve Documentation**: Enhance this README with more detailed instructions, troubleshooting tips, or examples.

To contribute, fork the repository, make your changes, and submit a pull request. We look forward to your contributions!

## Conclusion

This script provides an efficient and automated way to back up files to Google Drive. By leveraging the Google Drive API and OAuth 2.0, it ensures secure and streamlined backups. Whether for personal use or as part of a larger automation workflow, this script is a valuable tool for maintaining up-to-date backups with minimal effort.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

By following this guide, you'll be able to automate your file backups to Google Drive effectively. Feel free to customize the script to suit your specific needs and contribute to its improvement.