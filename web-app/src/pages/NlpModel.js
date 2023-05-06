import { useState } from "react";
import CollapsibleContent from "../components/CollapsibleContent";
import CollapsibleInputContent from "../components/CollapsibleInputContent";
import classes from "../components/layouts/Accordion.module.css"

function NlpModelPage() {

  const [selected, setSelected] = useState(null);

  const toggle = (i) => {
    if (selected === i) {
      return setSelected(null);
    }

    setSelected(i);
  }

    return (
        <section>
            <h1>NLP Model Page</h1>
            <div className={classes.accordion}>
              {data.map((item, i) => (
                <div className={classes.item}>
                  <div className={classes.title} onClick={() => toggle(i)}>
                    <h2 className={classes.titletext}>{item.title}</h2>
                    <span>{selected === i ? '-' : '+'}</span>
                  </div>
                  <div className={selected === i ? classes.contentshow : classes.content}>
                    {item.body}
                  </div>
                </div>
              ))}
            </div>
        </section>
    );
}

const data = [
  {
    title: "Free Text",
    body: <CollapsibleInputContent/>
  },
  {
    title: "Example Tweets",
    body: <CollapsibleContent />
  }
]

export default NlpModelPage;