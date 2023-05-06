import classes from './Prediction.module.css'

function Prediction(props) {
    return <div>
        <button className={props.labels.toxic ? classes.toggleTrue : classes.toggleFalse}>
            {'toxic'}
        </button>
        <button className={props.labels.severe_toxic ? classes.toggleTrue : classes.toggleFalse}>
            {'severe toxic'}
        </button>
        <button className={props.labels.obscene ? classes.toggleTrue : classes.toggleFalse}>
            {'obscene'}
        </button>
        <button className={props.labels.threat ? classes.toggleTrue : classes.toggleFalse}>
            {'threat'}
        </button>
        <button className={props.labels.insult ? classes.toggleTrue : classes.toggleFalse}>
            {'insult'}
        </button>
        <button className={props.labels.identity_hate ? classes.toggleTrue : classes.toggleFalse}>
            {'identity hate'}
        </button>
    </div>;
}

export default Prediction;