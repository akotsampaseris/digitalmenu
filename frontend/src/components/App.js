import React, { Component, Fragment } from "react";
import { render } from "react-dom";
import { HashRouter as Router, Route, Switch, Redirect } from 'react-router-dom';

import { ApolloProvider, useQuery, useMutation } from "@apollo/react-hooks";
import client from '../client';

import { Provider } from 'react-redux';
import store from '../store';

// Layout Import //
import Header from './layout/Header';

// Pages Import //
import Home from './pages/Home';

// Shops Import //
import Catalogue from './shops/Catalogue';


class App extends Component {
  render() {
    return (
    <Provider store={store}>
      <ApolloProvider client={client}>
        <Router>
          <Fragment>
          <Header />
          <div className="container">
          <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/catalogue" component={Catalogue} />
          </Switch>
          </div>
          </Fragment>
        </Router>
      </ApolloProvider>
    </Provider>
    );
  }
}

render(<App />, document.getElementById("app"));
