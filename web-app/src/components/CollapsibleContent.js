import { useState } from 'react';
import LoadingSpinner from './LoadingSpinner';
import classes from './CollapsibleInputItem.module.css';
import Prediction from './Prediction';
import twitterImg from '../images/twitter.png'

function CollapsibleContent() {

    const [data, setData] = useState([]);
    const [tweet, setTweet] = useState([]);
    const [isLoadingTweet, setIsLoadingTweet] = useState(false);
    const [isLoadingPreds, setIsLoadingPreds] = useState(false);
    const [showTweetDiv, setShowTweetDiv] = useState(false);
    const [showResultsDiv, setShowResultsDiv] = useState(false);
    const [err, setErr] = useState('');

    const handleTweet = async () => {
        setErr('');
        setIsLoadingTweet(true);
        setShowTweetDiv(false);
        setShowResultsDiv(false);

        try {
          const url = 'http://localhost:5000/api/db-posts/random';
          const response = await fetch(url, {
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
        } 
        
        catch (err) {
          setErr(err.message);
        } 
        
        finally {
          setIsLoadingTweet(false);
        }
      };
    
      console.log(data);
    
      const handlePrediction = async () => {
        setErr('');
        setIsLoadingPreds(true);

        try {
          const url = 'http://localhost:5000/api/user-input/detect-bullying?text=';
          const queryString = tweet.content.startsWith('#') 
                            ? tweet.content.slice(1) 
                            : tweet.content;
          const response = await fetch(url.concat('', queryString), {
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
          setShowResultsDiv(true);
        } catch (err) {
          setErr(err.message);
        } finally {
          setIsLoadingPreds(false);
        }
      };

    return (
        <div className={classes.tweetBorder}>
            <div>
                {err && <h2>{err}</h2>}
                {isLoadingTweet && <LoadingSpinner isSmall={true}/>}
            </div>
            <div className={showTweetDiv ? classes.twitterTweet : classes.content}>
                <header className={classes.header}>
                  <h3 className={classes.tweetHeader}>Tweet Content</h3>
                  <span className={classes.span}>
                    <h4 className={classes.author}>Author: </h4>
                    <p className={classes.author}>{tweet.user_name}</p>
                  </span>
                  <img className={classes.img} src={twitterImg} alt='twitter' />
                </header>
                <p classeName={classes.twitterTweet}>{tweet.content}</p>
            </div>
            {isLoadingPreds && <LoadingSpinner isSmall={true}/>}
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