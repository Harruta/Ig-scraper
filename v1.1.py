import os
import instaloader
from instaloader import Profile

def download_posts(user, max_videos=10):
    # Initialize the Instaloader instance
    bot = instaloader.Instaloader()

    # Fetch the user's profile
    profile = Profile.from_username(bot.context, user)

    # Get the profile's posts
    posts = profile.get_posts()

    # Initialize the counter for the number of videos downloaded
    count = 0

    # Download up to max_videos video posts
    for post in posts:
        if post.is_video:
            # Check if the limit has been reached
            if count == max_videos:
                break

            # Download the video post and update the count
            print(f"Downloading video post {count + 1} for {user}...")
            bot.download_post(post, target=profile.username)
            count += 1

    # Print the final message
    print(f"Downloaded {count} video posts for {user}.")

    # Close the Instaloader session
    bot.close()

# Request the list of Instagram usernames
print("Enter the Instagram usernames separated by a space:")
usernames = input("").split()

# Set the max number of videos to download
max_videos = 10

# Iterate through the usernames and download videos
for user in usernames:
    print(f"\nDownloading posts for {user}...")
    download_posts(user, max_videos)