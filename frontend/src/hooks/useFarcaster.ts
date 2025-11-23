// src/hooks/useFarcaster.ts
'use client';

import { useEffect, useState } from 'react';
import { isFarcasterFrame } from '../utils/miniapp';

export function useFarcaster() {
  const [isFrame, setIsFrame] = useState(false);
  const [frameData, setFrameData] = useState<any>(null);

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const frame = isFarcasterFrame();
      setIsFrame(frame);
      
      if (frame) {
        // Ler dados do frame se disponíveis
        const frameMeta = document.querySelector('meta[name="farcaster:frame"]');
        if (frameMeta) {
          const frameUrl = frameMeta.getAttribute('content');
          setFrameData({ frameUrl });
        }
      }
    }
  }, []);

  return {
    isFrame,
    frameData,
  };
}

