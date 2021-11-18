class Translation(object):
    START_TEXT = """Hi {},
I'm TN57 URL Uploader!
You can upload HTTP/HTTPS direct link, Using this bot!

/help for more details!"""
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    DOWNLOAD_START = "📥Downloading..."
    UPLOAD_START = "📤Uploading..."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks for using @TN57_Url_Upload_BOT\n\n<b>Join : @TN57_BotZ</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds.\n\n@TN57_BotZ"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    HELP_USER = """How to Use Me? Follow These steps!
    
1. Send url (example.domain/File.mp4 | New Filename.mp4).
2. Send Image As Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File (video) as file with Screenshots
   Video  - Give File as video without Screenshots
   File   - Give File without Screenshots

If bot didn't respond, contact @TN57_BotzSupport"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
   ABOUT_ME ="""
<b>My Name :</b> <a href='https://telegram.me/TN57_Url_Upload_BOT'>TN57 Url Uploader Bot</a>\n
<b>My Update Channel :</b> <a href='https://t.me/TN57_BotZ'>TN57 BotZ</a>\n
<b>Version :</b> <a href='https://telegram.me/TN57_Url_Upload_BOT'>0.9.2 beta</a>\n
<b>Leech & Mirror Zone:</b> <a href='https://t.me/TN57_LEECH_AND_MIRROR_ZONE/2'>Click Here</a>\n
<b>Server :</b> <a href='https://heroku.com'>Heroku</a>\n
<b>Library :</b> <a href='https://github.com/pyrogram'>Pyrogram 1.4.3</a>\n
<b>Language :</b> <a href='https://www.python.org'>Python 3.9.4</a>\n
<b>More BotZ :</b> <a href='https://t.me/TN57_BotZ/14'>Click Here</a>\n
<b>Support Group :</b> <a href='https://t.me/TN57_BotzSupport'>Click Here</a>\n"""
