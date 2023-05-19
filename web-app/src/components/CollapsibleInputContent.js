import { useState } from 'react';
import LoadingSpinner from './LoadingSpinner';
import classes from './CollapsibleInputItem.module.css';
import Prediction from './Prediction';

function CollapsibleInputContent() {

    const [message, setMessage] = useState('');
    const [data, setData] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [showResultsDiv, setshowResultsDiv] = useState(false);
    const [err, setErr] = useState('');
    
    const handleChange = (event) => {
        setMessage(event.target.value);
    };

    const handleClick = async () => {
        setErr('');
        setIsLoading(true);
        setshowResultsDiv(false);

        try {
          const url = 'http://localhost:5000/api/user-input/detect-bullying?text='
          const response = await fetch(url.concat('', message.slice(1)), {
            method: 'GET',
            headers: {
              Accept: 'application/json',
            },
          });
    
          if (!response.ok) {
            throw new Error(`Error! status: ${response.status}`);
          }
    
          const result = await response.json();
    
          console.log('result is: ', JSON.stringify(result, null, 4));
    
          setData(result);
        } catch (err) {
          setErr(err.message);
          setData([]);
        } finally {
          setIsLoading(false);
          setshowResultsDiv(true);
        }
      };
    
      console.log(data);
    
    return (
        <div>
            <h4>Please enter your free text for the NLP model below:</h4>
            <input
                className={classes.input}
                type='text'
                id='message'
                name='message'
                onChange={handleChange}
                value={message}
            />
            <div>
                {err && <h2>{err}</h2>}
                {isLoading && <LoadingSpinner />}
            </div>
            <div className={showResultsDiv ? classes.contentshow : classes.content}>
                <h3>Model Prediction: </h3>
                {data.map(labels => {
                    return <div>
                      <Prediction labels={labels}/>
                    </div>;
                })}
            </div>
            <div className={classes.actions}>
                <button onClick={handleClick}>Start</button>
            </div>
        </div>
    );
}

export default CollapsibleInputContent;