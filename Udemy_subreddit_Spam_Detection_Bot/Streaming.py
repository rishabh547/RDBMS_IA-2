# Part-3(Streaming from Reddit)
import praw

reddit = praw.Reddit(client_id='GcUAT3spNdPVIQ',
                     client_secret='VKDIgQQi7Xsv5SVGyLmo1F_Mwm-MSQ', password='Ronak@1208',
                     user_agent='PrawTut', username='Rishabh541')
subreddit = reddit.subreddit('python')

subreddit = reddit.subreddit('news')

for comment in subreddit.stream.comments():
    try:
        print(30*'_')
        print()
        parent_id = str(comment.parent())
        submission = reddit.comment(parent_id)
        print('Parent:')
        print(submission.body)
        print('Reply')
        print(comment.body)
    except praw.exceptions.PRAWException as e:
        pass
