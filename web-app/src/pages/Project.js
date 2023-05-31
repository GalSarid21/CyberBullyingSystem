import Typewriter from "typewriter-effect";
import classes from './Project.module.css'

const printSentences = [
    '<b>About the project:</b><br>',
    '&emsp;Our project aims to develop a robust and accurate NLP model that can effectively identify instances of cyberbullying in<br>&emsp;social media environments. By analyzing text data, our model, a <i><b>DistilBERT</b></i> implementation, enables the identification<br>&emsp;of cyberbullying content, providing valuable insights for users, social media companies, and other stakeholders.<br><br>',
    '<b>Our dataset consists the following labels:</b><br>',
    '&emsp;1. <i>Toxic:</i> This label refers to content that contains language or behavior intended to harm, insult, or provoke a<br>&emsp;negative emotional response from others. Toxic comments can include abusive or offensive language, personal<br>&emsp;attacks, or derogatory statements targeting individuals or groups.<br><br>',
    '&emsp;2. <i>Severe Toxic:</i> The "severe toxic" label signifies content that goes beyond general toxicity and exhibits an extremely &emsp;harmful or malicious nature. These comments may involve highly offensive language, explicit threats, or explicit and<br>&emsp;violent content meant to intimidate or cause significant distress to the recipient.<br><br>',
    '&emsp;3. <i>Threat:</i> The "threat" label is assigned to comments containing explicit or implicit threats towards individuals or<br>&emsp;groups. Such comments may include intentions of physical harm, violence, or any form of danger expressed towards<br>&emsp;the target.<br><br>',
    '&emsp;4. <i>Obscene:</i> Comments labeled as "obscene" contain explicit, vulgar, or sexually explicit content. This category includes<br>&emsp;profanity, sexually explicit language, or any form of content that violates social norms and standards of decency.<br><br>',
    '&emsp;5. <i>Identity Hate:</i> The "identity hate" label pertains to comments that display prejudice, discrimination, or hatred based<br>&emsp;on an individual\'s race, religion, ethnicity, gender, sexual orientation, or any other protected characteristic. These<br>&emsp;comments target a person or group\'s identity and aim to demean or express hostility based on those characteristics.<br><br>',
    '&emsp;6. <i>Insult:</i> The "insult" label is assigned to comments that contain language or behavior intended to offend, belittle, or<br>&emsp;humiliate others. These comments often involve personal attacks, mockery, or derogatory remarks aimed at<br>&emsp;undermining someone\'s intelligence, appearance, abilities, or other aspects of their identity.<br><br>'
]

function ProjectPage() {
    return(
        <div className={classes.fullWidth}>
            <h2 className={classes.projectTitle}>Hi, We're Eden and Gal and this our final project!</h2>
            <Typewriter 
                onInit={(typewriter) => {

                    printSentences.map(sentence => {
                        typewriter = typewriter.typeString(sentence).pause(1000);
                        return null;
                    });
                    typewriter.start();
                }}
                options={{
                    delay: 20,
                  }}
            />
        </div>
    );
}

export default ProjectPage;