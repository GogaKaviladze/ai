import { render, screen } from '@testing-library/react'
import { ContactForm } from '../components/ui/ContactForm'
import { describe, it, expect } from 'vitest'

describe('ContactForm', () => {
  it('has submit button', () => {
    render(<ContactForm />)
    expect(screen.getByText('Senden')).toBeDefined()
  })
})
