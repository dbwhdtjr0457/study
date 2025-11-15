import Link from 'next/link';

export default function Home() {
  return (
    <main style={{ padding: '2rem' }}>
      <h1 style={{ fontSize: '2.5rem', fontWeight: 'bold', marginBottom: '2rem' }}>App Router Learning Path</h1>
      <nav>
        <ul style={{ listStyle: 'none', padding: 0 }}>
          <li style={{ marginBottom: '1rem' }}>
            <Link href="/about" style={{ fontSize: '1.2rem', color: 'blue', textDecoration: 'underline' }}>
              1. Basic Routing (/about)
            </Link>
          </li>
          <li style={{ marginBottom: '1rem' }}>
            <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', marginBottom: '0.5rem' }}>2. Nested Routes & Special Files</h2>
            <ul style={{ listStyle: 'none', paddingLeft: '1rem' }}>
              <li style={{ marginBottom: '0.5rem' }}>
                <Link href="/dashboard" style={{ fontSize: '1.2rem', color: 'blue', textDecoration: 'underline' }}>
                  /dashboard (with Layout)
                </Link>
              </li>
              <li>
                <Link href="/dashboard/settings" style={{ fontSize: '1.2rem', color: 'blue', textDecoration: 'underline' }}>
                  /dashboard/settings (Nested Page)
                </Link>
              </li>
            </ul>
          </li>
          <li style={{ marginBottom: '1rem' }}>
            <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', marginBottom: '0.5rem' }}>3. Route Groups</h2>
             <ul style={{ listStyle: 'none', paddingLeft: '1rem' }}>
                <li style={{ marginBottom: '0.5rem' }}>
                  <Link href="/home" style={{ fontSize: '1.2rem', color: 'blue', textDecoration: 'underline' }}>
                    /home (from marketing group)
                  </Link>
                </li>
                <li>
                  <Link href="/pricing" style={{ fontSize: '1.2rem', color: 'blue', textDecoration: 'underline' }}>
                    /pricing (from marketing group)
                  </Link>
                </li>
            </ul>
          </li>
        </ul>
      </nav>
    </main>
  );
}
