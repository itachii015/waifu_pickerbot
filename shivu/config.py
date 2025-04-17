class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5559464565"
    sudo_users = "6312154011"
    GROUP_ID = -1002308742668
    Port = 8080
    TOKEN = "7762285113:AAF7fF1-c9CthCxFVmIDflsEV8WHtsqkVTg"
    mongo_url = "mongodb+srv://sanjii1505:HbyxK50HsVYKp9mJ@cluster0.qcdra.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Waifu_picker_chat"
    UPDATE_CHAT = "Waifu_picker_chat"
    BOT_USERNAME = "onee_piecebot"
    CHARA_CHANNEL_ID = "-1002599514806"
    api_id = 21283098
    api_hash = "a272cc3d3fc74a28df77951"
    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
