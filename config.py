# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

# One == Physics Wallah (PW)
# Two == ClassPlus (CP)
# Three == Appx

import os

def clean_env(key: str, default: str = "") -> str:
    val = os.environ.get(key, default)
    if val is None:
        return default
    return str(val).strip().strip('"\'')

api_id_raw = clean_env("API_ID", "34239723")
api_hash = clean_env("API_HASH", "966261d7f23f48f7765f2b2a0f7ee548")
bot_token = clean_env("BOT_TOKEN", "9053502415:AAGtW2zcBh51bsQvsswfsP570fA30OHKsqk")

try:
    api_id = int(api_id_raw)
except ValueError:
    raise ValueError(f"Invalid API_ID: '{api_id_raw}'. It must be an integer.")

auth_users_raw = clean_env("AUTH_USERS", "8844885567")
auth_users = [
    int(x.strip()) 
    for x in auth_users_raw.replace(";", ",").replace(" ", ",").split(",") 
    if x.strip().isdigit()
]

if not api_id: raise ValueError("Set API_ID env var!")
if not api_hash: raise ValueError("Set API_HASH env var!")
if not bot_token: raise ValueError("Set BOT_TOKEN env var!")
if not auth_users: raise ValueError("Set AUTH_USERS env var!")

# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
