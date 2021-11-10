import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [compressedStatus, setcompressedStatus] = useState(0);
  const [uploadedImage, setuploadedImage] = useState({
    file: [],
    filepreview: null,
  });
  const [loader, setLoader] = useState(0);
  const percent = 50;

  const imgSelectHandler = (event) => {
    setuploadedImage({
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
      axios
        .post("http://127.0.0.1:5000/upload", fd, {
          onUploadProgress: (progressEvent) => {
            setLoader((progressEvent.loaded / progressEvent.total) * 100);
          },
        })
        .then((response) => console.log(response))
        .then(() => dataImage(uploadedImage.file.name, percent))
        .catch((error) => window.alert(error.response.data.error));
    }
  };

  async function dataImage(imgname, percent) {
    try {
      let response = await axios.get(
        `http://localhost:5000/compressed/${imgname}/${percent}`
      );
      setcompressedStatus(1);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <div className="App">
      <div className="container">
        <input className="input-file" type="file" onChange={imgSelectHandler} />
        <button className="btn-upload" onClick={imgUploadHandler}>
          Upload
        </button>
        {uploadedImage.filepreview !== null ? (
          <img
            className="preview-img"
            src={uploadedImage.filepreview}
            alt="uploaded image"
          />
        ) : null}

        {compressedStatus !== 0 ? (
          <img
            src={`http://localhost:5000/compressed/${uploadedImage.file.name}/${percent}`}
            alt="compressed_image"
          />
        ) : null}
      </div>
    </div>
  );
}

export default App;
