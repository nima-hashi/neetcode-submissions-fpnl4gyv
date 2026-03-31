import heapq
from collections import defaultdict, deque

class Twitter:

    def __init__(self):
        self.timeStamp = 0
        self.userTweets = defaultdict(deque) # (timeStamp, tweetId)
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timeStamp += 1
        self.userTweets[userId].appendleft((self.timeStamp, tweetId))
        self.following[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []

        for followingId in self.following[userId]:
            tweets = list(self.userTweets[followingId])
            for tweet in tweets[:10]:
                heapq.heappush(min_heap, tweet)
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
        return [tweetId for _, tweetId in sorted(min_heap, reverse = True)]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
        
