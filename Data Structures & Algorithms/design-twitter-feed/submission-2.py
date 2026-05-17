from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.relationship = defaultdict(set)
        self.usertweet = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.usertweet[userId].add((-self.time,tweetId))
        self.time +=1

    def getNewsFeed(self, userId: int) -> List[int]:
        following=self.relationship[userId]
        following.add(userId)
        heap = []
        for f in following:
            tweets = self.usertweet[f]
            for tweet in tweets:
                heap.append(tweet)
        heapq.heapify(heap)
        res = []
        while len(res)<10 and heap:
            _,tweetId = heapq.heappop(heap)
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.relationship[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.relationship[followerId]:
            self.relationship[followerId].remove(followeeId)
