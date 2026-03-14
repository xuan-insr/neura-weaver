import pytz
import msal
import requests
from datetime import datetime, timedelta
from loguru import logger
import os

CLIENT_ID = "6fa867eb-3f42-44c3-b6f9-8291b5dce45a"
TENANT_ID = "consumers"   # 注意！个人账户固定写 "consumers"
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["Calendars.Read"]

CALENDAR_NAME = "TimeLog"
CACHE_FILE = "token_cache.json"

# ==== Token 缓存逻辑 ====
cache = msal.SerializableTokenCache()
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        cache.deserialize(f.read())

app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY, token_cache=cache)

# 优先 silent 登录
accounts = app.get_accounts()
if accounts:
    result = app.acquire_token_silent(SCOPES, account=accounts[0])
else:
    result = None

# 如果缓存失效，则交互式登录
if not result:
    result = app.acquire_token_interactive(SCOPES)

# 保存缓存
with open(CACHE_FILE, "w") as f:
    f.write(cache.serialize())

if "access_token" not in result:
    raise RuntimeError("获取 token 失败")

token = result["access_token"]

# ==== 获取 TimeLog 日历 ====
r = requests.get("https://graph.microsoft.com/v1.0/me/calendars",
                 headers={"Authorization": f"Bearer {token}"})
cals = r.json()["value"]
time_log_id = [c["id"] for c in cals if c["name"] == CALENDAR_NAME][0]

# ==== 本周区间 ====
shanghai_tz = pytz.timezone('Asia/Shanghai')
today = datetime.now(shanghai_tz).date()
# start = today - timedelta(days=today.weekday())   # 周一
# end = start + timedelta(days=7)                   # 下周一
start = shanghai_tz.localize(datetime(2025, 8, 23)).date()
end = today + timedelta(days=1)

logger.info(f"本周区间：{start} ~ {end}")

url = (f"https://graph.microsoft.com/v1.0/me/calendars/{time_log_id}/calendarView"
       f"?startDateTime={start.isoformat()}&endDateTime={end.isoformat()}")

events = []
while url:
    r = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    data = r.json()
    this_events = data.get("value", [])
    for event in this_events:
        start_time = datetime.fromisoformat(event['start']['dateTime']).replace(tzinfo=pytz.UTC).astimezone(shanghai_tz)
        end_time = datetime.fromisoformat(event['end']['dateTime']).replace(tzinfo=pytz.UTC).astimezone(shanghai_tz)
        subject = event['subject']
        events.append((start_time, end_time, subject))
        url = data.get("@odata.nextLink")  # 处理分页

events.sort(key=lambda x: x[0])

def start_end_time_to_str(start_time: datetime, end_time: datetime) -> str:
    """
    Returns like "10:00 ~ 11:00" or "23:00 ~ 01:00/+1" if end_time is the next day
    """
    if start_time.day == end_time.day:
        return f"{start_time.strftime('%H:%M')} ~ {end_time.strftime('%H:%M')}"
    else:
        return f"{start_time.strftime('%H:%M')} ~ {end_time.strftime('%H:%M')}/+{(end_time.day - start_time.day)}"

last_start_time_day = None
for e in events:
    start_time, end_time, subject = e
    if start_time.day != last_start_time_day:
        print(f"- {start_time.strftime('%Y-%m-%d')} ({start_time.strftime('%a')})")
    last_start_time_day = start_time.day
    print(f"    - {start_end_time_to_str(start_time, end_time)}: {subject}")

