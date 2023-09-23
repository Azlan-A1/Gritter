// components/Footer.js

function Footer() {
    return (
        <footer style={{ background: '#333', color: '#fff', textAlign: 'center', padding: '1rem 0' }}>
            <p>&copy; {new Date().getFullYear()} Gritter. All Rights Reserved.</p>
        </footer>
    );
}

export default Footer;
