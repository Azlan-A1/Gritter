import React from 'react';
import Footer from './Footer';

function Layout({ children }) {
    return (
        <div className="layout">
            {children}
            <Footer />
            <style jsx>{`
                .layout {
                    display: flex;
                    flex-direction: column;
                    min-height: 100vh;
                }
            `}</style>
        </div>
    );
}

export default Layout;
