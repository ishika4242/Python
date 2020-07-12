from instapy import InstaPy

'''Enter your username and password here'''
session == InstaPy(username="",password="")
session.login()

'''to like posts with hashtags nature,green,animal'''
session.like_by_tags["nature","green","animals"]

'''to make comments'''
session.set_do_comments(True,percentage=25)
sesssion.set.comments(["beautiful","lovit","awesome"])

session.end()
