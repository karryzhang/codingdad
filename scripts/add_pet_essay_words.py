#!/usr/bin/env python3
"""Add ~100 essay-writing words to pet-words-1000.json."""
import json, pathlib

DATA = pathlib.Path(__file__).parent.parent / 'game' / 'pet-words-1000.json'

ESSAY_WORDS = [
    # ── 连接词 / 衔接过渡 (18) ──────────────────────────────────────────────
    {"word": "furthermore",   "zh": "此外，而且",               "pos": "adv"},
    {"word": "moreover",      "zh": "而且，此外",               "pos": "adv"},
    {"word": "nevertheless",  "zh": "尽管如此，然而",           "pos": "adv"},
    {"word": "consequently",  "zh": "因此，结果",               "pos": "adv"},
    {"word": "meanwhile",     "zh": "与此同时，期间",           "pos": "adv"},
    {"word": "subsequently",  "zh": "随后，接着",               "pos": "adv"},
    {"word": "alternatively", "zh": "或者，另一方面",           "pos": "adv"},
    {"word": "whereas",       "zh": "然而，而（对比）",         "pos": "conj"},
    {"word": "despite",       "zh": "尽管，不管",               "pos": "prep"},
    {"word": "accordingly",   "zh": "因此，相应地",             "pos": "adv"},
    {"word": "nonetheless",   "zh": "尽管如此，仍然",           "pos": "adv"},
    {"word": "likewise",      "zh": "同样，也",                 "pos": "adv"},
    {"word": "conversely",    "zh": "相反地，反之",             "pos": "adv"},
    {"word": "simultaneously","zh": "同时，一起",               "pos": "adv"},
    {"word": "therefore",     "zh": "因此，所以",               "pos": "adv"},
    {"word": "thereby",       "zh": "从而，因此",               "pos": "adv"},
    {"word": "otherwise",     "zh": "否则，要不然",             "pos": "adv"},
    {"word": "regarding",     "zh": "关于，就…而言",            "pos": "prep"},

    # ── 写作动词 (14) ──────────────────────────────────────────────────────
    {"word": "claim",         "zh": "声称，主张",               "pos": "v"},
    {"word": "suggest",       "zh": "建议，暗示",               "pos": "v"},
    {"word": "imply",         "zh": "暗示，意味着",             "pos": "v"},
    {"word": "reveal",        "zh": "揭示，表明",               "pos": "v"},
    {"word": "highlight",     "zh": "突出，强调",               "pos": "v"},
    {"word": "illustrate",    "zh": "说明，举例说明",           "pos": "v"},
    {"word": "analyse",       "zh": "分析，研究",               "pos": "v"},
    {"word": "explore",       "zh": "探讨，探索",               "pos": "v"},
    {"word": "reflect",       "zh": "反映，深思",               "pos": "v"},
    {"word": "portray",       "zh": "描绘，描述",               "pos": "v"},
    {"word": "convey",        "zh": "传达，表达",               "pos": "v"},
    {"word": "contradict",    "zh": "反驳，与…矛盾",            "pos": "v"},
    {"word": "reinforce",     "zh": "加强，巩固",               "pos": "v"},
    {"word": "establish",     "zh": "建立，确立",               "pos": "v"},

    # ── 生动形容词 (22) ────────────────────────────────────────────────────
    {"word": "remarkable",    "zh": "显著的，非凡的",           "pos": "adj"},
    {"word": "crucial",       "zh": "关键的，至关重要的",       "pos": "adj"},
    {"word": "vital",         "zh": "极重要的，必不可少的",     "pos": "adj"},
    {"word": "profound",      "zh": "深刻的，影响深远的",       "pos": "adj"},
    {"word": "subtle",        "zh": "微妙的，隐约的",           "pos": "adj"},
    {"word": "vivid",         "zh": "生动的，鲜明的",           "pos": "adj"},
    {"word": "striking",      "zh": "引人注目的，显著的",       "pos": "adj"},
    {"word": "compelling",    "zh": "令人信服的，引人入胜的",   "pos": "adj"},
    {"word": "engaging",      "zh": "吸引人的，有趣的",         "pos": "adj"},
    {"word": "fascinating",   "zh": "极有吸引力的，迷人的",     "pos": "adj"},
    {"word": "intriguing",    "zh": "有趣的，迷人的",           "pos": "adj"},
    {"word": "overwhelming",  "zh": "压倒性的，势不可挡的",     "pos": "adj"},
    {"word": "dramatic",      "zh": "戏剧性的，引人注目的",     "pos": "adj"},
    {"word": "extraordinary", "zh": "非凡的，特别的",           "pos": "adj"},
    {"word": "outstanding",   "zh": "杰出的，显著的",           "pos": "adj"},
    {"word": "prominent",     "zh": "突出的，著名的",           "pos": "adj"},
    {"word": "prevalent",     "zh": "普遍的，流行的",           "pos": "adj"},
    {"word": "apparent",      "zh": "明显的，表面上的",         "pos": "adj"},
    {"word": "evident",       "zh": "明显的，显而易见的",       "pos": "adj"},
    {"word": "inherent",      "zh": "固有的，内在的",           "pos": "adj"},
    {"word": "abstract",      "zh": "抽象的，摘要",             "pos": "adj"},
    {"word": "subjective",    "zh": "主观的，个人的",           "pos": "adj"},

    # ── 状语副词，增强表达力 (20) ─────────────────────────────────────────
    {"word": "significantly", "zh": "显著地，重大地",           "pos": "adv"},
    {"word": "considerably",  "zh": "相当地，大量地",           "pos": "adv"},
    {"word": "increasingly",  "zh": "越来越，日益",             "pos": "adv"},
    {"word": "essentially",   "zh": "本质上，实质上",           "pos": "adv"},
    {"word": "particularly",  "zh": "尤其，特别",               "pos": "adv"},
    {"word": "generally",     "zh": "一般地，通常",             "pos": "adv"},
    {"word": "typically",     "zh": "通常，典型地",             "pos": "adv"},
    {"word": "frequently",    "zh": "频繁地，经常",             "pos": "adv"},
    {"word": "occasionally",  "zh": "偶尔，有时",               "pos": "adv"},
    {"word": "ultimately",    "zh": "最终，根本上",             "pos": "adv"},
    {"word": "primarily",     "zh": "主要地，首先",             "pos": "adv"},
    {"word": "initially",     "zh": "起初，最初",               "pos": "adv"},
    {"word": "gradually",     "zh": "逐渐地，缓慢地",           "pos": "adv"},
    {"word": "deliberately",  "zh": "故意地，深思熟虑地",       "pos": "adv"},
    {"word": "apparently",    "zh": "显然，表面上看来",         "pos": "adv"},
    {"word": "effectively",   "zh": "有效地，实际上",           "pos": "adv"},
    {"word": "precisely",     "zh": "精确地，恰恰",             "pos": "adv"},
    {"word": "strongly",      "zh": "强烈地，坚定地",           "pos": "adv"},
    {"word": "widely",        "zh": "广泛地，普遍地",           "pos": "adv"},
    {"word": "deeply",        "zh": "深深地，强烈地",           "pos": "adv"},

    # ── 议论文常用名词 (18) ────────────────────────────────────────────────
    {"word": "factor",        "zh": "因素，要素",               "pos": "n"},
    {"word": "aspect",        "zh": "方面，方面",               "pos": "n"},
    {"word": "impact",        "zh": "影响，冲击",               "pos": "n"},
    {"word": "notion",        "zh": "观念，概念",               "pos": "n"},
    {"word": "concept",       "zh": "概念，观念",               "pos": "n"},
    {"word": "principle",     "zh": "原则，原理",               "pos": "n"},
    {"word": "implication",   "zh": "含义，影响，暗示",         "pos": "n"},
    {"word": "viewpoint",     "zh": "观点，看法",               "pos": "n"},
    {"word": "argument",      "zh": "论点，争论",               "pos": "n"},
    {"word": "insight",       "zh": "见解，洞察力",             "pos": "n"},
    {"word": "outcome",       "zh": "结果，结局",               "pos": "n"},
    {"word": "obstacle",      "zh": "障碍，阻碍",               "pos": "n"},
    {"word": "alternative",   "zh": "替代选择，另一种可能",     "pos": "n"},
    {"word": "foundation",    "zh": "基础，根基",               "pos": "n"},
    {"word": "framework",     "zh": "框架，结构",               "pos": "n"},
    {"word": "dimension",     "zh": "维度，层面",               "pos": "n"},
    {"word": "scope",         "zh": "范围，余地",               "pos": "n"},
    {"word": "narrative",     "zh": "叙述，故事线",             "pos": "n"},

    # ── 写作品质形容词（评价文本用）(8) ──────────────────────────────────
    {"word": "eloquent",      "zh": "雄辩的，有口才的",         "pos": "adj"},
    {"word": "concise",       "zh": "简洁的，简明的",           "pos": "adj"},
    {"word": "coherent",      "zh": "连贯的，一致的",           "pos": "adj"},
    {"word": "persuasive",    "zh": "有说服力的",               "pos": "adj"},
    {"word": "comprehensive", "zh": "全面的，综合的",           "pos": "adj"},
    {"word": "sophisticated", "zh": "复杂的，精致的，有见识的", "pos": "adj"},
    {"word": "meaningful",    "zh": "有意义的，重要的",         "pos": "adj"},
    {"word": "constructive",  "zh": "建设性的，有益的",         "pos": "adj"},
]

# ── Process ───────────────────────────────────────────────────────────────────
d = json.load(open(DATA))
existing = {x['word'] for x in d}

to_add = [e for e in ESSAY_WORDS if e['word'] not in existing]
# ensure ipa field present
for e in to_add:
    e.setdefault('ipa', '')

d.extend(to_add)

print(f"Before: {len(existing)}  Added: {len(to_add)}  After: {len(d)}")
skipped = [e['word'] for e in ESSAY_WORDS if e['word'] in existing]
if skipped:
    print(f"Already present (skipped): {skipped}")

with open(DATA, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print("Done.")
