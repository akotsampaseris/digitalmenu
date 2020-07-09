// IMPORT REACT FUNCTIONALITY
import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

// IMPORT APOLLO CLIENT
import client from '../../../../apollo';

// IMPORT GRAPHQL FUNCTIONALITY
import { useMutation } from '@apollo/react-hooks';

// IMPORT QUERIES & MUTATIONS
import { LOGIN_USER } from '../api/UserMutations';

// IMPORT FORMS
import LoginUserForm from '../forms/LoginUserForm';

// EXPORT COMPONENTS
// // LOGIN USER PAGE
const LoginUser = (props) => {
  const [loginUser, { loading, error, data }] = useMutation(LOGIN_USER, {
    onCompleted({ loginUser }){
      localStorage.setItem('auth-token', loginUser),
      client.writeData({ data: { isLoggedIn: true }})
    }
  });

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>

  return (
    <Fragment>
      <h2>Login</h2>
      <hr></hr>
      <LoginUserForm loginUser={loginUser}/>
      <hr></hr>
      <Link to="/register">You don't have an account? Register...</Link>
    </Fragment>
  )
}

export default LoginUser
