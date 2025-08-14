import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    serverActions: true,
  },
  i18n: {
    locales: ['de', 'en'],
    defaultLocale: 'de',
  },
}

export default nextConfig
