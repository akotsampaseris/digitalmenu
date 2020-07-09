// IMPORT GRAPHQL FUNCTIONALITY
import gql from 'graphql-tag';


// EXPORT QUERIES
// GET USER LIST QUERY
export const GET_USER_LIST = gql`
query userList{
    allUsers{
        edges{
            node{
                id,
                email,
                firstName,
                lastName
            }
        }
    }
}`

// GET USER QUERY
export const GET_ME = gql`
query me{
  me{
    id,
    email,
    firstName,
    lastName,
    isActive
  }
}`
