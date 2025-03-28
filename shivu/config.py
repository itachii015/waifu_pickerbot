class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7776071513"
    sudo_users = "6312154011", "1350736363"
    GROUP_ID = -1002374696109
    TOKEN = "8058000288:AAE_jFBEH6l_LuabvVJJ9WwVzShHxNxbvGw"
    mongo_url = "mongodb+srv://itachii130506:idjVit5zIoSOL3Gv@cluster0.vmsab.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1002374696109"
    api_id = 28682516
    api_hash = "bb43fa00569d8f4de75aad6bdeb3650d"
    Port = 8080
    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
