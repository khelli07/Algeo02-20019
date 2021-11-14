import React, { useState, useEffect } from "react";
import { Container, Nav, Navbar } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.css";
import "./NavigationBar.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGamepad } from "@fortawesome/free-solid-svg-icons";

export function Navigationbar() {
  return (
    <>
      <Navbar
        collapseOnSelect
        fixed="top"
        expand="sm"
        variant="dark"
        className="navbar"
      >
        <Container>
          <Navbar.Brand href="./" className="navbar-team">
            <FontAwesomeIcon
              className="fas fa-gamepad"
              icon={faGamepad}
              size={1}
            />{" "}
            Mobilita
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav" />
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="ml-auto">
              <Nav.Link href="/about">
                <span className="choices">About</span>
              </Nav.Link>
              <Nav.Link href="/contactus">
                <span className="choices">Contact Us</span>
              </Nav.Link>
              <Nav.Link href="https://github.com/khelli07/Algeo02-20019">
                <span className="choices">Github Repo</span>
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </>
  );
}

export default Navigationbar;
