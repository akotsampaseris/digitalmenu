// IMPORT REACT FUNCTIONALITY
import React, { Fragment } from 'react';
import { Route, Redirect } from 'react-router-dom';

// IMPORT APOLLO CLIENT
import client from '../../../../apollo';

// IMPORT GRAPHQL FUNCTIONALITY
import { useMutation } from '@apollo/react-hooks';

// IMPORT QUERIES & MUTATIONS
import { LOGOUT_USER } from '../api/UserMutations';

// EXPORT COMPONENTS
// // CREATE SHOP PAGE
const LogoutUser = (props) => {
  const [logoutUser, { loading, error, data }] = useMutation(LOGOUT_USER, {
    onCompleted({ logoutUser }){
      localStorage.setItem('auth-token', logoutUser);
      client.writeData({ data: { isLoggedIn: false }});
      Route.history.push('/');
    }
  });

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>

  localStorage.removeItem('auth-token')

  return (
    <Fragment>
      <Redirect to="/" />
    </Fragment>
  )
}

export default LogoutUser
