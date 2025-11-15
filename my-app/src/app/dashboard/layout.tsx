// app/dashboard/layout.tsx
import React from 'react';

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <section style={{ border: '1px solid #ccc', padding: '1rem', borderRadius: '8px' }}>
      <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', marginBottom: '1rem' }}>Dashboard Layout</h2>
      <nav style={{ marginBottom: '1rem' }}>
        {/* Add dashboard-specific navigation here */}
      </nav>
      {children}
    </section>
  );
}
