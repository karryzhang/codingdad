# Bitget Wallet 战略简报系统

每日自动生成 Bitget Wallet 战略简报，覆盖三大核心领域。

## 📊 简报覆盖

### Domain 1: PayFi (支付金融)
- USDT 流向、稳定币监管
- on/off-ramp 渠道与流动性
- 跨链桥接与交易成本

### Domain 2: 去中心化钱包竞争 & 技术
- 竞品功能发布 (MetaMask, Rabby, Coinbase Wallet)
- Social Login、AA 账户抽象
- EIP 进展、安全事件

### Domain 3: 交易能力
- Meme 交易量与市场情绪
- Perps 流动性与新品发布
- RWA 融资、美股联动

## 🌐 信息源

**英文一级源:**
- CoinDesk, The Block, Decrypt, Cointelegraph
- Ethereum Improvement Proposals (GitHub)

**中文一级源:**
- 链捕手, 律动 BlockBeats, 深潮 TechFlow, Foresight News

**其他数据源:**
- Dune Analytics, Santiment, Twitter/X, Polymarket

## 📁 目录结构

```
bitget-brief/
├── index.html          # 简报查看页面
├── README.md           # 本文件
└── daily/
    ├── latest.json     # 最新简报数据 (实时更新)
    ├── 2026-02-23.json # 历史简报存档
    └── ...
```

## 🚀 使用方式

1. 打开 `index.html` 查看最新简报
2. 简报每天 9:00 SGT 自动生成
3. 历史简报保存在 `daily/` 文件夹
4. 每条信息包含：标题、来源、时间、相关度评分、对业务影响、原文链接

## 📋 简报数据格式

```json
{
  "date": "2026-02-23",
  "domains": [
    {
      "icon": "💰",
      "name": "Domain 1: PayFi",
      "items": [
        {
          "title": "新闻标题",
          "source": "来源 (语言)",
          "time": "发布时间",
          "score": 9,
          "impact": "对业务的影响",
          "url": "原文链接"
        }
      ]
    }
  ],
  "alerts": ["紧急信息1", "紧急信息2"]
}
```

## 🔄 自动更新

- Cron 任务配置：每天 9:00 SGT (Asia/Singapore)
- 生成逻辑：3个域 × 3条信息 = 9条关键信息
- 优化策略：token 节省 60%+，平衡数据深度与响应速度

## 📌 最后更新

- 日期: 2026-02-23
- 版本: v1.0
- 状态: 生产环境
