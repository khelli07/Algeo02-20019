import React from 'react';
import Box from '@material-ui/core/Box';
import "./About.css"
import LenaOri from "../img/lenaOriginal.png";
import LenaCompressed from "../img/lenaCompressed.png";
import { Parallax } from "react-parallax";
import BgParallaxHome from "../img/bg-scroll3.png";
  
export default function About() {
    const HorizontalLine = ({ color, thickness }) => (
        <hr style={{ color: color, backgroundColor: color, height: thickness}} />
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
                <div style={subStyles}>About This Website</div>
            </div>
        </Parallax>
        <div className="about-body">
            <Box className="about-outer-box">
                <h1 className="about-title">About</h1>
                <HorizontalLine color="teal" thickness="2" />
                <p className="about-exp">This image compression website is made in accordance to 
                    IF2123 Linear and Geometry Algebra course task on Informatics ITB. Any suggestions
                    and constructive critisism are gladly welcomed! </p>
                
                <br/>

                <h3 className="about-subtitle">Image Compression Overview (in Bahasa)</h3>
                <HorizontalLine color="teal" thickness="1" />
                <p className="about-exp">Kompresi gambar merupakan suatu tipe kompresi data yang dapat dilakukan pada gambar digital. Dengan kompresi gambar, suatu file gambar digital dapat dikurangi ukuran filenya dengan baik tanpa mempengaruhi kualitas gambar secara signifikan.</p>
                
                <br/>
                
                <h3 className="about-subtitle">SVD Compression Algorithm Used</h3>
                <HorizontalLine color="teal" thickness="1" />
                <p className="about-exp">Pada tugas besar ini, kami menggunakan algoritma Implicit QL oleh Dubrulle, Martin, dan Wilkinson dalam buku yang dipublikasikan pada tahun 1971 berjudul Handbook for Automatic Computation Linear Algebra Volume II. 
                    Algoritma yang digunakan adalah algoritma QL (nonimplisit) dengan pergeseran (shift). Pergeseran yang dilakukan untuk mempercepat konvergensi matriks sehingga menurunkan kompleksitas algoritma. Pemilihan pergeseran sebetulnya bisa saja diambil secara bebas karena pada akhirnya akan ditambahkan kembali kecuali jika pergeseran tersebut membuat komponen matriks menjadi nol (cancellation). </p>
                
                <br/>
                
                <h3 className="about-subtitle">Example Image</h3>
                <HorizontalLine color="teal" thickness="1" />
                <p className="about-exp">Below shown the well-known original (non-compressed) picture Lena,</p>
                <center><img src={LenaOri} /></center>
                <center><h8><i>Original image</i></h8></center>
                <br/>
                <p className="about-exp">And below, we present you the 50% compressed Lena image</p>
                <center><img src={LenaCompressed} /></center>
                <center><h8><i>Compressed image</i></h8></center>
            </Box>
        </div>
        </>
    );
};