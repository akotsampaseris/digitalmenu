// IMPORT REACT FUNCTIONALITY
import React, { Component, Fragment } from "react";
import { render } from "react-dom";
import { HashRouter as Router, Route, PrivateRoute, Switch } from 'react-router-dom';

// IMPORT GRAPHQL FUNCTIONALITY
import { ApolloProvider } from "@apollo/react-hooks";
import client from '../apollo';

// IMPORT LAYOUT COMPONENTS
import Header from './layout/Header';
import Footer from './layout/Footer';

// IMPORT APP COMPONENTS
// // NETWORK PAGES
import NotFound from './apps/pages/components/NotFound';

// // USERS
import GetMe from './apps/users/components/GetMe';
import RegisterUser from './apps/users/components/RegisterUser';
import LoginUser from './apps/users/components/LoginUser';
import LogoutUser from './apps/users/components/LogoutUser';

// // SHOPS
import GetShopList from './apps/shops/components/GetShopList';
import GetShop from './apps/shops/components/GetShop';
import CreateShop from './apps/shops/components/CreateShop';
import UpdateShop from './apps/shops/components/UpdateShop';
import DeleteShop from './apps/shops/components/DeleteShop';
import UndeleteShop from './apps/shops/components/UndeleteShop';

// // STATIC PAGES
import Home from './apps/pages/components/Home';
import About from './apps/pages/components/About';
import Services from './apps/pages/components/Services';
import Contact from './apps/pages/components/Contact';

// DEFINE THE APP CLASS
class App extends Component {
  render() {
    return (
    <ApolloProvider client={client}>
      <Router>
        <Fragment>
          <Header />
          <div className="container" style={{paddingTop: "25px",
                                            paddingBottom: "50px",
                                            minHeight: "500px"
                                          }}>
            <Switch>
              // ROUTING
              // // STATIC PAGES
              <Route exact path="/" component={Home} />
              <Route exact path="/about" component={About} />
              <Route exact path="/services" component={Services} />
              <Route exact path="/contact" component={Contact} />

              // // USERS APP
              <Route exact path="/profile" component={GetMe} />
              <Route exact path="/register" component={RegisterUser} />
              <Route exact path="/login" component={LoginUser} />
              <Route exact path="/logout" component={LogoutUser} />

              // // SHOPS APP
              <Route exact path="/catalogue" component={GetShopList} />
              <Route exact path="/shop/:slug" component={GetShop} />
              <Route exact path="/create-shop" component={CreateShop} />
              <Route exact path="/shop/:slug/edit" component={UpdateShop} />
              <Route exact path="/shop/:slug/delete" component={DeleteShop} />
              <Route exact path="/shop/:slug/undelete" component={UndeleteShop} />

              // // NETWORK ENDPOINTS
              <Route component={NotFound} />

            </Switch>
          </div>
        </Fragment>
      </Router>
    </ApolloProvider>
    );
  }
}

render(<App />, document.getElementById("app"));
