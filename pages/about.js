import React from 'react';
import Head from 'next/head';
import Navbar from '../components/Navbar';

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
        </div>
    );
}

export default AboutPage;
