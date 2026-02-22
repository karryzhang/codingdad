#!/usr/bin/env python3
"""Add internet/texting abbreviations to daily-words-1000.json."""
import json, pathlib

DATA = pathlib.Path(__file__).parent.parent / 'game' / 'daily-words-1000.json'

ABBREVS = [
    # ── Slack / 职场消息 ──────────────────────────────────────────────────
    {
        "word": "ASAP",
        "zh": "【网络缩写】as soon as possible / 尽快",
        "pos": "abbr.",
        "ex": "Can you send me the updated file ASAP? We need it before the meeting."
    },
    {
        "word": "FYI",
        "zh": "【网络缩写】for your information / 供参考，仅供知悉",
        "pos": "abbr.",
        "ex": "FYI, the meeting has been moved to Thursday at 3 PM."
    },
    {
        "word": "BTW",
        "zh": "【网络缩写】by the way / 顺便说一句",
        "pos": "abbr.",
        "ex": "BTW, did you see the new design mockups the team shared?"
    },
    {
        "word": "LMK",
        "zh": "【网络缩写】let me know / 告诉我，有消息通知我",
        "pos": "abbr.",
        "ex": "LMK if you need any help with the report and I'll jump in."
    },
    {
        "word": "ETA",
        "zh": "【网络缩写】estimated time of arrival / 预计到达（完成）时间",
        "pos": "abbr.",
        "ex": "What's the ETA on the new feature? The client is asking."
    },
    {
        "word": "TBD",
        "zh": "【网络缩写】to be determined / 待定",
        "pos": "abbr.",
        "ex": "The exact budget is still TBD — we'll confirm after next week's call."
    },
    {
        "word": "TBC",
        "zh": "【网络缩写】to be confirmed / 待确认",
        "pos": "abbr.",
        "ex": "Venue and time are TBC, but mark Thursday afternoon in your calendar."
    },
    {
        "word": "WIP",
        "zh": "【网络缩写】work in progress / 进行中，未完成",
        "pos": "abbr.",
        "ex": "Heads up — that doc is still WIP, so don't share it externally yet."
    },
    {
        "word": "OOO",
        "zh": "【网络缩写】out of office / 不在办公室，外出",
        "pos": "abbr.",
        "ex": "I'll be OOO from Monday to Wednesday. Ping Sarah if it's urgent."
    },
    {
        "word": "WFH",
        "zh": "【网络缩写】work from home / 居家办公",
        "pos": "abbr.",
        "ex": "I'm WFH today but available on Slack — just ping me anytime."
    },
    {
        "word": "EOD",
        "zh": "【网络缩写】end of day / 今日下班前，今日截止",
        "pos": "abbr.",
        "ex": "Can you get me your feedback on the proposal by EOD? Thanks."
    },
    {
        "word": "ICYMI",
        "zh": "【网络缩写】in case you missed it / 万一你没看到，防止你错过",
        "pos": "abbr.",
        "ex": "ICYMI — we posted the new onboarding guide in the #resources channel."
    },
    {
        "word": "TLDR",
        "zh": "【网络缩写】too long; didn't read / 太长没看，简而言之",
        "pos": "abbr.",
        "ex": "TLDR: the project is on track, but we need two more weeks for testing."
    },
    {
        "word": "DM",
        "zh": "【网络缩写】direct message / 私信",
        "pos": "abbr.",
        "ex": "Feel free to DM me if you have questions — happy to help."
    },
    {
        "word": "AFAIK",
        "zh": "【网络缩写】as far as I know / 据我所知",
        "pos": "abbr.",
        "ex": "AFAIK the deadline hasn't changed, but double-check with the PM."
    },
    {
        "word": "FWIW",
        "zh": "【网络缩写】for what it's worth / 仅供参考，不一定有用但说一下",
        "pos": "abbr.",
        "ex": "FWIW, I think the simpler layout tested much better with users."
    },
    # ── 通用聊天 / 表情达意 ───────────────────────────────────────────────
    {
        "word": "LOL",
        "zh": "【网络缩写】laughing out loud / 哈哈，好笑",
        "pos": "abbr.",
        "ex": "He sent a meme in the middle of the all-hands meeting — LOL 😂"
    },
    {
        "word": "LMAO",
        "zh": "【网络缩写】laughing my ass off / 笑死我了（比 LOL 更夸张）",
        "pos": "abbr.",
        "ex": "LMAO he introduced himself to the CEO twice in the same day."
    },
    {
        "word": "ROFL",
        "zh": "【网络缩写】rolling on the floor laughing / 笑到打滚（极度好笑）",
        "pos": "abbr.",
        "ex": "Did you see that autocorrect fail? ROFL I can't stop laughing."
    },
    {
        "word": "OMG",
        "zh": "【网络缩写】oh my god / 天哪，我的天",
        "pos": "abbr.",
        "ex": "OMG they just announced a surprise day off tomorrow!"
    },
    {
        "word": "IDK",
        "zh": "【网络缩写】I don't know / 我不知道，不确定",
        "pos": "abbr.",
        "ex": "IDK, maybe we should just go with plan B and see how it goes?"
    },
    {
        "word": "IMO",
        "zh": "【网络缩写】in my opinion / 依我看，我个人觉得",
        "pos": "abbr.",
        "ex": "IMO the second design is way cleaner — less clutter, easier to read."
    },
    {
        "word": "IMHO",
        "zh": "【网络缩写】in my humble opinion / 依我拙见（比 IMO 更客气）",
        "pos": "abbr.",
        "ex": "IMHO, we should run a small test before doing a full rollout."
    },
    {
        "word": "TBH",
        "zh": "【网络缩写】to be honest / 老实说，说实话",
        "pos": "abbr.",
        "ex": "TBH I wasn't sure about the idea at first, but it's growing on me."
    },
    {
        "word": "NGL",
        "zh": "【网络缩写】not gonna lie / 不骗你，说真的",
        "pos": "abbr.",
        "ex": "NGL, that was one of the best presentations I've seen from the team."
    },
    {
        "word": "SMH",
        "zh": "【网络缩写】shaking my head / 无语，摇头叹气",
        "pos": "abbr.",
        "ex": "He hit reply-all and sent his lunch order to 300 people... SMH."
    },
    # ── 状态 / 在线离开 ────────────────────────────────────────────────────
    {
        "word": "BRB",
        "zh": "【网络缩写】be right back / 马上回来，等一下",
        "pos": "abbr.",
        "ex": "BRB — grabbing a coffee, back in five ☕"
    },
    {
        "word": "GTG",
        "zh": "【网络缩写】got to go / 我得走了，先下了",
        "pos": "abbr.",
        "ex": "GTG, my next call is starting. Catch you after lunch!"
    },
    {
        "word": "AFK",
        "zh": "【网络缩写】away from keyboard / 暂时离开，不在电脑旁",
        "pos": "abbr.",
        "ex": "Going AFK for lunch — back around 1:30. Leave me a message!"
    },
    {
        "word": "NVM",
        "zh": "【网络缩写】never mind / 算了，没事了",
        "pos": "abbr.",
        "ex": "NVM — I found the file myself, no need to send it now."
    },
    # ── 生活 / 社交 ───────────────────────────────────────────────────────
    {
        "word": "IRL",
        "zh": "【网络缩写】in real life / 现实中，线下",
        "pos": "abbr.",
        "ex": "We've been on the same team for a year but never met IRL!"
    },
    {
        "word": "FOMO",
        "zh": "【网络缩写】fear of missing out / 害怕错过，错过恐惧症",
        "pos": "abbr.",
        "ex": "Seeing everyone's photos from the trip gave me serious FOMO."
    },
    {
        "word": "HMU",
        "zh": "【网络缩写】hit me up / 联系我，找我",
        "pos": "abbr.",
        "ex": "If you're ever in Shanghai, HMU and we can grab dinner!"
    },
    {
        "word": "TMI",
        "zh": "【网络缩写】too much information / 信息量太大，说太多细节了",
        "pos": "abbr.",
        "ex": "He described his dentist appointment in extreme detail — TMI, dude 😂"
    },
    # ── 流行网络用语 ──────────────────────────────────────────────────────
    {
        "word": "GOAT",
        "zh": "【网络缩写】greatest of all time / 史上最强，封神级别",
        "pos": "abbr.",
        "ex": "Serena Williams is the GOAT — no one else comes close."
    },
    {
        "word": "GG",
        "zh": "【网络缩写】good game / 好局；也用来表示认输或结束",
        "pos": "abbr.",
        "ex": "GG everyone — tough match but we played well. Let's review tomorrow."
    },
    {
        "word": "FR",
        "zh": "【网络缩写】for real / 真的吗，认真的（表示强调或惊讶）",
        "pos": "abbr.",
        "ex": "Wait, they cancelled the whole event? FR?? 😱"
    },
    {
        "word": "IYKYK",
        "zh": "【网络缩写】if you know, you know / 懂的都懂",
        "pos": "abbr.",
        "ex": "That little noodle shop on the side street — IYKYK 🍜"
    },
]

# ── Process ───────────────────────────────────────────────────────────────────
d = json.load(open(DATA))
existing_lower = {x['word'].lower() for x in d}

to_add = []
skipped = []
for e in ABBREVS:
    if e['word'].lower() in existing_lower:
        skipped.append(e['word'])
    else:
        e.setdefault('ipa', '')
        to_add.append(e)

d.extend(to_add)

print(f"Before : {len(existing_lower)}")
print(f"Added  : {len(to_add)}")
if skipped:
    print(f"Skipped: {skipped}")
print(f"After  : {len(d)}")

with open(DATA, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print("Done.")
