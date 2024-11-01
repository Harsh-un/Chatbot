from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "26516344"
# -------------------------------------------------------------
API_HASH = "7a3f7d55d89476a15a62b4dd39062556"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = getenv("OWNER_ID", "6253265083")
SUPPORT_GRP = "unb_support"
UPDATE_CHNL = "unb_info"
OWNER_USERNAME = "harsh_un"

