import {Link} from 'react-router-dom'

import classes from './MainNavigation.module.css'

function MainNavigation() {
    return (
        <header className={classes.header}>
            <div className={classes.logo}>Online bullying detection using NLP model</div>
            <nav>
                <ul>
                    <li>
                        <Link to='/'>About The Project</Link>
                    </li>
                    <li>
                        <Link to='/nlp-model'>NLP Model</Link>
                    </li>
                    <li>
                        <Link to='/reports'>Reports</Link>
                    </li>
                    <li>
                        <Link to='/alerts'>Alerts</Link>
                    </li>
                </ul>
            </nav>
        </header>
    );
}

export default MainNavigation;