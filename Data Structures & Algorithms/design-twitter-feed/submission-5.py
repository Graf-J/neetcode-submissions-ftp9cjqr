class Twitter:
    def __init__(self):
        self.ctr = 1
        self.user_tweets = defaultdict(deque)
        self.user_subscriptions = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.ctr, tweetId))
        if len(self.user_tweets) > 10:
            self.user_tweets[userId].popleft()
        self.ctr += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for uid in self.user_subscriptions[userId] | {userId}:
            if len(self.user_tweets[uid]) > 0:
                i = len(self.user_tweets[uid]) - 1
                ctr, tweet_id = self.user_tweets[uid][i]
                heap.append((ctr, tweet_id, uid, i))
        heapq.heapify_max(heap)

        feed = []
        while len(feed) < 10 and heap:
            _, tweet_id, uid, i = heapq.heappop_max(heap)
            feed.append(tweet_id)
            if i > 0:
                new_ctr, new_tweet_id = self.user_tweets[uid][i - 1]
                heapq.heappush_max(heap, (new_ctr, new_tweet_id, uid, i - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_subscriptions[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_subscriptions[followerId].discard(followeeId)
        
