import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "App Router Demo",
  description: "Learning Next.js App Router",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
