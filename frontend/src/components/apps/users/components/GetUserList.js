// IMPORT REACT FUNCTIONALITY
import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

// IMPORT GRAPHQL FUNCTIONALITY
import { useQuery } from '@apollo/react-hooks';

// IMPORT QUERIES & MUTATIONS
import { GET_USER_LIST } from '../api/UserQueries';

// EXPORT COMPONENT
// // SHOP LIST PAGE
const GetUserList = (props) => {
  const { loading, error, data } = useQuery(GET_USER_LIST);
  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>

  return (
    <Fragment>
      <h1>Users</h1>
      <div className="shop-list">
        <ul className="list-unstyled">
        {data.allUsers.edges.map(edge => {
          const user = edge.node;
          return (
            <li key={user.id}>
              <Link to={`/user/${user.id}`}>{user.firstName} {user.lastName}</Link>
            </li>
          )
        })}
        </ul>
      </div>
      <Link className="btn btn-primary" to="/register">Register</Link>
    </Fragment>
  )
}

export default GetUserList
