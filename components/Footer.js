//components/Footer.js

import Link from 'next/link';

function Footer() {
    return (
        <footer style={{ background: '#333', color: '#fff', textAlign: 'center', padding: '1rem 0' }}>
            <p>&copy; {new Date().getFullYear()} Gritter. All Rights Reserved.</p>
            <nav>
                <Link href="/privacyPolicy">
                    <span style={{ color: '#fff', marginRight: '1rem' }}>Privacy Policy</span>
                </Link>
                <Link href="/termsOfService">
                    <span style={{ color: '#fff' }}>Terms of Service</span>
                </Link>
            </nav>
        </footer>
    );
}

export default Footer;
