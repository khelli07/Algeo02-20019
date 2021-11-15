import React from "react";

export const Button = ({style, size, onClicked, text, types}) => {
    return(
        <button className={"button ${style} ${size}"} onClick={onClicked} type={types}>
            {text}
        </button>
    )
}