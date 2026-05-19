class Twitter:
    max_feed_len = 10

    def __init__(self):
        self.i = 0
        self.user_follows = defaultdict(set)
        self.user_posts = defaultdict(deque)

    def postTweet(self, userId: int, tweetId: int) -> None:
        posts = self.user_posts[userId]
        posts.append((self.i, tweetId))
        if len(posts) > self.max_feed_len:
            posts.popleft()
        self.i += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Build initial Heap
        heap = []
        for followed_user in self.user_follows[userId] | {userId}:
            followed_user_posts = self.user_posts[followed_user]
            if len(followed_user_posts) > 0:
                heapq.heappush_max(heap, (
                    followed_user_posts[-1][0], # Timestamp
                    followed_user_posts[-1][1], # TweetId
                    followed_user, # UserId
                    len(followed_user_posts) - 1 # UserPostIndex
                ))

        # Find 10 latest Tweets
        feed = []
        while heap and len(feed) < self.max_feed_len:
            _, tweet_id, user_id, user_post_idx = heapq.heappop_max(heap)
            feed.append(tweet_id)
            if user_post_idx > 0:
                post_ts, post_id = self.user_posts[user_id][user_post_idx - 1]
                heapq.heappush_max(heap, (
                    post_ts, # Timestamp
                    post_id, # TweetId
                    user_id, # UserId
                    user_post_idx - 1 # UserPostIndex
                ))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].discard(followeeId)
