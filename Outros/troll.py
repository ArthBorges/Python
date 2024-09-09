def main():
    import webbrowser
    import time
    import random

    website = random.choice([
        "youtube.com",
        "facebook.com",
        "twitter.com",
        "instagram.com",
        "twitch.com",
        "whatsapp.com",
    ])
    formatted = "https://www." + website
    while 1:
        webbrowser.open(formatted)
        time.sleep(1)

if __name__ == "__main__":
    #main()