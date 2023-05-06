import { useState } from "react";
import LoadingSpinner from "./LoadingSpinner";
import classes from './CollapsibleInputItem.module.css'
import Prediction from "./Prediction";

function CollapsibleContent() {

    const [data, setData] = useState([]);
    const [tweet, setTweet] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [showTweetDiv, setShowTweetDiv] = useState(false);
    const [showResultsDiv, setShowResultsDiv] = useState(false);
    const [err, setErr] = useState('');

    const handleTweet = async () => {
        setErr('');
        setIsLoading(true);
        setShowTweetDiv(false);
        setShowResultsDiv(false);

        try {
          const response = await fetch('http://localhost:5000/api/db-posts/random', {
            method: 'GET',
            headers: {
              Accept: 'application/json',
            },
          });
    
          if (!response.ok) {
            throw new Error(`Error! status: ${response.status}`);
          }
    
          const result = await response.json();
    
          console.log('tweet is: ', JSON.stringify(result, null, 4));
    
          setTweet(result);
          setShowTweetDiv(true);
        } catch (err) {
          setErr(err.message);
        } finally {
          setIsLoading(false);
        }
      };
    
      console.log(data);
    
      const handlePrediction = async () => {
        setErr('');
        setIsLoading(true);

        try {
          const url = 'http://localhost:5000/api/user-input/detect-bullying?text='
          const response = await fetch(url.concat('', tweet.content), {
            method: 'GET',
            headers: {
              Accept: 'application/json',
            },
          });
    
          if (!response.ok) {
            throw new Error(`Error! status: ${response.status}`);
          }
    
          const result = await response.json();
    
          console.log('prediction is: ', JSON.stringify(result, null, 4));
          
          setData(result);
          setIsLoading(false);
          setShowResultsDiv(true);
        } catch (err) {
          setErr(err.message);
        } finally {
            setIsLoading(false);
        }
      };

    return (
        <div>
            <div>
                {err && <h2>{err}</h2>}
                {isLoading && <LoadingSpinner />}
            </div>
            <div className={showTweetDiv ? classes.contentshow : classes.content}>
                <h3>Tweet Content: </h3>
                <p>{tweet.content}</p>
                <h3>Author: </h3>
                <p>{tweet.user_name}</p>
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
                <button className={classes.button} onClick={handleTweet}>Get Tweet</button>
                <button onClick={handlePrediction}>Get Prediction</button>
            </div>
        </div>
    );
}

export default CollapsibleContent;