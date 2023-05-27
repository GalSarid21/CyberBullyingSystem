import { useRef, useState } from 'react';
import LoadingSpinner from '../LoadingSpinner';
import Prediction from '../Prediction';
import DateTimePicker from 'react-datetime-picker';
import './NewDbMonitorForm.css';
import 'react-datetime-picker/dist/DateTimePicker.css';
import 'react-calendar/dist/Calendar.css';
import 'react-clock/dist/Clock.css';

function NewDbMonitorForm() {
    
    const sourceInputRef = useRef();
    const userNameInputRef = useRef();
    const contentInputRef = useRef();

    const [showResultsDiv, setshowResultsDiv] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    const [date, onDateChange] = useState(new Date());
    const [data, setData] = useState([]);
    const [err, setErr] = useState('');

    const handleSubmission = async (event) => {
        event.preventDefault();
        setErr('');
        setIsLoading(true);

        const sourceInput = sourceInputRef.current.value;
        const userNameInput = userNameInputRef.current.value;
        const contentInput = contentInputRef.current.value;

        try {
            const url = 'http://localhost:5000/api/user-input/detect-bullying?text='
            const queryString = contentInput.startsWith('#') ? contentInput.slice(1) : contentInput;
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
            setData(result);
          } 
          catch (err) {
            setErr(err.message);
            setData([]);
          } 
          finally {
            setIsLoading(false);
            setshowResultsDiv(true);
          }

          const newPostData = {
            'source': sourceInput,
            'userName': userNameInput,
            'content': contentInput,
            'toxic': data.toxic ? 1 : 0,
            'severeToxic': data.severeToxic ? 1 : 0,
            'obscene': data.obscene ? 1 : 0,
            'threat': data.threat ? 1 : 0,
            'insult': data.insult ? 1 : 0,
            'identityHate': data.identityHate ? 1 : 0,
            'addedOn' : date
          }

        try {
            const url = 'http://localhost:5000/api/hate-monitors/add'
            const response = await fetch(url, {
                method: 'POST',
                body: JSON.stringify(newPostData),
                headers: {
                    Accept: 'application/json',
                },
            });

            if (!response.ok) {
                throw new Error(`Error! status: ${response.status}`);
            }
        } 
        catch (err) {
            setErr(err.message);
        } 
      };
    
    return(
      <form className='form' onSubmit={handleSubmission}>
        <div className='input'>
            <h4 htmlFor='source' className='page-align-input'>Source:</h4>
            <input type='text' required id='source' className='input-text-short' ref={sourceInputRef}></input>
            <h4 htmlFor='user-name' className='h4'>User Name:</h4>
            <input type='text' required id='user-name' className='input-text-short' ref={userNameInputRef}></input>
        </div>
        <div className='input'>
          <h4 htmlFor='content' className='h4'>Content:</h4>
          <textarea id='content' className='text-area-for-form' ref={contentInputRef}></textarea>
        </div>
        <div className='input form-input-alignment '>
          <h4 htmlFor='content' className='h4'>Event Date:</h4>
          <div className='date-time-picker-div'>
              <DateTimePicker onChange={onDateChange} value={date}/>
          </div>
          <div className='actions right'>
              <button className='form-btn form-btn-right'>Submit</button>
          </div>
        </div>
        <div>
            {err && <h3>{err}</h3>}
            {isLoading && <LoadingSpinner isSmall={true}/>}
        </div>
        <div className={showResultsDiv ? 'content-show' : 'content-hide'}>
                <h3>Entry was added successfully with the following predictions:</h3>
                {data.map(labels => {
                    return <div>
                      <Prediction labels={labels}/>
                    </div>;
                })}
        </div>
      </form>
    );
}

export default NewDbMonitorForm;