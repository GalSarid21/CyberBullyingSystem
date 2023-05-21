import React from "react";
import classes from "./LoadingSpinner.module.css";

function LoadingSpinner(props) {
  console.log(props.isSmall);
  return (
    <div className={props.isSmall ? classes.spinnerContainerSmall : classes.spinnerContainer}>
      <div className={props.isSmall ? classes.loadingSpinnerSmall : classes.loadingSpinner}>
      </div>
    </div>
  );
}

export default LoadingSpinner;