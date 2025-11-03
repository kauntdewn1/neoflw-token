// src/config/contracts.ts
import { TOKEN_CONFIG } from './token';

// Endereços dos contratos (ajustar após deploy)
export const CONTRACT_ADDRESSES = {
  token: TOKEN_CONFIG.address,
  vault: process.env.NEXT_PUBLIC_VAULT_ADDRESS || "", // Adicionar após deploy
  claim: process.env.NEXT_PUBLIC_CLAIM_ADDRESS || "", // Adicionar após deploy
  governor: process.env.NEXT_PUBLIC_GOVERNOR_ADDRESS || "", // Adicionar após deploy
};

// ABIs básicos (versões simplificadas)
export const TOKEN_ABI = [
  "function name() view returns (string)",
  "function symbol() view returns (string)",
  "function decimals() view returns (uint8)",
  "function totalSupply() view returns (uint256)",
  "function balanceOf(address) view returns (uint256)",
  "function burn(uint256) external",
  "event Burned(address indexed account, uint256 amount)",
] as const;

export const VAULT_ABI = [
  "function stake(uint256 _amount) external",
  "function claim() external",
  "function stakes(address) view returns (uint256 amount, uint256 startTime, bool claimed)",
  "function timeLeft(address) view returns (uint256)",
  "function totalStakedAmount() view returns (uint256)",
  "function totalRewardsReserved() view returns (uint256)",
  "function getTotalStaked() view returns (uint256)",
  "function getAvailableBalance() view returns (uint256)",
  "event Staked(address indexed user, uint256 amount)",
  "event Claimed(address indexed user, uint256 amount, uint256 reward, uint256 total)",
] as const;

export const CLAIM_ABI = [
  "function claimTokens() external",
  "function claimableAmount(address) view returns (uint256)",
  "function hasClaimed(address) view returns (bool)",
  "function contractBalance() view returns (uint256)",
  "event TokensClaimed(address indexed user, uint256 amount)",
] as const;

