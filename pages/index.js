import React from 'react';
import Head from 'next/head';
import Navbar from '../components/Navbar';  // <-- Import the Navbar here

export default function HomePage() {
  return (
    <div>
      <Head>
        <title>Gritter - Home</title>
      </Head>

      <Navbar />  {/* <-- Include the Navbar component here */}

      <header>
        <h1>Welcome to Gritter</h1>
        <p>Your tagline or a brief introduction here.</p>
      </header>

      <main>
        <section>
          <h2>About Us</h2>
          <p>Short description about Gritter, what you do, and your mission.</p>
        </section>

        <section>
          <h2>Services</h2>
          <p>Highlight some of the main services or features of Gritter.</p>
        </section>

        <section>
          <h2>Contact</h2>
          <p>Invite visitors to get in touch or learn more about Gritter.</p>
        </section>
      </main>

      <footer>
        <p>&copy; 2023 Gritter. All Rights Reserved.</p>
      </footer>
    </div>
  );
}
