# SVD Based Image Compression Website

> This is a web-based image compression done with Singular Value Decomposition Algorithm. An assignment (and exploration media) for IF2123 Linear and Geometry Algebra ITB 2021.

<br>

## Table of Contents

<hr>

- [General Info](#general-information)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Screenshots](#screenshots)
- [Setup](#setup)
- [Usage](#usage)
- [Project Status](#project-status)
- [Room for Improvement](#room-for-improvement)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

<br>
<br>

## General Information

<hr>
Gambar merupakan salah satu media yang penting keberadaannya di dunia modern ini. Sayangnya, gambar, karena ukurannya yang dapat relatif besar, relatif sulit untuk dikirimkan. Kompresi gambar merupakan suatu tipe kompresi data yang dapat dilakukan pada gambar digital. Dengan kompresi gambar, suatu file gambar digital dapat dikurangi ukuran filenya dengan baik tanpa mempengaruhi kualitas gambar secara signifikan.
<br><br>
Singular Value Decomposition merupakan salah satu metode yang dapat digunakan dalam rangka kompresi gambar. Pada tugas besar ini, kami menggunakan algoritma Implicit QL oleh Dubrulle, Martin, dan Wilkinson dalam buku yang dipublikasikan pada tahun 1971 berjudul Handbook for Automatic Computation Linear Algebra Volume II. 
<br><br>
Algoritma yang digunakan adalah algoritma QL (nonimplisit) dengan pergeseran (shift). Pergeseran yang dilakukan untuk mempercepat konvergensi matriks sehingga menurunkan kompleksitas algoritma. Pemilihan pergeseran sebetulnya bisa saja diambil secara bebas karena pada akhirnya akan ditambahkan kembali kecuali jika pergeseran tersebut membuat komponen matriks menjadi nol (cancellation).

<br>

## Technologies Used

<hr>
<ul>
    <li>Python - version 3.9.0</li>
    <li>Pip - version 21.1.1</li>
    <li>fortawesome/free-solid-svg-icons - version ^5.15.4</li>
    <li>fortawesome/react-fontawesome - version ^0.1.16</li>
    <li>material-ui/core - version ^4.12.3</li>
    <li>react-spring/parallax - version ^9.3.0</li>
    <li>react-router-dom - version ^6.0.2</li>
    <li>axios - version ^0.24.0</li>
    <li>bootstrap - version ^5.1.3</li>
    <li>react - version ^17.0.2</li>
    <li>react-bootstrap - version ^2.0.2</li>
    <li>react-bootstrap-range-slider - version ^3.0.3</li>
    <li>react-dom - version ^17.0.2</li>
    <li>react-parallax - version ^3.3.0</li>
    <li>react-rounded-image - version ^2.0.13</li>
    <li>react-scripts - version 4.0.3</li>
    <li>react-scroll-parallax - version ^2.4.0</li>
    <li>react-spring - version ^9.3.0</li>
    <li>simple-react-footer - version ^1.0.2</li>
    <li>styled-components - version ^5.3.3</li>
    <li>use-elapsed-time - version ^3.0.2</li>
    <li>Flask - version 2.0.2</li>
    <li>Flask-Cors - version 3.0.10</li>
    <li>matplotlib - version 3.3.3</li>
    <li>numpy - version 1.19.3</li>
    <li>Pillow - version 8.4.0</li>
</ul>

<br>

## Features

This website contains 3 features, namely:

- Image Compression
- Image Download (post-compression)
- Statistics of compression, including compression time and pixel difference

<br>

## Screenshots

![Home Landing Page](https://drive.google.com/uc?export=view&id=156o0v5kZpVzgeNbfg_1aWxyK19NsMFtH)
![About Landing Page](https://drive.google.com/uc?export=view&id=1rW1zS33jmQp1yCzm_33DhDOryCFU_k5g)
![Contact Landing Page](https://drive.google.com/uc?export=view&id=1G4CIUzDDXKKzeai66TYFI5WuLGBmF5sa)
![Image Compression Page Content](https://drive.google.com/uc?export=view&id=1zUS51dS7amjdQxsVDy3vhYh7VQVXjAgz)
![About Page Content](https://drive.google.com/uc?export=view&id=1E4f3QEyuNKGU8D6rKbxUlSEpdS9Kloor)
![Continued](https://drive.google.com/uc?export=view&id=1yc-ztxp1Ee84GZyvY_HmoWeYMJbL8c9J)
![Contact Us Page Content](https://drive.google.com/uc?export=view&id=1m2GpxIpCOMNGzpO-wxuo_FrKYbJdLxkj)

<br>

## Setup

<hr>
To run this website locally, fork and clone this repository. Before setting up, make sure that you have the dependencies listed above installed. If you have not installed virtual environment, <strong>we encourage you to do so.</strong> This is to prevent changes (not always) to your other projects. Virtual environment will make your projects independent to each other.

1. Install python venv

```
pip install virtualenv
```

2. Create virtualenv

```
virtualenv venv
```

3. Then, activate the virtual environment

```
backend\venv\Scripts\activate
```

4. Install python dependencies

```
pip install -r backend\requirements.txt
```

## If you use yarn

1. You can <strong> change your directory to frontend</strong>, then

```
npm install --global yarn
```

You can use npm too, but the implementation with backend will be quite different.

2. Then with different terminals, type

```
cd src\frontend
yarn start
```

For the frontend terminal and for the backend terminal:

```
cd src\frontend
yarn start-api
```

## If you use npm

1. Make 2 terminal, then in different terminal, do

```
cd src\frontend
npm start
```

```
cd src\backend
py app.py
```

<strong> Do that on different terminal and line by line. </strong>

Then the browser will start and you are all set!

<br>

## Usage

<hr>
To utilize this website, simply press Upload Image button, choose image of yours, and hit OK. After that, Compress button will be activated along with a slider range. Drag left or right the range slider of your need then hit enter! You'll see the time it takes to compress the image you uploaded and the pixel difference. Finally, if you wish to save the image, press 'Download Image'

<br>

## Project Status

<hr>
Project is complete. Improvements may be made.

<br>

## Room for Improvement(s)

<hr>
This image compression website stil can't handle properly PNG formatted image compression. Improvements can be made since this project's output on PNG images still varies to each cases. Furthermore, we believe that there are many ways to search for the singular values. Hence, there might be improvements can be made on the algorithm.

Room for improvement:

- Compression for PNG formatted image
- Algorithm optimization

<br>

## Acknowledgement

<hr>
Great thanks to...

- Our lecturers of IF2123 Linear and Geometry Algebra Course ITB 2021, Mr. Judhi Santoso, Mr. Rinaldi Munir, and Mr. Rila Mandala.
- Course Lab Assistants.
- Our family, especially parents, and friends.

<br>

## Contact

<hr>
Created by Mobilita (Rani, Suryanto, Khelli), 2021. Contacts can be seen on 'Contact Us' page! Feel free to contact! :)
