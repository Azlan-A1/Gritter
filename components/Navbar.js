// components/Navbar.js
import Link from 'next/link';

function Navbar() {
  return (
    <nav>
      <span className="nav-item"><Link href="/">Home</Link></span>
      <span className="nav-item"><Link href="/about">About</Link></span>
      <span className="nav-item"><Link href="/contact">Contact</Link></span>
      <span className="nav-item"><Link href="/profile">Profile</Link></span>
      <span className="nav-item"><Link href="/privacy-policy">Privacy Policy</Link></span>

      <style jsx>{`
        .nav-item {
            margin-right: 15px;  // Adjust the value as needed
        }
      `}</style>
    </nav>
  );
}

export default Navbar;
