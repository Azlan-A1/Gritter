//components/Footer.js
import Link from 'next/link';

function Footer() {
    return (
        <footer style={{ 
            background: '#333', 
            color: '#fff', 
            textAlign: 'center', 
            padding: '1rem 0',
            position: 'fixed',
            left: 0,
            right: 0,
            bottom: 0,
            display: 'flex',
            justifyContent: 'center', // <-- center items horizontally
            alignItems: 'center'      // <-- center items vertically
        }}>
            <p style={{ margin: '0 1rem' }}>&copy; {new Date().getFullYear()} Gritter. All Rights Reserved.</p>
            <nav style={{ display: 'flex' }}>
                <Link href="/privacyPolicy">
                    <span style={{ color: '#fff', margin: '0 1rem' }}>Privacy Policy</span>
                </Link>
                <Link href="/termsOfService">
                    <span style={{ color: '#fff', margin: '0 1rem' }}>Terms of Service</span>
                </Link>
            </nav>
        </footer>
    );
}

export default Footer;
