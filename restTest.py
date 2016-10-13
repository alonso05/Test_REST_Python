import unittest
import json
import urllib.request

class RestApiTest(unittest.TestCase):
  def setUp(self):
    #define Api URL and API Key
    self.ApiUrl = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    self.ApiKey="da0e0094c0ab4e9291c75b559c24355c"
  
  def test_basic_search(self):
    #define what to search: halloween
    mySearch = 'halloween'
    #define api request
    testurl=(self.ApiUrl+"?api-key="+self.ApiKey+"&"+"q="+mySearch)
    print(testurl)
    request=urllib.request.urlopen(testurl)
    #read response
    response=request.read()
    #convert response from bytes to string
    strResponse = response.decode("utf-8")
    print(strResponse)
    #assert response
    self.assertTrue("halloween" in strResponse)

  def test_reading_json_status(self):
    #define what to search: halloween
    mySearch = 'halloween'
    #define api request
    testurl=(self.ApiUrl+"?api-key="+self.ApiKey+"&"+"q="+mySearch)
    print(testurl)
    request=urllib.request.urlopen(testurl)
    #read response
    response=request.read()
    #convert response from bytes to string
    strResponse = response.decode("utf-8")
    print(strResponse)
    #loads response as json
    json_data=json.loads(strResponse)
    #get the key "status" value
    status=json_data["status"]
    print("Status Response:"+status)
    #assert response status
    self.assertTrue(status=="OK")

  def tearDown(self):
    print("------- test is over -------")

if __name__ == "__main__":
  unittest.main()