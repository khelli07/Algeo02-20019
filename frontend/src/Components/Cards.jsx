import React from "react";
import axios from "axios";
import { useState } from "react";
import Card from "react-bootstrap/Card";
import "./Cards.css";
import 'react-bootstrap-range-slider/dist/react-bootstrap-range-slider.css';
import RangeSlider from 'react-bootstrap-range-slider';
import { CardGroup, Form, Row, Col } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import UpImage from "../img/fa-fa-cloud-upload-alt.png"
import DownImage from "../img/fa-fa-cloud-download-alt.png"
import { useElapsedTime } from "use-elapsed-time";

export default function Cards() {
    const endpoint = "http://127.0.0.1:5000";

    const [compressedStatus, setCompressedStatus] = useState(0);
    const [uploadImage, setUploadImage] = useState(false);
    const [uploadedImage, setUploadedImage] = useState({
        file: "",
        filepreview: "",
    });
    const [isPlaying, setIsPlaying] = useState(false);
    const { elapsedTime } = useElapsedTime({isPlaying});
    const [percent, setPercent] = useState(50);

    const fileInput = React.useRef(null);

    const imgUploadHandler = (event) => {
        fileInput.current.click();
    };

    const imgSelectHandler = (event) => {
        setUploadedImage({
            file: event.target.files[0],
            filepreview: URL.createObjectURL(event.target.files[0]),
        });
        setUploadImage(true);
    };

    const imgCompressCaller = () => {
        const fd = new FormData();
        fd.append("file", uploadedImage.file);
        axios.post(`${endpoint}/upload`, fd)
            .then((response) => console.log(response))
            .then(() => dataImage(uploadedImage.file.name, percent))
            .catch((error) => window.alert(error.response.data.error));
    };
    
    async function dataImage(imgname, percent) {
        setIsPlaying(true);
        console.log(imgname, percent);
        try {
            let response = await axios.get(
                `${endpoint}/compressed/${imgname}/${percent}`
            );
            setCompressedStatus(1);
            setIsPlaying(false);
        } catch (error) {
            console.log(error);
        }
    };

    return(
        <>
            <div className="uploadImage">
                <CardGroup>
                    <div className="w-50 p-3 h-100 d-inline-block">
                        <Card className="cardColoring flex-fill border-0">
                            <Card.Body>
                                <Card.Title className="cardTitle">Before</Card.Title>
                            </Card.Body>
                            {uploadImage ? (
                                <Card.Img className="upImage" src={uploadedImage.filepreview}>
                                </Card.Img>
                            ) : (
                                <Card.Img className="UpCloudImage" src={UpImage}>
                                </Card.Img>
                            )}
                            <div className="d-flex justify-content-center upload-btn-wrapper">
                                <Button className="upDownBtn" variant="contained" onClick={imgUploadHandler}>Upload an image</Button>
                                    <input id="upload-file"
                                        type="file"
                                        accept="image/*"
                                        ref={fileInput}
                                        style={{display:'none'}}
                                        onChange={imgSelectHandler}
                                        >
                                    </input>
                            </div>
                        </Card>
                    </div>
                    <div className="w-50 p-3 h-100 d-inline-block">
                        <Card className="cardColoring flex-fill border-0">
                            <Card.Body>
                                <Card.Title className="cardTitle">After</Card.Title>
                            </Card.Body>
                            {(compressedStatus !== 0) ? (
                                <Card.Img className="downImage" src={`http://localhost:5000/compressed/${uploadedImage.file.name}/${percent}`}>
                                </Card.Img>
                            ) : (
                                <Card.Img className="downCloudImage" src={DownImage}>
                                </Card.Img>
                            )}
                            <div className="d-flex justify-content-center upload-btn-wrapper">
                                {uploadImage ? (
                                    <a href={`http://localhost:5000/compressed/${uploadedImage.file.name}/${percent}`} target="_blank" download >
                                        <Button className="upDownBtn" variant="contained" onClick="">Download image</Button>
                                    </a>
                                ) : ( <></> )}
                            </div>
                        </Card>
                    </div>
                </CardGroup>
            </div>
            <div className="text-image-compression-rate">
            {uploadImage ? (
                <h5>Image Compression Rate</h5>
            ) : ( <></> )}
            </div>
            <div className="range-slider d-flex justify-content-center upload-btn-wrapper">
                {uploadImage ? (
                    <Form>
                        <Form.Group as={Row}>
                            <Col lg="9">
                                <RangeSlider value={percent} onChange={e => setPercent(e.target.value)}/>
                            </Col>
                            <Col lg="3" className="numer-comp-rate">
                                <Form.Control value={percent}/>
                            </Col>
                        </Form.Group>
                    </Form>
                ) : ( <></> )}
            </div>
            <div className="d-flex justify-content-center upload-btn-wrapper">
                {uploadImage ? (
                    <Button onClick={imgCompressCaller} className="compress-button">Compress!</Button>
                ) : ( <></> )}
            </div>
            <div className="timer">
                {uploadImage ? (
                    <h5>Time elapsed: {elapsedTime.toFixed(2)} s</h5>
                ) : ( <></> )}
            </div>
        </>
    );
}