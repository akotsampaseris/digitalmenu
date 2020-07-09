// IMPORT REACT FUNCTIONALITY
import React, { Fragment } from 'react';

// IMPORT APOLLO CLIENT
import client from '../../../../apollo';

// IMPORT GRAPHQL FUNCTIONALITY
import { useMutation } from '@apollo/react-hooks';

// IMPORT QUERIES & MUTATIONS
import { REGISTER_USER } from '../api/UserMutations';

// IMPORT FORMS
import RegisterUserForm from '../forms/RegisterUserForm';

// EXPORT COMPONENTS
// // REGISTER USER PAGE
const RegisterUser = (props) => {
  const [registerUser, { loading, error, data }] = useMutation(REGISTER_USER);

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>
  
  return (
    <Fragment>
      <h2>Register</h2>
      <hr></hr>
      <RegisterUserForm registerUser={registerUser} />

    </Fragment>
  )
}

export default RegisterUser
