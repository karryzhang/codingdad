#!/usr/bin/env python3
"""Add ~100 native-speaker high-frequency phrases to daily-words-1000.json."""
import json, pathlib

DATA = pathlib.Path(__file__).parent.parent / 'game' / 'daily-words-1000.json'

PHRASES = [
    # ── 日常反应 / 语气词（地道口语）─────────────────────────────────────
    {"word": "fair enough",          "zh": "说得过去 / 行吧",              "pos": "expr", "scene": "daily"},
    {"word": "totally",              "zh": "完全正确 / 太对了",            "pos": "adv",  "scene": "daily"},
    {"word": "absolutely",           "zh": "当然 / 绝对是",                "pos": "adv",  "scene": "daily"},
    {"word": "for sure",             "zh": "当然 / 肯定的",                "pos": "expr", "scene": "daily"},
    {"word": "no kidding",           "zh": "不是开玩笑吧 / 真的假的",      "pos": "expr", "scene": "daily"},
    {"word": "seriously?",           "zh": "认真的吗？/ 真的？",           "pos": "expr", "scene": "daily"},
    {"word": "no way",               "zh": "不可能 / 绝对不行",            "pos": "expr", "scene": "daily"},
    {"word": "come on",              "zh": "得了吧 / 快点 / 拜托",         "pos": "expr", "scene": "daily"},
    {"word": "give me a break",      "zh": "饶了我吧 / 得了吧",            "pos": "expr", "scene": "daily"},
    {"word": "tell me about it",     "zh": "可不是嘛 / 我深有同感",        "pos": "expr", "scene": "daily"},
    {"word": "same here",            "zh": "我也是 / 同感",                "pos": "expr", "scene": "daily"},
    {"word": "I hear you",           "zh": "我理解你 / 我明白你的意思",    "pos": "expr", "scene": "daily"},
    {"word": "you're telling me",    "zh": "可不是嘛 / 你说的太对了",      "pos": "expr", "scene": "daily"},
    {"word": "oh my goodness",       "zh": "天哪 / 我的天",                "pos": "expr", "scene": "daily"},

    # ── 赞同 / 确认 ───────────────────────────────────────────────────────
    {"word": "sounds good",          "zh": "听起来不错 / 好的",            "pos": "expr", "scene": "daily"},
    {"word": "sounds like a plan",   "zh": "听起来是个好主意 / 就这么定了","pos": "expr", "scene": "daily"},
    {"word": "works for me",         "zh": "我没问题 / 可以",              "pos": "expr", "scene": "daily"},
    {"word": "I'm down",             "zh": "我愿意 / 我参加",              "pos": "expr", "scene": "daily"},
    {"word": "I'm in",               "zh": "算我一个 / 我参与",            "pos": "expr", "scene": "daily"},
    {"word": "count me in",          "zh": "把我算进去 / 我要参加",        "pos": "expr", "scene": "daily"},
    {"word": "I'm on it",            "zh": "我来处理 / 我去办",            "pos": "expr", "scene": "daily"},
    {"word": "got it",               "zh": "明白了 / 好的",                "pos": "expr", "scene": "daily"},
    {"word": "will do",              "zh": "好的，我会的 / 没问题",        "pos": "expr", "scene": "daily"},
    {"word": "noted",                "zh": "已记下 / 收到",                "pos": "expr", "scene": "work"},

    # ── 委婉表达异议 ──────────────────────────────────────────────────────
    {"word": "I'm not so sure",      "zh": "我不太确定 / 我有点怀疑",      "pos": "expr", "scene": "daily"},
    {"word": "that said",            "zh": "话虽如此 / 尽管如此",          "pos": "expr", "scene": "daily"},
    {"word": "with all due respect", "zh": "冒昧说一句 / 恕我直言",        "pos": "expr", "scene": "daily"},
    {"word": "if you ask me",        "zh": "依我看 / 我觉得",              "pos": "expr", "scene": "daily"},
    {"word": "I see your point",     "zh": "我理解你的意思",               "pos": "expr", "scene": "daily"},

    # ── 请求澄清 ──────────────────────────────────────────────────────────
    {"word": "can you elaborate",    "zh": "能详细说说吗",                 "pos": "expr", "scene": "daily"},
    {"word": "what are you getting at", "zh": "你想说的是什么意思",        "pos": "expr", "scene": "daily"},
    {"word": "come again?",          "zh": "再说一遍？/ 什么？",           "pos": "expr", "scene": "daily"},
    {"word": "bear with me",         "zh": "请耐心等一下 / 稍等",          "pos": "expr", "scene": "daily"},

    # ── 时间 / 转折 ───────────────────────────────────────────────────────
    {"word": "all of a sudden",      "zh": "突然之间 / 猛然",              "pos": "expr", "scene": "daily"},
    {"word": "out of the blue",      "zh": "突如其来 / 出乎意料",          "pos": "expr", "scene": "daily"},
    {"word": "sooner or later",      "zh": "迟早 / 早晚",                  "pos": "expr", "scene": "daily"},
    {"word": "at some point",        "zh": "在某个时候 / 总有一天",        "pos": "expr", "scene": "daily"},
    {"word": "from now on",          "zh": "从现在起 / 今后",              "pos": "expr", "scene": "daily"},
    {"word": "moving forward",       "zh": "今后 / 往前走（下一步）",      "pos": "expr", "scene": "work"},
    {"word": "down the road",        "zh": "将来 / 以后",                  "pos": "expr", "scene": "daily"},
    {"word": "for the time being",   "zh": "暂时 / 目前",                  "pos": "expr", "scene": "daily"},
    {"word": "on second thought",    "zh": "再想想 / 转念一想",            "pos": "expr", "scene": "daily"},
    {"word": "in hindsight",         "zh": "事后回想 / 回头看",            "pos": "expr", "scene": "daily"},

    # ── 描述处境 / 表达立场 ───────────────────────────────────────────────
    {"word": "it's up to you",       "zh": "看你的 / 由你决定",            "pos": "expr", "scene": "daily"},
    {"word": "either way",           "zh": "不管怎样 / 两种情况都一样",    "pos": "expr", "scene": "daily"},
    {"word": "no matter what",       "zh": "不管怎样 / 无论如何",          "pos": "expr", "scene": "daily"},
    {"word": "regardless",           "zh": "不管 / 无论如何",              "pos": "adv",  "scene": "daily"},
    {"word": "in any case",          "zh": "无论如何 / 不管怎样",          "pos": "expr", "scene": "daily"},
    {"word": "as it turns out",      "zh": "结果发现 / 事实上",            "pos": "expr", "scene": "daily"},
    {"word": "believe it or not",    "zh": "信不信由你 / 你可能不信",      "pos": "expr", "scene": "daily"},
    {"word": "under the circumstances", "zh": "在这种情况下 / 考虑到情况", "pos": "expr", "scene": "daily"},
    {"word": "it varies",            "zh": "情况不同 / 因情况而定",        "pos": "expr", "scene": "daily"},
    {"word": "out of curiosity",     "zh": "出于好奇 / 随便问问",          "pos": "expr", "scene": "daily"},

    # ── 表达观点 ──────────────────────────────────────────────────────────
    {"word": "the way I see it",     "zh": "在我看来 / 我的看法是",        "pos": "expr", "scene": "daily"},
    {"word": "to be fair",           "zh": "说句公道话 / 平心而论",        "pos": "expr", "scene": "daily"},
    {"word": "to be clear",          "zh": "说清楚一点 / 明确一下",        "pos": "expr", "scene": "daily"},
    {"word": "to put it simply",     "zh": "简单来说 / 说白了",            "pos": "expr", "scene": "daily"},
    {"word": "personally speaking",  "zh": "就我个人而言 / 我个人认为",    "pos": "expr", "scene": "daily"},
    {"word": "speaking of which",    "zh": "说到这个 / 提到这里",          "pos": "expr", "scene": "daily"},
    {"word": "come to think of it",  "zh": "这么一说 / 仔细想想",          "pos": "expr", "scene": "daily"},
    {"word": "now that you mention it", "zh": "你这么一说 / 既然你提到了", "pos": "expr", "scene": "daily"},
    {"word": "keep that in mind",    "zh": "记住这一点 / 把这个放心上",    "pos": "expr", "scene": "daily"},

    # ── 打招呼 / 日常寒暄 ────────────────────────────────────────────────
    {"word": "what's up",            "zh": "怎么了 / 最近咋样",            "pos": "expr", "scene": "daily"},
    {"word": "what's going on",      "zh": "发生什么了 / 最近怎么样",      "pos": "expr", "scene": "daily"},
    {"word": "how's it going",       "zh": "最近怎么样 / 还好吗",          "pos": "expr", "scene": "daily"},
    {"word": "long time no see",     "zh": "好久不见",                     "pos": "expr", "scene": "daily"},
    {"word": "good to see you",      "zh": "很高兴见到你",                 "pos": "expr", "scene": "daily"},
    {"word": "have a good one",      "zh": "祝你过得好 / 保重",            "pos": "expr", "scene": "daily"},
    {"word": "catch you later",      "zh": "回头见 / 等会儿再聊",          "pos": "expr", "scene": "daily"},
    {"word": "see you around",       "zh": "改天见 / 保持联系",            "pos": "expr", "scene": "daily"},
    {"word": "until next time",      "zh": "下次见",                       "pos": "expr", "scene": "daily"},

    # ── 请求帮忙 / 表达许可 ───────────────────────────────────────────────
    {"word": "do me a favor",        "zh": "帮我一个忙",                   "pos": "expr", "scene": "daily"},
    {"word": "I was wondering if",   "zh": "我想问一下是否可以…",          "pos": "expr", "scene": "daily"},
    {"word": "any chance you could", "zh": "你有没有可能…",                "pos": "expr", "scene": "daily"},
    {"word": "feel free to",         "zh": "随便…/ 不用客气",              "pos": "expr", "scene": "daily"},
    {"word": "be my guest",          "zh": "请便 / 随你",                  "pos": "expr", "scene": "daily"},
    {"word": "help yourself",        "zh": "请随便吃喝 / 自己来",          "pos": "expr", "scene": "daily"},

    # ── 鼓励 / 安慰 ───────────────────────────────────────────────────────
    {"word": "you've got this",      "zh": "你能行的 / 加油",              "pos": "expr", "scene": "daily"},
    {"word": "keep it up",           "zh": "继续保持 / 坚持下去",          "pos": "expr", "scene": "daily"},
    {"word": "good for you",         "zh": "太棒了 / 为你高兴",            "pos": "expr", "scene": "daily"},
    {"word": "way to go",            "zh": "干得好 / 太厉害了",            "pos": "expr", "scene": "daily"},
    {"word": "you nailed it",        "zh": "你做到了 / 完美",              "pos": "expr", "scene": "daily"},
    {"word": "you killed it",        "zh": "你太厉害了 / 超棒",            "pos": "expr", "scene": "daily"},
    {"word": "don't worry about it", "zh": "别担心 / 没事的",              "pos": "expr", "scene": "daily"},
    {"word": "no big deal",          "zh": "没什么大不了的 / 小事",        "pos": "expr", "scene": "daily"},
    {"word": "forget about it",      "zh": "别放在心上 / 算了吧",          "pos": "expr", "scene": "daily"},

    # ── 常用动词短语 ──────────────────────────────────────────────────────
    {"word": "work out",             "zh": "解决 / 锻炼 / 结果是",         "pos": "v",    "scene": "daily"},
    {"word": "carry out",            "zh": "执行 / 实施",                  "pos": "v",    "scene": "work"},
    {"word": "point out",            "zh": "指出 / 提出",                  "pos": "v",    "scene": "daily"},
    {"word": "find out",             "zh": "查明 / 发现",                  "pos": "v",    "scene": "daily"},
    {"word": "end up",               "zh": "最终 / 结果（成为）",          "pos": "v",    "scene": "daily"},
    {"word": "turn up",              "zh": "出现 / 找到 / 调高",           "pos": "v",    "scene": "daily"},
    {"word": "give up",              "zh": "放弃",                         "pos": "v",    "scene": "daily"},
    {"word": "pick up",              "zh": "接人 / 拿起 / 学会 / 好转",    "pos": "v",    "scene": "daily"},
    {"word": "drop off",             "zh": "送人下车 / 减少 / 睡着",       "pos": "v",    "scene": "daily"},

    # ── 描述困境 / 意外 ───────────────────────────────────────────────────
    {"word": "something came up",    "zh": "有事情突然出现 / 临时有事",    "pos": "expr", "scene": "daily"},
    {"word": "it slipped my mind",   "zh": "我忘了 / 一时没想起来",        "pos": "expr", "scene": "daily"},
    {"word": "I lost track of time", "zh": "我忘了时间 / 一时入迷",        "pos": "expr", "scene": "daily"},
    {"word": "I'm swamped",          "zh": "我忙得不可开交",               "pos": "expr", "scene": "work"},
    {"word": "that's a bummer",      "zh": "真遗憾 / 太糟了",              "pos": "expr", "scene": "daily"},
    {"word": "what a shame",         "zh": "真可惜 / 太遗憾了",            "pos": "expr", "scene": "daily"},
    {"word": "I can't help it",      "zh": "我没办法 / 情不自禁",          "pos": "expr", "scene": "daily"},
]

# ── Process ───────────────────────────────────────────────────────────────────
d = json.load(open(DATA))
existing_lower = {x['word'].lower() for x in d}

to_add = []
skipped = []
for e in PHRASES:
    if e['word'].lower() in existing_lower:
        skipped.append(e['word'])
    else:
        e.setdefault('ipa', '')
        e.setdefault('ex', '')
        to_add.append(e)

d.extend(to_add)

print(f"Before : {len(existing_lower)}")
print(f"Added  : {len(to_add)}")
print(f"Skipped (already present): {len(skipped)} — {skipped}")
print(f"After  : {len(d)}")

with open(DATA, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print("Done.")
