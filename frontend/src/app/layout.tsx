import "../styles/globals.css"
import { ReactNode } from 'react'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Hansabit – Automatisierung und Digitalisierung',
  description: 'Moderne Lösungen für Unternehmen',
  openGraph: {
    title: 'Hansabit',
    description: 'Automatisierung und Digitalisierung',
    url: 'https://hansabit.de',
    siteName: 'Hansabit',
  },
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="de">
      <body className="min-h-screen flex flex-col">
        {children}
      </body>
    </html>
  )
}
