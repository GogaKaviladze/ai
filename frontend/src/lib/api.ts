export async function apiFetch(path: string, options?: RequestInit) {
  const res = await fetch(path, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })
  if (!res.ok) throw new Error('API error')
  return res.json()
}

export const fetcher = (url: string) => apiFetch(url)
