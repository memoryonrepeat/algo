# https://leetcode.com/problems/web-crawler/

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    
    host = None
    result = set()
    
    def getHostname(self, url):
        host = (url.split('//')[1]).split('/')[0]
        print(host, self.host)
        return host
    
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        if not self.host:
            self.host = self.getHostname(startUrl)
            
        if self.getHostname(startUrl) == self.host:
            self.result.add(startUrl)
        
        neighbors = htmlParser.getUrls(startUrl)
        
        for neighbor in neighbors:
            self.crawl(neighbor, htmlParser)
            
        return self.result