import './DbTable.css';

function DbTable(props) {
    return (
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Source</th>
                    <th>User Name</th>
                    <th>Content</th>
                    <th>Timestamp</th>
                    <th>Toxic</th>
                    <th>Severe Toxic</th>
                    <th>Obscene</th>
                    <th>Threat</th>
                    <th>Insult</th>
                    <th>Identity Hate</th>
                </tr>
            </thead>
            <tbody>
                {props.posts && props.posts.map(post =>
                    <tr key={post.id}>
                        <td>{post.id}</td>
                        <td>{post.source}</td>
                        <td><span className='table-span'>{post.userName}</span></td>
                        <td><span className='table-span'>{post.content}</span></td>
                        <td><span className='table-span'>{post.addedOn}</span></td>
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