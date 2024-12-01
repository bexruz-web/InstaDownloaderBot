import json

# Utils
from utils import is_instagram_link
from downloader import video_downloader

# JSON data
with open("./static_texts.json", 'r', encoding='utf-8') as file:
    static_text = json.load(file)


def message_handler(update, context):
    message = update.message.text
    # Timer
    deleted_message = update.message.reply_text("⏳")

    check_link = is_instagram_link(message)
    print(check_link)
    if check_link:
        # Video downloading
        result = video_downloader(video_url=message)

        # Download logic
        if result['status'] is True:
            download_video = result['result'][0]['url']

            # Deleted Timer
            deleted_message.delete()

            # Send Video
            update.message.reply_video(video=download_video, caption=static_text['botMessage'], parse_mode='HTML')
        else:
            # Deleted Timer
            deleted_message.delete()

            # Show error
            update.message.reply_text(text=static_text['downloadError'], parse_mode='HTML')

    elif 'Yaratuvchi' in message:
        update.message.reply_text(text=static_text['buttonMessage'], parse_mode='HTML')

    else:
        # Deleted Timer
        deleted_message.delete()

        # Show error
        update.message.reply_text(text=static_text['errorLink'], parse_mode='HTML')



