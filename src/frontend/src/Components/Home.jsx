import React from "react";
import './Home.css';
import Cards from "./Cards";
import Box from '@material-ui/core/Box';
import { Parallax } from "react-parallax";
import BgParallaxHome from "../img/bg-scroll2.png";

export default function Home() {
    const HorizontalLine = ({ color }) => (
        <hr style={{ color: color, backgroundColor: color, height: 2}} />
    );

    const subStyles = {
        background: "#FEF5ED",
        color: "teal",
        padding: 20,
        position: "absolute",
        top: "50%",
        left: "50%",
        transform: "translate(-50%,-50%)",
        fontSize: "2rem",
        fontFamily: 'Homemade Apple',
    };

    return (
        <>
            <Parallax bgImage={BgParallaxHome} strength={window.innerHeight}>
                <div style={{ height: window.innerHeight }}>
                    <div style={subStyles}>Image Compressor</div>
                </div>
            </Parallax>
            <div className="body">
                <Box className="outer-box">
                    <h1 className="title">Image Compressor</h1>
                    <h4 className="subtitle">Upload your image!</h4>
                    <HorizontalLine color="teal" />
                    <Cards/>
                </Box>
            </div>
        </>
    );
}