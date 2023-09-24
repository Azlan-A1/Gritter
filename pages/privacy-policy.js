import React from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';  // <-- Import the Footer component

function Privacypolicy() {
    return (
        <div>
            <Navbar />
            <h1>Privacy Policy</h1>
            <p>Here is our privacy policy...</p>
            
            <Footer />  {/* <-- Include the Footer component here */}
        </div>
    );
}

export default Privacypolicy;
