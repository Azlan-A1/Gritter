// pages/profile.js
import React from 'react';
import Head from 'next/head';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer'; // Assuming you have a Footer component

function Profile() {
    const user = {
        name: 'John Doe',
        username: '@johndoe',
        avatar: '/path/to/avatar.jpg',  // Path to an image in your public folder
        bio: 'Web developer. Passionate about Next.js and OpenAI.',
        postsCount: 120,
        followersCount: 250,
        followingCount: 300
    };

    return (
        <div>
            <Head>
                <title>{user.name}'s Profile</title>
            </Head>

            <div className="profile-container">
                <img src={user.avatar} alt={`${user.name}'s Avatar`} className="avatar" />
                <h1>{user.name}</h1>
                <span className="username">{user.username}</span>
                <p className="bio">{user.bio}</p>

                <div className="stats">
                    <div>
                        <span className="stat-number">{user.postsCount}</span>
                        <span className="stat-label">Posts</span>
                    </div>
                    <div>
                        <span className="stat-number">{user.followersCount}</span>
                        <span className="stat-label">Followers</span>
                    </div>
                    <div>
                        <span className="stat-number">{user.followingCount}</span>
                        <span className="stat-label">Following</span>
                    </div>
                </div>
            </div>

            <Footer />
            <style jsx>{`
                .profile-container {
                    max-width: 400px;
                    margin: 20px auto;
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
                    margin-top: 20px;
                }

                .stat-number {
                    font-weight: bold;
                }
            `}</style>
        </div>
    );
}

export default Profile;
