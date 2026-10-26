import bisect

class Twitter:

    def __init__(self):
        self.follows = defaultdict(dict)
        self.fans = defaultdict(dict)
        self.user_feed = defaultdict(deque)
        self.user_own = defaultdict(deque)
        self.t2u = {}
        self.ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        follows = self.follows
        fans = self.fans
        user_feed = self.user_feed 
        user_own = self.user_own
        t2u = self.t2u 
        self.ts += 1
        ts = self.ts

        follows[userId][userId] = 1
        fans[userId][userId] = 1

        t2u[tweetId] = userId
        user_own[userId].append((ts,tweetId))
        if len(user_own[userId]) > 10:
            user_own[userId].popleft()

        fans_userIds = fans[userId].keys()
        for uid in fans_userIds:
            user_feed[uid].append((ts,tweetId))
            if len(user_feed[uid]) > 10:
                user_feed[uid].popleft()
        

    def getNewsFeed(self, userId: int) -> List[int]:
        return list(reversed([tw[1] for tw in self.user_feed[userId]]))

    def follow(self, followerId: int, followeeId: int) -> None:
        print("flollow")
        follows = self.follows
        fans = self.fans
        user_feed = self.user_feed 
        user_own = self.user_own
        t2u = self.t2u 

        follows[followerId][followeeId] = 1
        fans[followeeId][followerId] = 1
        
        if not user_own[followeeId]:
            return
        
        my_user_feed = user_feed[followerId]
        print(f"my_user_feed:{my_user_feed} user_own[followeeId]:{user_own[followeeId]}")
        if not my_user_feed:
            for tw in user_own[followeeId]:
                my_user_feed.append(tw)
            return 

        for tw in reversed(user_own[followeeId]):
            if tw[0] > my_user_feed[0][0] or len(my_user_feed) < 10:
                if tw not in my_user_feed:
                    bisect.insort(my_user_feed, tw)
                    print(f"after insort my_user_feed:{my_user_feed} ")
                    if len(my_user_feed) > 10:
                        my_user_feed.popleft()
            else: break

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follows = self.follows
        fans = self.fans
        user_feed = self.user_feed 
        user_own = self.user_own
        t2u = self.t2u 

        follows[followerId].pop(followeeId, None)
        fans[followeeId].pop(followerId, None)

        my_user_feed = user_feed[followerId]
        remove_cnt = 0 
        need_remove = []
        for tw in my_user_feed:
            if t2u[tw[1]] == followeeId:
                need_remove.append(tw)
                remove_cnt += 1
        if remove_cnt == 0: 
            return 

        for tw in need_remove:
            my_user_feed.remove(tw)

        backup = []
        for follow in follows[followerId]:
            cnt = 0
            for tw in reversed(user_own[follow]):
                tw = (-tw[0], tw[1])
                backup.append(tw)
                cnt += 1
                if cnt == 10: break
        heapq.heapify(backup)

        while remove_cnt > 0 and backup:
            tw = heapq.heappop(backup)
            tw = (-tw[0], tw[1])
            if tw not in my_user_feed:
                bisect.insort(my_user_feed, tw)