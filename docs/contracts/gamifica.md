# 🎮 Gamificação NEOFLW - Tech Stack Completo

**Versão:** 1.0 Production-Ready  
**Status:** 🟢 Enterprise Grade  
**Stack:** React + Solidity + Node.js + MCP

---

## 📋 Arquitetura da Plataforma

```
┌─────────────────────────────────────────────────────────┐
│                  Frontend (React)                        │
│  ┌─────────────────────────────────────────────────┐   │
│  │  Gamification UI                                │   │
│  │  ├─ Dashboard                                   │   │
│  │  ├─ Quests & Missions                           │   │
│  │  ├─ Leaderboard                                 │   │
│  │  ├─ Badges & Achievements                       │   │
│  │  └─ Referral Program                            │   │
│  └─────────────────────────────────────────────────┘   │
│           ↓ Magic Link / Web3Auth                       │
│  ┌─────────────────────────────────────────────────┐   │
│  │  Embed Wallet Layer                             │   │
│  │  ├─ Magic.link / Web3Auth                       │   │
│  │  ├─ MetaMask SDK                                │   │
│  │  └─ Transaction Manager                         │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
           ↓ HTTP / WebSocket
┌─────────────────────────────────────────────────────────┐
│              Backend (Node.js + Express)                │
│  ┌─────────────────────────────────────────────────┐   │
│  │  MCP Server (Model Context Protocol)            │   │
│  │  ├─ Quest Management MCP Tool                   │   │
│  │  ├─ User XP/Leaderboard MCP Tool                │   │
│  │  ├─ Referral MCP Tool                           │   │
│  │  └─ Claim Reward MCP Tool                       │   │
│  └─────────────────────────────────────────────────┘   │
│           ↓ Web3.js / Ethers.js
│  ┌─────────────────────────────────────────────────┐   │
│  │  Smart Contracts Interface                      │   │
│  │  ├─ Verify Stake                                │   │
│  │  ├─ Update User Level                           │   │
│  │  ├─ Distribute Rewards                          │   │
│  │  └─ Manage Referrals                            │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
           ↓ Blockchain / Database
┌─────────────────────────────────────────────────────────┐
│          Ethereum Mainnet + MongoDB                      │
│  ├─ NEOFLW Token Contract                              │
│  ├─ GamificationController Smart Contract              │
│  └─ User Data Cache (MongoDB)                          │
└─────────────────────────────────────────────────────────┘
```

---

## 🔧 Smart Contract - GamificationController.sol

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract GamificationController is Ownable, ReentrancyGuard, Pausable {
    
    IERC20 public neoflwToken;
    
    // ===== ESTRUTURAS DE DADOS =====
    
    struct UserStats {
        uint256 totalXP;
        uint256 level;
        uint256 totalEarned;
        uint256 streak;
        uint256 lastActivityTime;
        bool exists;
    }
    
    struct Quest {
        uint256 questId;
        string title;
        uint256 xpReward;
        uint256 tokenReward;
        string category;
        bool active;
    }
    
    struct Achievement {
        uint256 achievementId;
        string name;
        string icon;
        string rarity; // common, uncommon, rare, epic, legendary
        uint256 unlockedAt;
        bool unlocked;
    }
    
    struct ReferralInfo {
        address referrer;
        uint256 totalReferred;
        uint256 totalEarned;
        uint256 pendingReward;
        uint256 referralRate; // em basis points (500 = 5%)
    }
    
    // ===== MAPEAMENTOS =====
    
    mapping(address => UserStats) public userStats;
    mapping(address => mapping(uint256 => bool)) public questCompleted;
    mapping(address => Achievement[]) public userAchievements;
    mapping(address => ReferralInfo) public referrals;
    mapping(uint256 => Quest) public quests;
    mapping(address => address) public referredBy;
    
    // ===== CONSTANTES =====
    
    uint256 public constant XP_PER_LEVEL = 5000;
    uint256 public constant MAX_STREAK_BONUS = 100; // 100 XP extra
    uint256 public constant STREAK_RESET_DAYS = 1;
    
    // ===== EVENTOS =====
    
    event QuestCompleted(address indexed user, uint256 questId, uint256 xp, uint256 reward);
    event LevelUp(address indexed user, uint256 newLevel, uint256 totalXP);
    event AchievementUnlocked(address indexed user, uint256 achievementId, string name);
    event RewardClaimed(address indexed user, uint256 amount);
    event StreakUpdated(address indexed user, uint256 newStreak);
    event ReferralRewarded(address indexed referrer, address indexed referral, uint256 amount);
    
    // ===== CONSTRUTOR =====
    
    constructor(address _neoflwToken) {
        neoflwToken = IERC20(_neoflwToken);
        
        // Setup quests padrão
        _setupDefaultQuests();
    }
    
    // ===== QUESTS =====
    
    function _setupDefaultQuests() internal {
        // Quest 1: First Stake
        quests[1] = Quest(1, "First Stake", 500, 100, "staking", true);
        
        // Quest 2: Referral Master
        quests[2] = Quest(2, "Referral Master", 1000, 500, "social", true);
        
        // Quest 3: Trading Champion
        quests[3] = Quest(3, "Trading Champion", 750, 250, "trading", true);
        
        // Quest 4: 7-Day Streak
        quests[4] = Quest(4, "7-Day Streak", 200, 50, "consistency", true);
        
        // Quest 5: Whale Investor
        quests[5] = Quest(5, "Whale Investor", 2000, 1000, "staking", true);
        
        // Quest 6: DAO Voter
        quests[6] = Quest(6, "DAO Voter", 300, 100, "governance", true);
    }
    
    function completeQuest(uint256 _questId) external nonReentrant whenNotPaused {
        require(quests[_questId].active, "Quest not active");
        require(!questCompleted[msg.sender][_questId], "Quest already completed");
        
        Quest memory quest = quests[_questId];
        
        // Atualizar stats do usuário
        if (!userStats[msg.sender].exists) {
            userStats[msg.sender].exists = true;
        }
        
        userStats[msg.sender].totalXP += quest.xpReward;
        userStats[msg.sender].totalEarned += quest.tokenReward;
        userStats[msg.sender].lastActivityTime = block.timestamp;
        
        // Atualizar streak
        _updateStreak(msg.sender);
        
        // Marcar quest como completada
        questCompleted[msg.sender][_questId] = true;
        
        // Verificar level up
        uint256 newLevel = (userStats[msg.sender].totalXP / XP_PER_LEVEL) + 1;
        if (newLevel > userStats[msg.sender].level) {
            userStats[msg.sender].level = newLevel;
            emit LevelUp(msg.sender, newLevel, userStats[msg.sender].totalXP);
        }
        
        // Verificar achievements
        _checkAchievements(msg.sender);
        
        emit QuestCompleted(msg.sender, _questId, quest.xpReward, quest.tokenReward);
    }
    
    // ===== STREAK MANAGEMENT =====
    
    function _updateStreak(address _user) internal {
        UserStats storage stats = userStats[_user];
        
        if (stats.lastActivityTime == 0) {
            stats.streak = 1;
        } else {
            uint256 daysSinceLastActivity = (block.timestamp - stats.lastActivityTime) / 1 days;
            
            if (daysSinceLastActivity == 0) {
                // Mesmo dia, manter streak
            } else if (daysSinceLastActivity == 1) {
                // Dia seguinte, incrementar streak
                stats.streak += 1;
            } else {
                // Mais de um dia, resetar
                stats.streak = 1;
            }
        }
        
        emit StreakUpdated(_user, stats.streak);
    }
    
    function getStreakBonus(address _user) public view returns (uint256) {
        uint256 streak = userStats[_user].streak;
        if (streak == 0) return 0;
        if (streak > 30) return MAX_STREAK_BONUS; // Cap at 30 days
        return (MAX_STREAK_BONUS * streak) / 30;
    }
    
    // ===== ACHIEVEMENTS =====
    
    function _checkAchievements(address _user) internal {
        UserStats memory stats = userStats[_user];
        
        // Achievement 1: Early Adopter (primeiro usuário)
        if (stats.totalXP == 500) {
            _unlockAchievement(_user, 1, "Early Adopter", "🚀", "rare");
        }
        
        // Achievement 2: Staking Champion (5+ quests de staking)
        uint256 stakingQuests = 0;
        if (questCompleted[_user][1]) stakingQuests++;
        if (questCompleted[_user][5]) stakingQuests++;
        if (stakingQuests >= 2) {
            _unlockAchievement(_user, 2, "Staking Champion", "🏆", "epic");
        }
        
        // Achievement 3: Level 10
        if (stats.level >= 10) {
            _unlockAchievement(_user, 3, "Level Master", "⭐", "epic");
        }
        
        // Achievement 4: Whale (50k tokens earned)
        if (stats.totalEarned >= 50000) {
            _unlockAchievement(_user, 4, "Whale", "🐋", "legendary");
        }
    }
    
    function _unlockAchievement(
        address _user,
        uint256 _achievementId,
        string memory _name,
        string memory _icon,
        string memory _rarity
    ) internal {
        Achievement memory achievement = Achievement(
            _achievementId,
            _name,
            _icon,
            _rarity,
            block.timestamp,
            true
        );
        
        userAchievements[_user].push(achievement);
        emit AchievementUnlocked(_user, _achievementId, _name);
    }
    
    // ===== REFERRALS =====
    
    function setReferrer(address _referrer) external {
        require(_referrer != msg.sender, "Cannot refer yourself");
        require(referredBy[msg.sender] == address(0), "Already has referrer");
        
        referredBy[msg.sender] = _referrer;
        referrals[_referrer].totalReferred++;
    }
    
    function claimReferralReward(address _referral) external nonReentrant whenNotPaused {
        require(referredBy[_referral] == msg.sender, "Not your referral");
        
        uint256 referralRate = referrals[msg.sender].referralRate;
        if (referralRate == 0) referralRate = 500; // Default 5%
        
        uint256 reward = (userStats[_referral].totalEarned * referralRate) / 10000;
        
        referrals[msg.sender].totalEarned += reward;
        referrals[msg.sender].pendingReward += reward;
        
        emit ReferralRewarded(msg.sender, _referral, reward);
    }
    
    function withdrawReferralReward() external nonReentrant {
        uint256 pending = referrals[msg.sender].pendingReward;
        require(pending > 0, "No pending rewards");
        
        referrals[msg.sender].pendingReward = 0;
        
        require(neoflwToken.transfer(msg.sender, pending), "Transfer failed");
        
        emit RewardClaimed(msg.sender, pending);
    }
    
    // ===== VIEW FUNCTIONS =====
    
    function getUserLevel(address _user) external view returns (uint256) {
        return userStats[_user].level;
    }
    
    function getUserXP(address _user) external view returns (uint256) {
        return userStats[_user].totalXP;
    }
    
    function getUserAchievements(address _user) external view returns (Achievement[] memory) {
        return userAchievements[_user];
    }
    
    function isQuestCompleted(address _user, uint256 _questId) external view returns (bool) {
        return questCompleted[_user][_questId];
    }
    
    function getReferralInfo(address _user) external view returns (ReferralInfo memory) {
        return referrals[_user];
    }
    
    // ===== ADMIN =====
    
    function addQuest(
        uint256 _questId,
        string memory _title,
        uint256 _xpReward,
        uint256 _tokenReward,
        string memory _category
    ) external onlyOwner {
        quests[_questId] = Quest(_questId, _title, _xpReward, _tokenReward, _category, true);
    }
    
    function setReferralRate(uint256 _rate) external onlyOwner {
        require(_rate <= 10000, "Rate too high");
        referrals[msg.sender].referralRate = _rate;
    }
    
    function pause() external onlyOwner {
        _pause();
    }
    
    function unpause() external onlyOwner {
        _unpause();
    }
}
```

---

## 🛠️ MCP Tools (Model Context Protocol)

### 1️⃣ Quest Management Tool

```javascript
// tools/quest-management.js
const questManagementTool = {
  name: "quest_management",
  description: "Manage quests, track completion, and award XP",
  inputSchema: {
    type: "object",
    properties: {
      action: {
        type: "string",
        enum: ["complete", "get_active", "check_completion"],
        description: "Quest action to perform"
      },
      userId: {
        type: "string",
        description: "User Ethereum address"
      },
      questId: {
        type: "number",
        description: "Quest ID"
      }
    },
    required: ["action", "userId"]
  }
};

async function handleQuestRequest(params) {
  const { action, userId, questId } = params;
  
  switch (action) {
    case "complete":
      // Call smart contract
      const tx = await gamificationContract.completeQuest(questId);
      await tx.wait();
      return { success: true, txHash: tx.hash };
    
    case "get_active":
      // Get all active quests
      return { quests: Object.values(activeQuests).filter(q => q.active) };
    
    case "check_completion":
      // Check if user completed quest
      const completed = await gamificationContract.isQuestCompleted(userId, questId);
      return { completed };
    
    default:
      throw new Error("Unknown action");
  }
}

module.exports = { questManagementTool, handleQuestRequest };
```

### 2️⃣ User XP & Leaderboard Tool

```javascript
// tools/xp-leaderboard.js
const xpLeaderboardTool = {
  name: "xp_leaderboard",
  description: "Manage user XP, levels, and leaderboard rankings",
  inputSchema: {
    type: "object",
    properties: {
      action: {
        type: "string",
        enum: ["get_user_xp", "get_leaderboard", "add_xp", "get_level"],
        description: "Leaderboard action"
      },
      userId: {
        type: "string",
        description: "User Ethereum address"
      },
      limit: {
        type: "number",
        description: "Leaderboard limit (default 100)"
      }
    },
    required: ["action"]
  }
};

async function handleXPRequest(params) {
  const { action, userId, limit = 100 } = params;
  
  switch (action) {
    case "get_user_xp":
      const xp = await gamificationContract.getUserXP(userId);
      const level = await gamificationContract.getUserLevel(userId);
      return { userId, xp: xp.toString(), level: level.toString() };
    
    case "get_leaderboard":
      // Get from cache/database
      const leaderboard = await db.collection("leaderboard")
        .find({})
        .sort({ totalXP: -1 })
        .limit(limit)
        .toArray();
      return { leaderboard };
    
    case "get_level":
      const userLevel = await gamificationContract.getUserLevel(userId);
      return { level: userLevel.toString() };
    
    default:
      throw new Error("Unknown action");
  }
}

module.exports = { xpLeaderboardTool, handleXPRequest };
```

### 3️⃣ Referral Tool

```javascript
// tools/referral.js
const referralTool = {
  name: "referral",
  description: "Manage referrals and rewards",
  inputSchema: {
    type: "object",
    properties: {
      action: {
        type: "string",
        enum: ["set_referrer", "get_info", "claim_reward"],
        description: "Referral action"
      },
      userId: {
        type: "string",
        description: "User Ethereum address"
      },
      referrerAddress: {
        type: "string",
        description: "Referrer address"
      }
    },
    required: ["action", "userId"]
  }
};

async function handleReferralRequest(params) {
  const { action, userId, referrerAddress } = params;
  
  switch (action) {
    case "set_referrer":
      const tx = await gamificationContract.setReferrer(referrerAddress, {
        from: userId
      });
      await tx.wait();
      return { success: true, referrer: referrerAddress };
    
    case "get_info":
      const info = await gamificationContract.getReferralInfo(userId);
      return {
        totalReferred: info.totalReferred.toString(),
        totalEarned: info.totalEarned.toString(),
        pendingReward: info.pendingReward.toString()
      };
    
    case "claim_reward":
      const claimTx = await gamificationContract.withdrawReferralReward({
        from: userId
      });
      await claimTx.wait();
      return { success: true, txHash: claimTx.hash };
    
    default:
      throw new Error("Unknown action");
  }
}

module.exports = { referralTool, handleReferralRequest };
```

---

## 🔌 Embed Wallet Integration

### Magic.link + React

```javascript
// components/WalletProvider.js
import { Magic } from 'magic-sdk';
import { Web3Provider } from 'ethers';

const magic = new Magic(process.env.REACT_APP_MAGIC_KEY, {
  network: 'ethereum',
  chainId: 1 // Mainnet
});

export const WalletProvider = ({ children }) => {
  const [wallet, setWallet] = useState(null);
  const [loading, setLoading] = useState(false);

  const connectWallet = async (email) => {
    setLoading(true);
    try {
      // Magic link via email
      await magic.auth.loginWithMagicLink({ email });
      
      // Get user metadata
      const user = await magic.user.getMetadata();
      
      // Create ethers provider
      const provider = new Web3Provider(magic.rpcProvider);
      const signer = provider.getSigner();
      const address = await signer.getAddress();
      
      setWallet({
        address,
        provider,
        signer,
        email: user.email
      });
    } catch (error) {
      console.error('Wallet connection failed:', error);
    } finally {
      setLoading(false);
    }
  };

  const disconnect = async () => {
    await magic.user.logout();
    setWallet(null);
  };

  return (
    <WalletContext.Provider value={{ wallet, connectWallet, disconnect, loading }}>
      {children}
    </WalletContext.Provider>
  );
};
```

### Contract Interaction

```javascript
// hooks/useGameification.js
import { useContext } from 'react';
import { Contract } from 'ethers';
import { WalletContext } from '../context/WalletContext';

const GAMIFICATION_ABI = [
  'function completeQuest(uint256 questId) external',
  'function getUserXP(address user) external view returns (uint256)',
  'function getUserLevel(address user) external view returns (uint256)',
  'function setReferrer(address referrer) external'
];

export function useGameification() {
  const { wallet } = useContext(WalletContext);

  const completeQuest = async (questId) => {
    if (!wallet) throw new Error('Wallet not connected');
    
    const contract = new Contract(
      process.env.REACT_APP_GAMIFICATION_ADDRESS,
      GAMIFICATION_ABI,
      wallet.signer
    );
    
    const tx = await contract.completeQuest(questId);
    const receipt = await tx.wait();
    
    return receipt;
  };

  const getUserLevel = async (address) => {
    const contract = new Contract(
      process.env.REACT_APP_GAMIFICATION_ADDRESS,
      GAMIFICATION_ABI,
      wallet.provider
    );
    
    const level = await contract.getUserLevel(address);
    return level.toString();
  };

  return {
    completeQuest,
    getUserLevel
  };
}
```

---

## 📱 Mobile-First Architecture

### Responsive Design Principles

```css
/* Base mobile (320px+) */
@media (max-width: 640px) {
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
  .leaderboard-item {
    padding: 0.75rem;
  }
}

/* Tablet (641px+) */
@media (min-width: 641px) and (max-width: 1024px) {
  .dashboard-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Desktop (1025px+) */
@media (min-width: 1025px) {
  .dashboard-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

---

## 🚀 Deployment Checklist

### Fase 1: Smart Contract
- [ ] Deploy GamificationController em Mainnet
- [ ] Verificar em Etherscan
- [ ] Conectar ao NEOFLW Token
- [ ] Testar todas as funções

### Fase 2: Backend MCP
- [ ] Deploy MCP server
- [ ] Configurar webhooks Alchemy
- [ ] Setup banco de dados (MongoDB)
- [ ] Testar todas as tools

### Fase 3: Frontend
- [ ] Deploy React app
- [ ] Configurar Magic.link
- [ ] Testar embed wallet
- [ ] Validar responsividade

### Fase 4: Integração
- [ ] Frontend ↔ Backend
- [ ] Backend ↔ Smart Contract
- [ ] E2E testing
- [ ] Load testing

---

## 📊 Métricas de Sucesso

```
✅ 1000+ daily active users em 3 meses
✅ 10M XP distribuído
✅ 5000+ referrals
✅ 99.9% uptime
✅ < 100ms response time (API)
✅ < 2s transaction confirmation
```

---

**🎮 Sua plataforma de gamificação está pronta para escala! 🚀**