import {Link} from 'react-router-dom';
import { useState } from "react";
import classes from './MainNavigation.module.css';

function MainNavigation() {
    const [aboutTheProjectState, setAboutTheProjectState] = useState(0);
    const [dbManagementState, setDbManagementState] = useState(0);
    const [nlpModelState, setNlpModelState] = useState(0);
    
    const toggleLink = (page) => {
        
        switch(page) {
            case Page.AboutTheProject: {
                setAboutTheProjectState(1);
                setDbManagementState(0);
                setNlpModelState(0);
                break;
            }
            case Page.DbManagement: {
                setAboutTheProjectState(0);
                setDbManagementState(1);
                setNlpModelState(0);
                break;
            }
            case Page.NlpModel: {
                setAboutTheProjectState(0);
                setDbManagementState(0);
                setNlpModelState(1);
                break;
            }
            default: {
                throw new Error('Invalid page!');;
            }
        }
    };
    
    return (
        <header className={classes.header}>
            <div className={classes.logo}>Online Bullying Detection Using NLP Model</div>
            <nav>
                <ul>
                    <li>
                        <Link 
                            to='/' 
                            className={aboutTheProjectState === 1 ? classes.active : ''}
                            onClick={() => toggleLink(Page.AboutTheProject)}
                        >
                            About The Project
                        </Link>
                    </li>
                    <li>
                        <Link 
                            to='/nlp-model'
                            className={nlpModelState === 1 ? classes.active : ''}
                            onClick={() => toggleLink(Page.NlpModel)}
                        >
                            NLP Model
                        </Link>
                    </li>
                    <li>
                        <Link 
                            to='/db-management'
                            className={dbManagementState === 1 ? classes.active : ''}
                            onClick={() => toggleLink(Page.DbManagement)}
                        >
                            DB Management
                        </Link>
                    </li>
                </ul>
            </nav>
        </header>
    );
}

const Page = {
	AboutTheProject: 0,
	NlpModel: 1,
	DbManagement: 2
}

export default MainNavigation;