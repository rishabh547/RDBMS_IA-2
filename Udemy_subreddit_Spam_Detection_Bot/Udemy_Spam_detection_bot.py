# Creating a chatbot to detect spam comments on Udemy Subreddit
import praw
# from praw_creds import client_id, client_secret, password, user_agent, username
import random
import time

common_spammy_words = ['udemy', 'course', 'save', 'coupon', 'free', 'discount']

reddit = praw.Reddit(client_id='GcUAT3spNdPVIQ',
                     client_secret='VKDIgQQi7Xsv5SVGyLmo1F_Mwm-MSQ', password='Ronak@1208',
                     user_agent='PrawTut', username='Rishabh541')


def find_spam_by_name(search_query):
    authors = []
    for submission in reddit.subreddit("all").search(search_query, sort="new", limit=11):
        print(submission.title, submission.author, submission.url)
        if submission.author not in authors:
            authors.append(submission.author)
    return authors


if __name__ == "__main__":
    while True:
        current_search_query = random.choice(["udemy"])
        spam_content = []
        trashy_users = {}
        smelly_authors = find_spam_by_name(current_search_query)
        for author in smelly_authors:
            user_trashy_urls = []
            sub_count = 0
            dirty_count = 0
            try:
                for sub in reddit.redditor(str(author)).submissions.new():
                    submit_links_to = sub.url
                    submit_id = sub.id
                    submit_subreddit = sub.subreddit
                    submit_title = sub.title
                    dirty = False
                    for w in common_spammy_words:
                        if w in submit_title.lower():
                            dirty = True
                            junk = [submit_id, submit_title]
                            if junk not in user_trashy_urls:
                                user_trashy_urls.append(
                                    [submit_id, submit_title, str(author)])

                    if dirty:
                        dirty_count += 1
                    sub_count += 1

                try:
                    trashy_score = dirty_count/sub_count
                except:
                    trashy_score = 0.0
                print("User {} trashy score is: {}".format(
                    str(author), round(trashy_score, 3)))

                if trashy_score >= 0.5:
                    trashy_users[str(author)] = [trashy_score, sub_count]

                    for trash in user_trashy_urls:
                        spam_content.append(trash)

            except Exception as e:
                print(str(e))

        for spam in spam_content:
            spam_id = spam[0]
            spam_user = spam[2]
            submission = reddit.submission(id=spam[0])
            created_time = submission.created_utc
            if time.time()-created_time <= 86400:
                link = "https://reddit.com"+submission.permalink

                message = """*Beep boop*

I am a bot that sniffs out spammers, and this smells like spam.

At least {}% out of the {} submissions from /u/{} appear to be for Udemy affiliate links. 

Don't let spam take over Reddit! Throw it out!

*Bee bop*""".format(round(trashy_users[spam_user][0]*100, 2), trashy_users[spam_user][1], spam_user)

                try:
                    with open("C:\Sem4_Studymaterials\RDBMS\posted_urls.txt", "r") as f:
                        already_posted = f.read().split('\n')
                    if link not in already_posted:
                        print(message)
                        submission.reply(message)
                        print(
                            "We've posted to {} and now we need to sleep for 12 minutes".format(link))
                        with open("C:\Sem4_Studymaterials\RDBMS\posted_urls.txt", "a") as f:
                            f.write(link+'\n')
                        time.sleep(12*60)
                        break
                except Exception as e:
                    print(str(e))
                    time.sleep(12*60)
