import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const endpoint = "http://127.0.0.1:5000";

  const [compressedStatus, setCompressedStatus] = useState(0);
  const [uploadedImage, setUploadedImage] = useState({
    file: [],
    filepreview: null,
  });
  const [isCompressing, setIsCompressing] = useState(0);
  const [percent, setPercent] = useState(0);
  const [time, setTime] = useState(0);

  const imgSelectHandler = (event) => {
    setUploadedImage({
      ...uploadedImage,
      file: event.target.files[0],
      filepreview: URL.createObjectURL(event.target.files[0]),
    });
  };

  const imgUploadHandler = () => {
    const fd = new FormData();
    fd.append("file", uploadedImage.file);
    if (uploadedImage.file.length === 0) {
      window.alert("Woi upload filenya!!");
    } else {
      setIsCompressing(1);
      axios
        .post(`${endpoint}/upload`, fd)
        .then((response) => console.log(response))
        .then(() => dataImage(uploadedImage.file.name, percent))
        .catch((error) => window.alert(error.response.data.error));
    }
  };

  async function dataImage(imgname, percent) {
    let fetchTime = new Date().getTime();
    console.log(imgname, percent);
    try {
      let response = await axios.get(
        `${endpoint}/compressed/${imgname}/${percent}`
      );
      fetchTime = ((await new Date().getTime()) - fetchTime) / 1000;
      setCompressedStatus(1);
      setIsCompressing(0);
      setTime(fetchTime);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <div className="App">
      <h2 className="title">
        Image Compressor with Singular Value Decomposition
      </h2>
      <div className="body">
        <div className="upload">
          <div className="input-wrapper">
            <div className="file-input">
              <input className="file" type="file" onChange={imgSelectHandler} />
              <button className="btn-upload" onClick={imgUploadHandler}>
                Upload
              </button>
            </div>
            <div className="percent-input">
              <h4>Percentage</h4>
              <input
                className="percent"
                type="number"
                min="0"
                max="100"
                onChange={(e) => setPercent(e.target.value)}
              />
              <h4>%</h4>
            </div>
          </div>
          <div className="loader">
            {isCompressing ? <h3>Compressing... </h3> : null}
            {compressedStatus !== 0 ? (
              <h3>
                Completed in <span className="time">{time}</span> s.
              </h3>
            ) : null}
          </div>
        </div>

        <div className="preview-container">
          {uploadedImage.filepreview !== null ? (
            <img
              className="preview-img"
              src={uploadedImage.filepreview}
              alt="uploaded image"
            />
          ) : null}
          {compressedStatus !== 0 ? (
            <img
              className="preview-img"
              src={`http://localhost:5000/compressed/${uploadedImage.file.name}/${percent}`}
              alt="compressed_image"
            />
          ) : null}
        </div>

        <div className="download-container">
          {compressedStatus !== 0 ? (
            <a
              href={`http://localhost:5000/compressed/${uploadedImage.file.name}/${percent}`}
              target="_blank"
              download
            >
              <button className="download-btn">Download here</button>
            </a>
          ) : null}
        </div>
      </div>
    </div>
  );
}

export default App;
