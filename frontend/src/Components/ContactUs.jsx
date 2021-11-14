import React, { Component, useState } from 'react';
import Box from '@material-ui/core/Box';
import "./ContactUs.css"
import { Parallax, ParallaxLayer } from "@react-spring/parallax";
import NoOne from "../img/1.png";
import NoTwo from "../img/2.png";
import NoThree from "../img/3.png";
import BgScroll from "../img/bg-scroll2.png";
import MaharaniAyu from "../img/MaharaniAyu.jpg";
import SuryantoTan from "../img/SuryantoTan.jpg";
import MariaKhelli from "../img/MariaKhelli.jpg";
import ReactRoundedImage from "react-rounded-image";
import { Card, CardGroup } from "react-bootstrap";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEnvelope } from '@fortawesome/free-solid-svg-icons';

export default function ContactUs() {
    const HorizontalLine = ({ color, thickness }) => (
        <hr style={{ color: color, backgroundColor: color, height: thickness}} />
    );

    return (
        <>
            <Parallax pages={2} style={{ top: "0", left: "0" }}>
                <ParallaxLayer offset={0} speed={0.3}>
                    <img src={BgScroll} style={{width: "100%"}}/>
                    <div className="contact-us-body">
                        <Box className="contact-us-outer-box">
                            <h1 className="contact-us-title">Contact Us</h1>
                            <h4 className="contact-us-subtitle"><i>Our Team</i></h4>
                            
                            <HorizontalLine color="teal" thickness="3" />
                            <p>Consists of three second-year ITB student majoring in Informatics striving and sparing
                                our best efforts to make this project realized with ❤️ for approximately 2 weeks!
                            </p>
                            <br/>
                            <CardGroup>
                                <Card className="cardColor border-0">
                                    <center><ReactRoundedImage image={MaharaniAyu} imageWidth="150" imageHeight="150" roundedColor="#D3E4CD" hoverColor="#99A799" /></center>
                                    <Card.Body>
                                        <Card.Title><b>Maharani Ayu Putri Irawan</b></Card.Title>
                                        <Card.Subtitle>13520019</Card.Subtitle>
                                        <div className="icon-style">
                                            <a href="mailto:13520019@std.stei.itb.ac.id">
                                                <FontAwesomeIcon icon={faEnvelope} size="2x"/>          
                                            </a>
                                        </div>
                                    </Card.Body>
                                </Card>
                                <Card className="cardColor border-0">
                                    <center><ReactRoundedImage image={SuryantoTan} imageWidth="150" imageHeight="150" roundedColor="#D3E4CD" hoverColor="#99A799" /></center>
                                    <Card.Body>
                                        <Card.Title><b>Suryanto Tan</b></Card.Title>
                                        <Card.Subtitle>13520059</Card.Subtitle>
                                        <div className="icon-style">
                                            <a href="mailto:13520059@std.stei.itb.ac.id">
                                                <FontAwesomeIcon icon={faEnvelope} size="2x"/>          
                                            </a>
                                        </div>
                                    </Card.Body>
                                </Card>
                                <Card className="cardColor border-0">
                                    <center><ReactRoundedImage image={MariaKhelli} imageWidth="150" imageHeight="150" roundedColor="#D3E4CD" hoverColor="#99A799" /></center>
                                    <Card.Body>
                                        <Card.Title><b>Maria Khelli</b></Card.Title>
                                        <Card.Subtitle>13520115</Card.Subtitle>
                                        <div className="icon-style">
                                            <a href="mailto:13520115@std.stei.itb.ac.id">
                                                <FontAwesomeIcon icon={faEnvelope} size="2x"/>          
                                            </a>
                                        </div>
                                    </Card.Body>
                                </Card>
                            </CardGroup>
                        </Box>
                    </div>
                </ParallaxLayer>
                <ParallaxLayer offset={0.1} speed={0.15}>
                    <img src={NoThree} style={{width: "100%" }}/>
                </ParallaxLayer>
                <ParallaxLayer offset={0.1} speed={0.56}>
                    <img src={NoTwo} style={{width: "100%" }}/>
                </ParallaxLayer>
                <ParallaxLayer offset={0.3} speed={0.08}>
                    <img src={NoOne} style={{width: "100%" }}/>
                </ParallaxLayer>
            </Parallax>
            
        </>
    );
};