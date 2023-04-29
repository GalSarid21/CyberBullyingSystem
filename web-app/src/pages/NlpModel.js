import { useState } from "react";
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
    body: "This is the free text section"
  },
  {
    title: "Example Tweets",
    body: "This is the example tweets section"
  }
]

export default NlpModelPage;