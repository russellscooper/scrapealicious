#Tools used in the core functionality of the application 
import requests
import re

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
    
    
#Test Case 
Scan = Scanner("https://twitter.com/home")
Data = Scan.scan_for_endpoints()
print(Data)
