import bisect

class Twitter:

    def __init__(self):
        self.follows = defaultdict(dict)
        self.user_own = defaultdict(deque)
        self.ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        follows = self.follows
        user_own = self.user_own
        self.ts += 1
        ts = self.ts

        follows[userId][userId] = 1

        user_own[userId].append((-ts,tweetId,userId))
        if len(user_own[userId]) > 10:
            user_own[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        user_own = self.user_own
        follows = self.follows
        pd = {}
        most_recent_per_user = []
        
        for u in follows[userId]:
            if user_own[u]:
                pd[u] = -1
                most_recent_per_user.append(user_own[u][-1])
        heapq.heapify(most_recent_per_user)
        
        feed = []
        while len(feed) < 10 and len(most_recent_per_user) > 0:
            most_recent = heapq.heappop(most_recent_per_user)
            feed.append(most_recent)
            u = most_recent[2]
            pd[u] -= 1
            if -pd[u] > len(user_own[u]): 
                continue
            heapq.heappush(most_recent_per_user, user_own[u][pd[u]])
        return [f[1] for f in feed]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId][followeeId] = 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.follows[followerId].pop(followeeId, None)
