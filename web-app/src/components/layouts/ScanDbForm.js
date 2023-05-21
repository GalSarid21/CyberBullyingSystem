import { useRef, useState } from "react";
import LoadingSpinner from "../LoadingSpinner";
import './ScanDbForm.css';

function ScanDbForm() {

    const userNameInputRef = useRef();
    const alertEmailInputRef = useRef();
    const maxHatePerHourInputRef = useRef();
    const maxHatePerDayInputRef = useRef();
    const maxHatePerWeekInputRef = useRef();
    const maxHatePerMonthInputRef = useRef();

    const [isLoading, setIsLoading] = useState(false);
    const [err, setErr] = useState('');

    const handleSubmission = async (event) => {
        event.preventDefault();
        setErr('');
        setIsLoading(true);

        const newScanData = {
            'userName': userNameInputRef.current.value,
            'alertEmail': alertEmailInputRef.current.value,
            'maxHatePerHour': maxHatePerHourInputRef.value,
            'maxHatePerDay': maxHatePerDayInputRef.value,
            'maxHatePerWeek': maxHatePerWeekInputRef.value,
            'maxHatePerMonth': maxHatePerMonthInputRef.value
          }

        try {
            const url = 'http://localhost:5000/api/'
            const response = await fetch(url, {
                method: 'POST',
                body: JSON.stringify(newScanData),
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
        finally {
            setIsLoading(false);
        }
    }

    return(
        <form className='form' onSubmit={handleSubmission}>
            <div className='input'>
                <h4 htmlFor='user-name' className='h4'>User Name:</h4>
                <input type='text' required id='user-name' className='scan-input' ref={userNameInputRef}></input>
                <h4 htmlFor='alert-email' className='h4'>Alet Email:</h4>
                <input type='text' required id='alert-email' className='scan-input' ref={alertEmailInputRef}></input>
            </div>
            <h2 className='scan-h2'>Scan Rules:</h2>
            <div className='input'>
                    <h4 htmlFor='hour' className='h4'>Max hate per hour:</h4>
                    <input type='text' required id='hour' className='scan-input-short hour' ref={maxHatePerHourInputRef}></input>
                    <h4 htmlFor='day' className='h4'>Max hate per day:</h4>
                    <input type='text' required id='day' className='scan-input-short day' ref={maxHatePerDayInputRef}></input>
                </div>
                <div className='input'>
                    <h4 htmlFor='week' className='h4'>Max hate per week:</h4>
                    <input type='text' required id='week' className='scan-input-short week' ref={maxHatePerWeekInputRef}></input>
                    <h4 htmlFor='month' className='h4'>Max hate per month:</h4>
                    <input type='text' required id='month' className='scan-input-short month' ref={maxHatePerMonthInputRef}></input>
                </div>
                <div className='actions'>
                    <button className='form-btn'>Scan</button>
                </div>
            <div>
                {err && <h3>{err}</h3>}
                {isLoading && <LoadingSpinner isSmall={true}/>}
            </div>
      </form>
    );
}

export default ScanDbForm;