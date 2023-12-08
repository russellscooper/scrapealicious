#Tools used in the core functionality of the application 
import requests
import re
from bs4 import BeautifulSoup as bs

#Abstract class for endpoint scanning
class Scanner:
    """
    This code defines a class called Scanner with a constructor (__init__ method) that 
    takes a target_url parameter and initializes an instance variable self.target_url with this value.
    """
    def __init__(self, target_url) -> None:
        self.target_url = target_url
        """class constructor"""

    def extractor(self):
        """
        extractor method: This method sends a GET request to the specified target_url using the requests library, 
        retrieves the response, and then uses a regular expression (re) to find all URLs (starting with "http://" or "https://") 
        in the response text. 
        These URLs are then stored in the candidates list, which is returned by the method.
        """
        response = requests.get(self.target_url)
        candidates = []

        for catch in re.finditer(r"(https?://\S+)", response.text):
            candidates.append(catch.group(1))
        
        return candidates
    
    def validate_endpoint(self, candidates):
        """
        validate_endpoint method: This method takes a list of URLs (candidates) as input, sends GET requests to each URL, 
        and checks if the HTTP status code of the response is 200, 201, or 202. 
        If the status code is one of these values, the URL is considered valid and is added to the validated list. 
        The method returns the list of validated URLs.
        """
        validated = []

        for endpoint in candidates:
            try:
                endpoint_response = requests.get(endpoint)
                if endpoint_response.status_code in [200, 201, 202]:
                    validated.append(endpoint)
            except requests.exceptions.RequestException:
                pass

        return validated

   
    def scan_for_endpoints(self):
        """
    scan_for_endpoints method: This method calls the extractor method to get a list of URLs (candidates).
    It then calls the validate_endpoint method to filter out the valid URLs. 
    The final list of validated URLs is returned by this method.
    """
        c = self.extractor()
        v = self.validate_endpoint(c)
        return v
    
class Security():
    """This code attempts to apply security features to the applications features."""
    def __init__(self, secure) -> None:
        """
        Class constructor for security features
        """
        self.secure = secure
    
    def secure_string(self, user_string, max_length=255):
        """
        Method to secure user input strings
        """
        if isinstance(user_string, str):
            #rws stands for removed white space
            rws_string = user_string.strip()
            #rtc stands for remove threat characters
            rtc_string = re.sub(r"[;'\"]", '', rws_string)

            #enforce length limitation policy
            if len(rtc_string) > max_length:
                raise ValueError(f"Input exceeds maximum length of {max_length} characters.")
            return rtc_string
        else:
            raise ValueError("Invalid input type. Please provide a sting.")
    
    def ensure_tls(self, target_url):
        if not 'https://' in target_url:
            tls_string = 'https://' + target_url
        else:
            target_url = tls_string
        
        return tls_string

class Crawler:

    def __init__(self, start_url) -> None:
        self.start_url = start_url
        self.visited = set()
        self.api_endpoints = []
    
    def crawl(self, urls):
        '''
        Crawls a list of urls and extracts potential api endpoints
        '''
        api_endpoints = []
        for url in urls:
            if url in self.visited:
                continue

            try:
                response = requests.get(url)
            except Exception as e:
                print(f'Error fetching url: {e}')
                continue

            soup = bs(response.content, "lxml")

            links = soup.find_all("a", href=True)

            for link in links:
                href = link["href"]
                if not href.startswith("https"):
                    href = f"{self.start_url}/{href}"

                if href not in self.api_endpoints and self.is_api_endpoint(href):
                    api_endpoints.append(href)
        
        return api_endpoints
            


    def is_api_endpoint(self, url):
        '''
        Check if url is an api endpoint based on file type.
        '''
        extension = url.split(".")[-1]
        return extension in ["json","xml","yaml"]
    
    def get_api_endpoints(self):
        '''
        Return a list of discovered API endpoints.
        '''
        return self.api_endpoints
    