// components/Navbar.js
import Link from 'next/link';

function Navbar() {
  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
      <Link href="/contact">Contact</Link>
      <Link href="/profile">Profile</Link>
      <Link href="/privacy-policy">Privacy Policy</Link>
    </nav>
  );
}

export default Navbar;
