import React, { useState } from 'react';
import './DbTable.css';

function DbTable() {
    const [posts, setPosts] = useState([
        { id: 1, source: 'Twitter', userName: 'Test', content: 'this is a tweet', toxic: 'true', severeToxic: 'false', obscene: 'false', threat: 'false', insult: 'true', identityHate: 'false', addedOn: '2023-05-05T01:07:36.089Z', lastUpdatedOn: '2023-05-05T01:07:36.091Z' },
        { id: 2, source: 'Twitter', userName: 'Test1', content: 'this is a longer tweet', toxic: 'true', severeToxic: 'false', obscene: 'false', threat: 'false', insult: 'true', identityHate: 'false', addedOn: '2023-05-05T01:07:37.021Z', lastUpdatedOn: '2023-05-05T01:07:37.022' },
        { id: 3, source: 'Twitter', userName: 'Test2', content: 'this is a very very long tweet', toxic: 'true', severeToxic: 'false', obscene: 'false', threat: 'false', insult: 'true', identityHate: 'false', addedOn: '2023-05-05T01:07:37.154', lastUpdatedOn: '2023-05-05T01:07:37.154' },
        { id: 4, source: 'Twitter', userName: 'Test3', content: 'this is a super ulta mega longgggggggggggggggg tweet', toxic: 'true', severeToxic: 'false', obscene: 'false', threat: 'false', insult: 'true', identityHate: 'false', addedOn: '2023-05-05T01:07:37.154', lastUpdatedOn: '2023-05-05T01:07:37.154' },
        { id: 5, source: 'Twitter', userName: 'Test4', content: 'this is a super ulta mega longgggggggggggggggg tweettttttttt', toxic: 'true', severeToxic: 'false', obscene: 'false', threat: 'false', insult: 'true', identityHate: 'false', addedOn: '2023-05-05T01:07:37.154', lastUpdatedOn: '2023-05-05T01:07:37.154' },
        { id: 4, source: 'Twitter', userName: 'Test3', content: 'this is a super ulta mega longgggggggggggggggg tweet', toxic: 'true', severeToxic: 'false', obscene: 'false', threat: 'false', insult: 'true', identityHate: 'false', addedOn: '2023-05-05T01:07:37.154', lastUpdatedOn: '2023-05-05T01:07:37.154' },
        { id: 4, source: 'Twitter', userName: 'Test3', content: 'this is a super ulta mega longgggggggggggggggg tweet', toxic: 'true', severeToxic: 'false', obscene: 'false', threat: 'false', insult: 'true', identityHate: 'false', addedOn: '2023-05-05T01:07:37.154', lastUpdatedOn: '2023-05-05T01:07:37.154' },
        { id: 4, source: 'Twitter', userName: 'Test3', content: 'this is a super ulta mega longgggggggggggggggg tweet', toxic: 'true', severeToxic: 'false', obscene: 'false', threat: 'false', insult: 'true', identityHate: 'false', addedOn: '2023-05-05T01:07:37.154', lastUpdatedOn: '2023-05-05T01:07:37.154' },
        { id: 4, source: 'Twitter', userName: 'Test3', content: 'this is a super ulta mega longgggggggggggggggg tweet', toxic: 'true', severeToxic: 'false', obscene: 'false', threat: 'false', insult: 'true', identityHate: 'false', addedOn: '2023-05-05T01:07:37.154', lastUpdatedOn: '2023-05-05T01:07:37.154' }
    ]);

    return (
        <table>
            <thead>
                <tr>
                    <th>Source</th>
                    <th>User Name</th>
                    <th>Content</th>
                    <th>Toxic</th>
                    <th>Severe Toxic</th>
                    <th>Obscene</th>
                    <th>Threat</th>
                    <th>Insult</th>
                    <th>Identity Hate</th>
                </tr>
            </thead>
            <tbody>
                {posts && posts.map(post =>
                    <tr key={post.id}>
                        <td>{post.source}</td>
                        <td><span>{post.userName}</span></td>
                        <td><span>{post.content}</span></td>
                        <td>{post.toxic}</td>
                        <td>{post.severeToxic}</td>
                        <td>{post.obscene}</td>
                        <td>{post.threat}</td>
                        <td>{post.insult}</td>
                        <td>{post.identityHate}</td>
                    </tr>
                )}
            </tbody>
        </table>
    );
}

export default DbTable;