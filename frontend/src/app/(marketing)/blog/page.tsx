import Link from 'next/link'

export default function Blog() {
  return (
    <main className="p-8">
      <h1 className="text-3xl font-bold mb-4">Blog</h1>
      <ul className="list-disc pl-6">
        <li><Link href="/blog/posts/hello">Erster Beitrag</Link></li>
      </ul>
    </main>
  )
}
