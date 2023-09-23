//components/Footer.js

import Link from 'next/link';

function Footer() {
    return (
        <footer style={{ background: '#333', color: '#fff', textAlign: 'center', padding: '1rem 0' }}>
            <p>&copy; {new Date().getFullYear()} Gritter. All Rights Reserved.</p>
            <nav>
                <Link href="/privacyPolicy">
                    <a style={{ color: '#fff', marginRight: '1rem' }}>Privacy Policy</a>
                </Link>
                <Link href="/termsOfService">
                    <a style={{ color: '#fff' }}>Terms of Service</a>
                </Link>
            </nav>
        </footer>
    );
}

export default Footer;
