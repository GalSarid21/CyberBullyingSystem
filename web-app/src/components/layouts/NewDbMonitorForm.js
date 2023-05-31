import { useRef, useState } from 'react';
import LoadingSpinner from '../LoadingSpinner';
import Prediction from '../Prediction';
import DateTimePicker from 'react-datetime-picker';
import './NewDbMonitorForm.css';
import 'react-datetime-picker/dist/DateTimePicker.css';
import 'react-calendar/dist/Calendar.css';
import 'react-clock/dist/Clock.css';

function NewDbMonitorForm(props) {
    
    const sourceInputRef = useRef();
    const userNameInputRef = useRef();
    const contentInputRef = useRef();

    const [showResultsDiv, setShowResultsDiv] = useState(false);
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
          const preds = await props.onFormSubmission(
            sourceInput, userNameInput, contentInput, date
          );

          const url = 'http://localhost:5000/api/hate-monitors/add'
          const response = await fetch(url, {
              method: 'POST',
              body: JSON.stringify(preds[0]),
              headers: {
                  Accept: 'application/json',
              },
          });

          if (!response.ok) {
            throw new Error(`Error! status: ${response.status}`);
          }
          
          setData(preds);
          setShowResultsDiv(true);
        }
        catch(err) {
          setErr(err.message);
        }
        finally {
          setIsLoading(false);
        }
    }
    
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