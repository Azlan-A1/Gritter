// pages/home.js
import React from 'react';
import Head from 'next/head';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import useDarkMode from '../hooks/useDarkMode';  // <-- Import the custom hook


export default function HomePage() {
    const [theme, toggleTheme] = useDarkMode();

    return (
        <div className={theme}>
            <Head>
                <title>Gritter - Home</title>
            </Head>

            <Navbar />

            <button onClick={toggleTheme}>
                {theme === 'light' ? 'Switch to Dark Mode' : 'Switch to Light Mode'}
            </button>

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

            <Footer />

            <style jsx>{`
                /* ... existing styles ... */

                /* Add your dark and light theme styles */
                .dark {
                    background-color: #121212;
                    color: #fff;
                }

                .light {
                    background-color: #fff;
                    color: #000;
                }

                /* ... other existing styles ... */
                .profile-container {
                    max-width: 400px;
                    margin: 60px auto;
                    text-align: center;
                }

                .avatar {
                    width: 100px;
                    height: 100px;
                    border-radius: 50%;
                    object-fit: cover;
                }

                .username {
                    color: #777;
                    font-size: 14px;
                }

                .bio {
                    margin: 20px 0;
                    font-size: 16px;
                }

                .stats {
                    display: flex;
                    justify-content: space-between;
                    margin-top: 60px;
                }

                .stat-number {
                    font-weight: bold;
                }
            `}</style>
        </div>
    );
}
