
# Part-1(Intro and Basics) https://www.reddit.com/r/Python/

import praw

reddit = praw.Reddit(client_id='GcUAT3spNdPVIQ',
                     client_secret='VKDIgQQi7Xsv5SVGyLmo1F_Mwm-MSQ', password='Ronak@1208',
                     user_agent='PrawTut', username='Rishabh541')

subreddit = reddit.subreddit('python')
# hot is an upvotes over time algorithm
hot_python = subreddit.hot(limit=3)

# print(reddit.user.me()) CHECKING APP Authentication

# for submission in hot_python:
#     if not submission.stickied:
#         print(submission.title)

hot_python = subreddit.hot(limit=3)
for submission in hot_python:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title,
                                                                           submission.ups,
                                                                           submission.downs,
                                                                           submission.visited))

subreddit.subscribe()  # We might get banned for this as it is privilege info
