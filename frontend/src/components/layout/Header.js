// IMPORT REACT FUNCTIONALITY
import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Header extends Component {
  render() {
    return (
      <nav className="navbar navbar-expand-lg navbar-dark bg-info sticky-top">
        <div className="container">
          <Link className="navbar-brand" to="/">
            <img src="" alt="DigitalMenu" />
          </Link>
          <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>

          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <Link className="nav-item nav-link text-white" to="/catalogue">Shops</Link>
            <Link className="nav-item nav-link text-white" to="/about">About</Link>
            <Link className="nav-item nav-link text-white" to="/services">Services</Link>
            <Link className="nav-item nav-link text-white" to="/contact">Contact</Link>
            { localStorage.getItem('auth-token')
              ? <>
                <Link className="nav-item nav-link text-white" to="/profile">Profile</Link>
                <Link className="nav-item nav-link text-white" to="/logout">Logout</Link>
                </>
              : <Link className="nav-item nav-link text-white" to="/login">Login</Link>
            }
          </div>
        </div>
      </nav>

    );
  }
}

export default Header;
