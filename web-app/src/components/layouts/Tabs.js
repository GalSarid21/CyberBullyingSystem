import { useState } from 'react';
import LoadingSpinner from '../LoadingSpinner';
import DbTable from './DbTable';
import './Tabs.css';

function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

function Tabs() {
  const [message, setMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [showTable, setShowTable] = useState(false);
  const [toggleState, setToggleState] = useState(1);

  const handleChange = (event) => {
    setMessage(event.target.value);
  };

  const toggleTab = (index) => {
        setToggleState(index);
  };

  const handleClick = async () => {
    setIsLoading(true);
    setShowTable(false);
    await sleep(1000);
    setIsLoading(false);
    setShowTable(true);
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
          Edit DB Events
        </button>
        <button
          className={toggleState === 3 ? "tabs active-tabs" : "tabs"}
          onClick={() => toggleTab(3)}
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
                />
                <div className='actions'>
                    <button onClick={handleClick}>Get Events</button>
                </div>
            </div>
            <div>
                {isLoading && <LoadingSpinner />}
            </div>
            <div className={showTable && !isLoading ? 'table-show' : 'table-hide'}>
                <DbTable />
            </div>
        </div>

        <div
          className={toggleState === 2 ? "content  active-content" : "content"}
        >
          <h2>Content 2</h2>
          <hr />
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente
            voluptatum qui adipisci.
          </p>
        </div>

        <div
          className={toggleState === 3 ? "content  active-content" : "content"}
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