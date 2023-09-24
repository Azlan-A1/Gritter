import React from 'react';
import Head from 'next/head';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

export default function ContactUs() {
  return (
    <div>
      <Head>
        <title>Gritter - Contact Us</title>
      </Head>

      <Navbar />

      <main>
        <h1>Contact Us</h1>
        <p>Have questions? We'd love to hear from you! Fill out the form below and we'll get back to you as soon as possible.</p>

        <form action="/api/contact" method="post">
          <div>
            <label htmlFor="name">Name:</label>
            <input type="text" id="name" name="name" required />
          </div>

          <div>
            <label htmlFor="email">Email:</label>
            <input type="email" id="email" name="email" required />
          </div>

          <div>
            <label htmlFor="message">Message:</label>
            <textarea id="message" name="message" rows="5" required></textarea>
          </div>

          <div>
            <button type="submit">Send</button>
          </div>
        </form>
      </main>

      <Footer /> {/* <-- Include the Footer component here */}

    </div>
  );
}
