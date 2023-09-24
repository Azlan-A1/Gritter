import React from 'react';
import Head from 'next/head';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

function AboutPage() {
    return (
        <div>
          <Head>
            <title>About Gritter</title>
          </Head>

          <Navbar />
            
            <p>
                Gritter is an innovative platform designed to [Your Description Here].
            </p>
            <p>
                Our mission is to [Your Mission Statement Here].
            </p>
        
            <Footer />  {/* <-- Include the Footer component here */}

            <style jsx>{`
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

export default AboutPage;
