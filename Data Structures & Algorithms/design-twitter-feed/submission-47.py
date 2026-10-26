import bisect

class Twitter:

    def __init__(self):
        self.follows = defaultdict(dict)
        self.fans = defaultdict(dict)
        self.user_feed = defaultdict(deque)
        self.user_own = defaultdict(deque)
        self.ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        follows = self.follows
        fans = self.fans
        user_feed = self.user_feed 
        user_own = self.user_own
        self.ts += 1
        ts = self.ts

        follows[userId][userId] = 1
        fans[userId][userId] = 1

        user_own[userId].append((-ts,tweetId,userId))
        if len(user_own[userId]) > 10:
            user_own[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        user_own = self.user_own
        follows = self.follows
        pd = {}

        for u in follows[userId]:
            pd[u] = -1

        heaplist = []
        for u in pd:
            p = pd[u]
            if -p > len(user_own[u]):
                continue
            heapq.heappush(heaplist, user_own[u][p])
        
        feed = []
        while len(feed) < 10 and len(heaplist) > 0:
            most_recent = heapq.heappop(heaplist)
            feed.append(most_recent)

            
            uid = most_recent[2]
            pd[uid] -= 1
            
            if -pd[uid] <= len(user_own[uid]):
                heapq.heappush(heaplist, user_own[uid][pd[uid]])
        return [f[1] for f in feed]

    def follow(self, followerId: int, followeeId: int) -> None:
        follows = self.follows
        fans = self.fans
        follows[followerId][followeeId] = 1
        fans[followeeId][followerId] = 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follows = self.follows
        fans = self.fans
        follows[followerId].pop(followeeId, None)
        fans[followeeId].pop(followerId, None)
