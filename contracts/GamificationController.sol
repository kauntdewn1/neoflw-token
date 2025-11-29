// contracts/GamificationController.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title GamificationController
 * @notice Contrato de gamificação para NEOFLW - Gerencia quests, XP, achievements e referrals
 * @dev Otimizado para Polygon (gas baixo permite microtransações)
 */
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
        bool exists;
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
    mapping(address => mapping(uint256 => bool)) private achievementUnlocked; // Para evitar duplicatas
    
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
    event QuestAdded(uint256 questId, string title);
    event QuestDeactivated(uint256 questId);
    
    // ===== CONSTRUTOR =====
    
    constructor(address _neoflwToken) {
        require(_neoflwToken != address(0), "Invalid token address");
        neoflwToken = IERC20(_neoflwToken);
        
        // Setup quests padrão
        _setupDefaultQuests();
    }
    
    // ===== QUESTS =====
    
    function _setupDefaultQuests() internal {
        // Quest 1: First Stake
        quests[1] = Quest(1, "First Stake", 500, 100 * 10**18, "staking", true);
        
        // Quest 2: Referral Master
        quests[2] = Quest(2, "Referral Master", 1000, 500 * 10**18, "social", true);
        
        // Quest 3: Trading Champion
        quests[3] = Quest(3, "Trading Champion", 750, 250 * 10**18, "trading", true);
        
        // Quest 4: 7-Day Streak
        quests[4] = Quest(4, "7-Day Streak", 200, 50 * 10**18, "consistency", true);
        
        // Quest 5: Whale Investor
        quests[5] = Quest(5, "Whale Investor", 2000, 1000 * 10**18, "staking", true);
        
        // Quest 6: DAO Voter
        quests[6] = Quest(6, "DAO Voter", 300, 100 * 10**18, "governance", true);
    }
    
    function completeQuest(uint256 _questId) external nonReentrant whenNotPaused {
        require(quests[_questId].active, "Quest not active");
        require(!questCompleted[msg.sender][_questId], "Quest already completed");
        
        Quest memory quest = quests[_questId];
        
        // Atualizar stats do usuário
        if (!userStats[msg.sender].exists) {
            userStats[msg.sender].exists = true;
            userStats[msg.sender].level = 1;
        }
        
        userStats[msg.sender].totalXP += quest.xpReward;
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
        
        // Transferir reward de tokens (se houver)
        if (quest.tokenReward > 0) {
            require(
                neoflwToken.balanceOf(address(this)) >= quest.tokenReward,
                "Insufficient contract balance"
            );
            userStats[msg.sender].totalEarned += quest.tokenReward;
            require(
                neoflwToken.transfer(msg.sender, quest.tokenReward),
                "Token transfer failed"
            );
        }
        
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
        
        // Achievement 1: Early Adopter (primeiro quest completado)
        if (stats.totalXP >= 500 && !achievementUnlocked[_user][1]) {
            _unlockAchievement(_user, 1, "Early Adopter", "rocket", "rare");
        }
        
        // Achievement 2: Staking Champion (2+ quests de staking)
        uint256 stakingQuests = 0;
        if (questCompleted[_user][1]) stakingQuests++;
        if (questCompleted[_user][5]) stakingQuests++;
        if (stakingQuests >= 2 && !achievementUnlocked[_user][2]) {
            _unlockAchievement(_user, 2, "Staking Champion", "trophy", "epic");
        }
        
        // Achievement 3: Level 10
        if (stats.level >= 10 && !achievementUnlocked[_user][3]) {
            _unlockAchievement(_user, 3, "Level Master", "star", "epic");
        }
        
        // Achievement 4: Whale (50k tokens earned)
        if (stats.totalEarned >= 50000 * 10**18 && !achievementUnlocked[_user][4]) {
            _unlockAchievement(_user, 4, "Whale", "whale", "legendary");
        }
    }
    
    function _unlockAchievement(
        address _user,
        uint256 _achievementId,
        string memory _name,
        string memory _icon,
        string memory _rarity
    ) internal {
        require(!achievementUnlocked[_user][_achievementId], "Achievement already unlocked");
        
        achievementUnlocked[_user][_achievementId] = true;
        
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
        require(_referrer != address(0), "Invalid referrer address");
        require(referredBy[msg.sender] == address(0), "Already has referrer");
        
        referredBy[msg.sender] = _referrer;
        
        if (!referrals[_referrer].exists) {
            referrals[_referrer].exists = true;
            referrals[_referrer].referralRate = 500; // Default 5%
        }
        
        referrals[_referrer].totalReferred++;
    }
    
    function claimReferralReward(address _referral) external nonReentrant whenNotPaused {
        require(referredBy[_referral] == msg.sender, "Not your referral");
        
        ReferralInfo storage referrerInfo = referrals[msg.sender];
        uint256 referralRate = referrerInfo.referralRate;
        if (referralRate == 0) referralRate = 500; // Default 5%
        
        uint256 reward = (userStats[_referral].totalEarned * referralRate) / 10000;
        
        referrerInfo.totalEarned += reward;
        referrerInfo.pendingReward += reward;
        
        emit ReferralRewarded(msg.sender, _referral, reward);
    }
    
    function withdrawReferralReward() external nonReentrant {
        uint256 pending = referrals[msg.sender].pendingReward;
        require(pending > 0, "No pending rewards");
        
        referrals[msg.sender].pendingReward = 0;
        
        require(
            neoflwToken.balanceOf(address(this)) >= pending,
            "Insufficient contract balance"
        );
        
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
    
    function getUserStats(address _user) external view returns (UserStats memory) {
        return userStats[_user];
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
    
    function getQuest(uint256 _questId) external view returns (Quest memory) {
        return quests[_questId];
    }
    
    // ===== ADMIN =====
    
    function addQuest(
        uint256 _questId,
        string memory _title,
        uint256 _xpReward,
        uint256 _tokenReward,
        string memory _category
    ) external onlyOwner {
        require(_questId > 0, "Invalid quest ID");
        quests[_questId] = Quest(_questId, _title, _xpReward, _tokenReward, _category, true);
        emit QuestAdded(_questId, _title);
    }
    
    function deactivateQuest(uint256 _questId) external onlyOwner {
        require(quests[_questId].questId != 0, "Quest does not exist");
        quests[_questId].active = false;
        emit QuestDeactivated(_questId);
    }
    
    function setReferralRate(uint256 _rate) external onlyOwner {
        require(_rate <= 10000, "Rate too high"); // Max 100%
        referrals[msg.sender].referralRate = _rate;
    }
    
    function depositRewards(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        require(
            neoflwToken.transferFrom(msg.sender, address(this), _amount),
            "Transfer failed"
        );
        emit RewardClaimed(msg.sender, _amount);
    }
    
    function pause() external onlyOwner {
        _pause();
    }
    
    function unpause() external onlyOwner {
        _unpause();
    }
}

