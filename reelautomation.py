import os
import csv
import random
from datetime import datetime

# Simple caption + hashtag pools
CAPTIONS = [
    "Turning ideas into reality 🚀",
    "Just another step forward 💻",
    "Built with curiosity and code ⚙️",
    "Small project, big learning 🌱",
    "Creating something out of nothing ✨"
]

HASHTAGS = [
    "#coding", "#programming", "#developer", "#tech",
    "#automation", "#python", "#buildinpublic",
    "#engineering", "#learning", "#techlife"
]


def generate_caption():
    caption = random.choice(CAPTIONS)
    tags = random.sample(HASHTAGS, 5)
    return caption, " ".join(tags)


def scan_videos(folder):
    videos = []
    for file in os.listdir(folder):
        if file.endswith((".mp4", ".mov", ".mkv")):
            videos.append(file)
    return videos


def create_log(video_name, caption, hashtags, log_file="reel_log.csv"):
    file_exists = os.path.isfile(log_file)

    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "video", "caption", "hashtags"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            video_name,
            caption,
            hashtags
        ])


def run(folder):
    videos = scan_videos(folder)

    if not videos:
        print("No videos found.")
        return

    print("\n🎬 REEL AUTOMATION SYSTEM\n")

    for video in videos:
        caption, hashtags = generate_caption()

        print(f"📹 Video: {video}")
        print(f"📝 Caption: {caption}")
        print(f"🏷️ Hashtags: {hashtags}\n")

        create_log(video, caption, hashtags)

    print("✅ Done. Log saved to reel_log.csv")


if __name__ == "__main__":
    path = input("Enter folder path with reels: ")
    run(path)
