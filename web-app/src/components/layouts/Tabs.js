import { useState } from 'react';
import LoadingSpinner from '../LoadingSpinner';
import NewDbMonitorForm from './NewDbMonitorForm';
import DbTable from './DbTable';
import './Tabs.css';

function Tabs() {
  const [err, setErr] = useState('');
  const [posts, setPosts] = useState([]);
  const [message, setMessage] = useState('');
  const [deleteId, setDeleteId] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [showTable, setShowTable] = useState(false);
  const [showDeleteMsg, setshowDeleteMsg] = useState(false);
  const [toggleState, setToggleState] = useState(1);

  const handleKeypress = (event) => {
    if (event.keyCode === 13) { //enter
      handleClick();
    }
  }

  const handleDeleteKeypress = (event) => {
    if (event.keyCode === 13) { //enter
      handleDelete();
    }
  }

  const handleChange = (event) => {
    setMessage(event.target.value);
  };

  const handleDeleteChange = (event) => {
    setDeleteId(event.target.value);
  };

  const toggleTab = (index) => {
        setToggleState(index);
  };

  const handleClick = async () => {
    setErr('');
    setIsLoading(true);
    setShowTable(false);

    try {
      const url = 'http://localhost:5000/api/hate-monitors?user_name='
      const response = await fetch(url.concat('', message), {
        method: 'GET',
        headers: {
          Accept: 'application/json',
        },
      });

      if (response.status === 200) {
        const result = await response.json();
        console.log('result is: ', JSON.stringify(result, null, 4));
        setPosts(result);
        setShowTable(true);
      }
      else if (response.status === 204) {
        throw new Error(`Could not find events for the user: ${message}`);
      }
      else {
        throw new Error(`Error! status: ${response.status}`);
      }
    } 
    
    catch (err) {
      setErr(err.message);
      setPosts([]);
    } 
    
    finally {
      setIsLoading(false);
    }
  }

  const handleDelete = async () => {
    setErr('');
    setIsLoading(true);
    setshowDeleteMsg(false);

    try {
      const url = 'http://localhost:5000/api/hate-monitors/delete?id='
      const response = await fetch(url.concat('', deleteId), {
        method: 'GET',
        headers: {
          Accept: 'application/json',
        },
      });

      if (!response.status === 204) {
        throw new Error(`Error! status: ${response.status}`);
      }
      setshowDeleteMsg(true);
    } 
    
    catch (err) {
      setErr(err.message);
    } 
    
    finally {
      setIsLoading(false);
    }
  }

  return (
    <div className="container">
      <div className="bloc-tabs">
        <button
          className={toggleState === 1 ? "tabs active-tabs" : "tabs"}
          onClick={() => toggleTab(1)}
        >
          Get DB Events By User Name
        </button>
        <button
          className={toggleState === 2 ? "tabs active-tabs" : "tabs"}
          onClick={() => toggleTab(2)}
        >
          Add a DB Monitor
        </button>
        <button
          className={toggleState === 3 ? "tabs active-tabs" : "tabs"}
          onClick={() => toggleTab(3)}
        >
          Delete a DB Monitor
        </button>
        <button
          className={toggleState === 4 ? "tabs active-tabs" : "tabs"}
          onClick={() => toggleTab(4)}
        >
          Scan DB By User Name
        </button>
      </div>

      <div className="content-tabs">
        <div
          className={toggleState === 1 ? "content  active-content" : "content"}
        >
            <div className='input'>
                <h4>Please enter user name:</h4>
                <input
                    className='input-text'
                    type='text'
                    id='message'
                    name='message'
                    onChange={handleChange}
                    value={message}
                    onKeyDown={handleKeypress}
                />
                <div className='actions'>
                    <button 
                      onClick={handleClick}>
                        Get events
                    </button>
                </div>
            </div>
            <div>
                {err && <h3>{err}</h3>}
                {isLoading && <LoadingSpinner />}
            </div>
            <div className={showTable && !isLoading ? 'table-show' : 'table-hide'}>
                <DbTable posts={posts}/>
            </div>
        </div>

        <div
          className={toggleState === 2 ? "content  active-content" : "content"}
        >
          <div>
            <h2>Add a new entry to the DB Monitor table</h2>
            <NewDbMonitorForm />
          </div>
        </div>
        
        <div
          className={toggleState === 3 ? "content  active-content" : "content"}
        >
            <div className='input'>
                <h4>Please enter hate monitor id to delete:</h4>
                <input
                    className='input-text'
                    type='text'
                    id='delete'
                    name='delete'
                    onChange={handleDeleteChange}
                    value={deleteId}
                    onKeyDown={handleDeleteKeypress}
                />
                <div className='actions'>
                    <button onClick={handleDelete}>Delete</button>
                </div>
            </div>
            <div>
                {err && <h3>{err}</h3>}
                {isLoading && <LoadingSpinner />}
            </div>
            <div className={showDeleteMsg && !isLoading ? 'active-content' : 'content'}>
              <h3>Event was deleted successfully!</h3>
            </div>
        </div>
        
        <div
          className={toggleState === 4 ? "content  active-content" : "content"}
        >
          <h2>Content 3</h2>
          <hr />
          <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eos sed
            nostrum rerum laudantium totam unde adipisci incidunt modi alias!
            Accusamus in quia odit aspernatur provident et ad vel distinctio
            recusandae totam quidem repudiandae omnis veritatis nostrum
            laboriosam architecto optio rem, dignissimos voluptatum beatae
            aperiam voluptatem atque. Beatae rerum dolores sunt.
          </p>
        </div>
      </div>
    </div>
  );
}

export default Tabs;