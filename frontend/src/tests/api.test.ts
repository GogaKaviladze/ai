import { describe, it, expect, vi } from 'vitest'
import { apiFetch } from '../lib/api'

describe('apiFetch', () => {
  it('throws on bad status', async () => {
    global.fetch = vi.fn().mockResolvedValue({ ok: false })
    await expect(apiFetch('/')).rejects.toThrow()
  })
})
