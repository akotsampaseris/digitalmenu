// IMPORT REACT FUNCTIONALITY
import React, { Component, Fragment } from "react";
import { render } from "react-dom";
import { HashRouter as Router, Route, Switch } from 'react-router-dom';

// IMPORT GRAPHQL FUNCTIONALITY
import { ApolloProvider } from "@apollo/react-hooks";
import client from '../apollo';

// IMPORT LAYOUT COMPONENTS
import Header from './layout/Header';
import Footer from './layout/Footer';

// IMPORT APP COMPONENTS
// // NETWORK PAGES
import NotFound from './apps/pages/components/NotFound';

// // STATIC PAGES
import Home from './apps/pages/components/Home';
import About from './apps/pages/components/About';
import Services from './apps/pages/components/Services';
import Contact from './apps/pages/components/Contact';

// // SHOPS
import GetShopList from './apps/shops/components/GetShopList';
import GetShop from './apps/shops/components/GetShop';
import CreateShop from './apps/shops/components/CreateShop';
import UpdateShop from './apps/shops/components/UpdateShop';
import DeleteShop from './apps/shops/components/DeleteShop';

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

              // // SHOPS APP
              <Route exact path="/catalogue" component={GetShopList} />
              <Route exact path="/shop/:slug" component={GetShop} />
              <Route exact path="/create-shop" component={CreateShop} />
              <Route exact path="/shop/:slug/edit" component={UpdateShop} />
              <Route exact path="/shop/:slug/delete" component={DeleteShop} />

              // // NETWORK ENDPOINTS
              <Route component={NotFound} />

            </Switch>
          </div>
          <Footer />
        </Fragment>
      </Router>
    </ApolloProvider>
    );
  }
}

render(<App />, document.getElementById("app"));
