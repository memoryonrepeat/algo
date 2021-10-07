# https://leetcode.com/problems/tweet-counts-per-frequency/

from collections import defaultdict
from bisect import bisect_left, insort_left

class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        insort_left(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        
        freqMap = {
            "minute": 60,
            "hour": 60*60,
            "day": 60*60*24
        }
        
        tweetRecord = self.tweets[tweetName]
        
        chunksCount = (endTime - startTime)//freqMap[freq] + 1
        
        result = [0 for _ in range(chunksCount)]
        
        index = bisect_left(tweetRecord, startTime)
        
        while index < len(tweetRecord) and tweetRecord[index] <= endTime:
            currentTweetTime = tweetRecord[index]
            chunkIndex = (currentTweetTime - startTime)//freqMap[freq]
            result[chunkIndex] += 1
            index += 1
            
        return result
            
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)