import { render, screen } from '@testing-library/react'
import Home from '../app/page'
import { describe, it, expect } from 'vitest'

describe('Home', () => {
  it('renders heading', () => {
    render(<Home />)
    expect(screen.getByText('Automation für Ihr Unternehmen')).toBeDefined()
  })
})
