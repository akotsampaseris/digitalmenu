import React, { Component } from "react";
import { render } from "react-dom";

import ApolloClient from "apollo-boost";
import { ApolloProvider, useMutation } from "@apollo/react-hooks";
import gql from "graphql-tag";

const client = new ApolloClient({
  uri: 'http://localhost:8000/api/',
});

const CREATE_SHOP = gql`
mutation CreateShop($slug: String!){
  createShop(slug: $slug){
      slug
  }
}`;

function CreateShop() {
  let input;
  const [createShop, { data }] = useMutation(CREATE_SHOP);

  return (
    <div>
      <form
        onSubmit={e => {
          e.preventDefault();
          createShop({ variables: { slug: input.value } });
          input.value = '';
        }}
      >
        <input className="input form-input"
          ref={node => {
            input = node;
          }}
        />
        <button className="btn btn-primary" type="submit">Create Shop</button>
      </form>
    </div>
  );
}


class App extends Component {
  render() {
    return (
    <ApolloProvider client={client}>
      <h2>My first apollo app</h2>
      <CreateShop />
    </ApolloProvider>
    );
  }
}

render(<App />, document.getElementById("app"));
