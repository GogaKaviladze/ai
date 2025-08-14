import Link from 'next/link'
import { ContactForm } from '../components/ui/ContactForm'

export default function Home() {
  return (
    <main className="flex-1">
      <section className="bg-gray-50 py-20 text-center">
        <h1 className="text-4xl font-bold mb-4">Automation für Ihr Unternehmen</h1>
        <p className="mb-6">Wir digitalisieren Prozesse und schaffen Freiräume.</p>
        <Link href="/kontakt" className="bg-blue-600 text-white px-4 py-2 rounded">Kontakt</Link>
      </section>
      <section className="p-8 grid md:grid-cols-3 gap-6">
        <div className="shadow p-4 rounded">
          <h2 className="font-semibold mb-2">Beratung</h2>
          <p>Wir analysieren Ihre Abläufe und finden Potenziale.</p>
        </div>
        <div className="shadow p-4 rounded">
          <h2 className="font-semibold mb-2">Entwicklung</h2>
          <p>Individuelle Softwarelösungen für Ihren Bedarf.</p>
        </div>
        <div className="shadow p-4 rounded">
          <h2 className="font-semibold mb-2">Betrieb</h2>
          <p>Wir betreuen Ihre Systeme langfristig.</p>
        </div>
      </section>
      <section className="p-8" id="kontakt">
        <h2 className="text-2xl font-bold mb-4">Kontakt</h2>
        <ContactForm />
      </section>
    </main>
  )
}
