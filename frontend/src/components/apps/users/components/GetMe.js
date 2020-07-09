// IMPORT REACT FUNCTIONALITY
import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

// IMPORT GRAPHQL FUNCTIONALITY
import { useQuery } from '@apollo/react-hooks';

// IMPORT QUERIES & MUTATIONS
import { GET_ME } from '../api/UserQueries';

// EXPORT COMPONENTS
// // GET ME PAGE
const GetMe = (props) => {
  const urlParams = props.match.params;
  const { loading, error, data } = useQuery(GET_ME);
  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>
  const me = data.me;

  return (
    <Fragment>
      <h2>{me.firstName} {me.lastName}</h2>
      <hr></hr>
      <p>e-mail: {me.email}</p>
      <hr></hr>
      <Link className="btn btn-primary" to="/user/edit">Edit User</Link>
      &nbsp;
      <Link className="btn btn-danger" to="/user/delete">Delete User</Link>
    </Fragment>
  )
}

export default GetMe
