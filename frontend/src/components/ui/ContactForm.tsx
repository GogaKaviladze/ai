'use client'
import { useForm } from 'react-hook-form'
import { z } from 'zod'
import { zodResolver } from '@hookform/resolvers/zod'
import { Input } from './Input'
import { Button } from './Button'
import { apiFetch } from '../../lib/api'

const schema = z.object({
  name: z.string().min(1),
  email: z.string().email(),
  message: z.string().min(1),
})

type FormData = z.infer<typeof schema>

export function ContactForm() {
  const { register, handleSubmit, reset, formState: { errors } } = useForm<FormData>({ resolver: zodResolver(schema) })
  const onSubmit = async (data: FormData) => {
    await apiFetch('/api/v1/contact', { method: 'POST', body: JSON.stringify(data) })
    reset()
  }
  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4 max-w-md">
      <Input placeholder="Name" {...register('name')} />
      {errors.name && <span className="text-red-500">{errors.name.message}</span>}
      <Input placeholder="Email" type="email" {...register('email')} />
      {errors.email && <span className="text-red-500">{errors.email.message}</span>}
      <textarea className="border p-2 w-full rounded" placeholder="Nachricht" {...register('message')} />
      {errors.message && <span className="text-red-500">{errors.message.message}</span>}
      <Button type="submit">Senden</Button>
    </form>
  )
}
