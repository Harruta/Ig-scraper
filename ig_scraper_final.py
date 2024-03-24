import instaloader

bot = instaloader.Instaloader()

user = input("Enter the username: ")

profile = instaloader.Profile.from_username(bot.context, user)

posts = profile.get_posts()

count = 0

for post in posts :
    if post.is_video:
        print("Downloading video posts {count + 1}")
        bot.download_post(post, target=profile.username)
        count += 1
        if count == 10:
            break