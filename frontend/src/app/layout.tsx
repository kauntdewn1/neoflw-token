// src/app/layout.tsx
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import { Providers } from './providers';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'NEOFLW Protocol',
  description: 'Tokenização com propósito - NeoFlow Token',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pt-BR">
      <head>
        {/* Telegram MiniApp viewport */}
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
        <meta name="telegram-web-app" content="true" />
        
        {/* Farcaster Frame */}
        <meta name="farcaster:frame" content="vNext" />
        <meta property="fc:frame" content="vNext" />
        <meta property="fc:frame:image" content="https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i" />
        <meta property="fc:frame:button:1" content="Stake NEOFLW" />
        <meta property="fc:frame:button:1:action" content="link" />
        <meta property="fc:frame:button:1:target" content="https://neoflowoff.eth" />
        <meta property="fc:frame:button:2" content="View Leaderboard" />
        <meta property="fc:frame:button:2:action" content="link" />
        <meta property="fc:frame:button:2:target" content="https://neoflowoff.eth/leaderboard" />
      </head>
      <body className={inter.className}>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}

