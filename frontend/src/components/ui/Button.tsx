import { ButtonHTMLAttributes } from 'react'

export function Button(props: ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button className="bg-blue-600 text-white px-4 py-2 rounded" {...props} />
  )
}
