#Sprint One Unit Tests
import unittest
from app.core.tools import Scanner, Security

class ScannerTest(unittest.TestCase):
    def exctractor_test(self):
        '''
        Verify that the exctractor method can exctract URLs from target URL.
        '''
        scanner = Scanner('https://www.google.com')
        extracted_urls = scanner.extractor()
        self.assertTrue(len(extracted_urls) > 0)

    def test_validate_endpoint(self):
        '''
        Verify that the endpoint validation can filter invalid URLs.
        '''
        scanner = Scanner('https://www.google.com')
        extracted_urls = scanner.extractor()
        valid_urls = scanner.validate_endpoint(extracted_urls)
        self.assertTrue(len(valid_urls) > 0)

    def test_scan_for_endpoints(self):
        '''
        Verify that the exctractor and validator can work together to provide a comprehensive
            list of valid urls. 
        '''
        scanner = Scanner('https://www.google.com')
        valid_urls = scanner.scan_for_endpoints()
        self.assertTrue(len(valid_urls) > 0)

class SecurityTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()