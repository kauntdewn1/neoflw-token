/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // Especifica o diretório raiz do projeto para evitar confusão com lockfiles externos
  outputFileTracingRoot: require('path').join(__dirname, '../'),
  
  // Headers para suportar MiniApps (Telegram/Farcaster)
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'X-Frame-Options',
            value: 'ALLOWALL', // Permitir embed em Telegram/Farcaster
          },
          {
            key: 'Content-Security-Policy',
            value: "frame-ancestors 'self' https://*.telegram.org https://*.farcaster.xyz https://warpcast.com;",
          },
        ],
      },
    ];
  },
  
  images: {
    unoptimized: true, // Para IPFS deploy (opcional)
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'gateway.lighthouse.storage',
        pathname: '/ipfs/**',
      },
      {
        protocol: 'https',
        hostname: 'ipfs.io',
        pathname: '/ipfs/**',
      },
      {
        protocol: 'https',
        hostname: 'cloudflare-ipfs.com',
        pathname: '/ipfs/**',
      },
    ],
  },
};

module.exports = nextConfig;

