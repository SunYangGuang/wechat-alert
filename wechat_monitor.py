"""
微信群关键词监控
自动检测微信目录，自动提取key，自动匹配群名
"""
import time, sys, os, winsound, ctypes
from wechatauto.db import WeChatDB

# === 配置（可改）===
# KEYWORD = "下午7点"
KEYWORD = "车找人"
INTERVAL = 3
TARGET_GROUP_NAMES = [
    "香河东通勤拼车2群",
    "大爱社区业主群1",
    "大爱&绿地拼车群",
]

def alert(group_name, content):
    print(f"\n{'='*50}", flush=True)
    print(f"  [提醒] {group_name}", flush=True)
    print(f"  {content[:200]}", flush=True)
    print(f"{'='*50}\n", flush=True)
    for _ in range(3):
        winsound.Beep(1200, 400)
        time.sleep(0.15)
    ctypes.windll.user32.MessageBoxW(0, content[:300], f"微信提醒: {group_name}", 0x40 | 0x1000)

print("初始化数据库...", flush=True)
db = WeChatDB()
me = db.get_self_info()
print(f"已登录: {me.get('nick_name','?')}", flush=True)

# 自动匹配群名
TARGET_GROUPS = {}
for name in TARGET_GROUP_NAMES:
    results = db.search_contact(name)
    if results:
        gid = results[0]["username"]
        TARGET_GROUPS[gid] = name
        print(f"  已匹配: {name}", flush=True)
    else:
        print(f"  [警告] 未找到群: {name}", flush=True)

if not TARGET_GROUPS:
    print("错误: 没有匹配到任何群，退出", flush=True)
    input("按回车退出...")
    sys.exit(1)

# 记录每个群最后消息seq
last_seq = {}
for gid in TARGET_GROUPS:
    msgs = db.get_messages(gid, limit=1)
    last_seq[gid] = msgs[0].get("sort_seq", 0) if msgs else 0

print(f"\n监控运行中... 关键词: {KEYWORD}", flush=True)

while True:
    for gid, gname in TARGET_GROUPS.items():
        try:
            new_msgs = db.get_new_messages(gid, last_seq[gid])
            for m in new_msgs:
                content = str(m.get("content", ""))
                if KEYWORD in content:
                    alert(gname, content)
                last_seq[gid] = max(last_seq[gid], m.get("sort_seq", 0))
        except Exception as e:
            print(f"  [ERR] {gname}: {e}", flush=True)
    time.sleep(INTERVAL)
