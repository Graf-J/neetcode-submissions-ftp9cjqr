class Twitter:
    def __init__(self):
        self.ctr = 1
        self.user_posts = defaultdict(list)
        self.user_subscriptions = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_posts[userId].append((self.ctr, tweetId))
        self.ctr += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for uid in self.user_subscriptions[userId] | {userId}:
            if len(self.user_posts[uid]) > 0:
                ctr, tweet_id = self.user_posts[uid][-1]
                heapq.heappush_max(heap, (ctr, tweet_id, uid, len(self.user_posts[uid]) - 1))

        feed = []
        while len(feed) < 10 and heap:
            _, tweet_id, uid, i = heapq.heappop_max(heap)
            feed.append(tweet_id)
            if i > 0:
                ctr, tweet_id = self.user_posts[uid][i - 1]
                heapq.heappush_max(heap, (ctr, tweet_id, uid, i - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_subscriptions[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_subscriptions[followerId].discard(followeeId)



