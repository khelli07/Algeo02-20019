import React from "react";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navigationbar from "./Components/NavigationBar";
import Home from "./Components/Home";
import About from "./Components/About";
import ContactUs from "./Components/ContactUs";
import Footer from "./Components/Footer";

export default function App() {
    return (
        <>
            <Router>
                <Navigationbar/>
                <Routes>
                    <Route path='/' element={<Home/>} />
                    <Route path='/about' element={<About/>}/>
                    <Route path='/contactus' element={<ContactUs/>}/>
                </Routes>
                <Footer />
            </Router>
        </>
    );
}