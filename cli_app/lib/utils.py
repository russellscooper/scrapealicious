import os
import requests 
#Objects that help with file management

class FileWriter:

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, data, mode="w"):
        with open(self.file_path, mode) as f:
            f.write(data)

    def write_lines(self, lines, mode="a"):
        with open(self.file_path, mode) as f:
            f.writelines(lines)

    def append(self, data):
        self.write(data, mode="a")

#Objects that help with time management 

#Objects that provides the user with downloads
class Downloader:

    def download_file(self, url, filename=None):
        """
        Downloads a file from the given URL to the user's Downloads folder.

        Args:
            url: The URL of the file to download.
            filename: The filename to save the downloaded file as (optional).
        """

        if not filename:
            if isinstance(url, list):
                url = url[0]
                
        filename = os.path.basename(url)

        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

        # Ensure downloads folder exists
        os.makedirs(downloads_folder, exist_ok=True)

        # Download the file
        with requests.get(url, stream=True) as response:
            response.raise_for_status()

            with open(os.path.join(downloads_folder, filename), "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

        print(f"Downloaded file: {filename} to Downloads folder")