'use client'
import { useEffect, useState } from 'react'

export default function Dashboard() {
  const [contacts, setContacts] = useState([])
  useEffect(() => {
    fetch('/api/v1/contact', { credentials: 'include' })
      .then(r => r.json())
      .then(setContacts)
  }, [])
  return (
    <main className="p-8">
      <h1 className="text-3xl font-bold mb-4">Admin Dashboard</h1>
      <pre>{JSON.stringify(contacts, null, 2)}</pre>
    </main>
  )
}
