import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Footer extends Component {
  render() {
    return (
      <footer className="footer bg-info">
        <div className="container p-4">
          <div className="row text-white">
            <div className="col-6">
              <p className="text-justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            </div>
            <div className="col">
              <div className="text-center">
                <h5>Links</h5>
                <ul className="list-unstyled">
                  <li className="list-item">
                    <a className="text-white" href="#">Item</a>
                  </li>
                  <li className="list-item">
                    <a className="text-white" href="#">Item</a>
                  </li>
                  <li className="list-item">
                    <a className="text-white" href="#">Item</a>
                  </li>
                  <li className="list-item">
                    <a className="text-white" href="#">Item</a>
                  </li>
                  <li className="list-item">
                    <a className="text-white" href="#">Item</a>
                  </li>
                </ul>
              </div>
            </div>
            <div className="col">
              <h5>Links 2</h5>
              <ul className="list-unstyled">
                <li className="list-item">
                  <a className="text-white" href="#">Item 2</a>
                </li>
                <li className="list-item">
                  <a className="text-white" href="#">Item 2</a>
                </li>
                <li className="list-item">
                  <a className="text-white" href="#">Item 2</a>
                </li>
                <li className="list-item">
                  <a className="text-white" href="#">Item 2</a>
                </li>
                <li className="list-item">
                  <a className="text-white" href="#">Item 2</a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div className="footer-bottom text-light bg-primary p-3">
          <div className="row">
            <div className="col">
              © 2020 Copyright: &nbsp;
              <Link to="/" className="text-white" href="#">
                Digital Menu Ltd.
              </Link>
            </div>
            <div className="col text-center">
              <Link to="/">
                <img src="https://www.digitalmenu.gr/wp-content/uploads/2017/03/digitalmenu-logo.png" alt="DigitalMenu" />
              </Link>
            </div>
            <div className="col text-right">
              Designed & Developed by &nbsp;
              <a className="text-white" target="_blank" href="https://thenegativeentropy.com">
                <img src="" alt="theNegativeEntropy" />
              </a>
            </div>
          </div>
        </div>
      </footer>
    );
  }
}

export default Footer;
