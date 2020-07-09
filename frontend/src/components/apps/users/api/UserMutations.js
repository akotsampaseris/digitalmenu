// IMPORT GRAPHQL FUNCTIONALITY
import gql from 'graphql-tag';


// EXPORT MUTATIONS
// // REGISTER USER MUTATION
export const REGISTER_USER = gql`
mutation registerUser(
  $email: String!,
  $password: String!
){
  registerUser(
    userData: {
      email: $email,
      password: $password
    }
  ){
    user{
      id,
      email
    }
  }
}
`

// // LOGIN USER MUTATION
export const LOGIN_USER = gql`
mutation loginUser(
  $email: String!,
  $password: String!
){
  tokenAuth(
    email: $email,
    password: $password
  ){
    token
  }
}
`

export const LOGOUT_USER = gql`
  mutation LogoutUser($refreshToken: String!){
    revokeToken(refreshToken: $refreshToken){
      revoked
    }
  }
`

// // CREATE USER MUTATION
export const CREATE_USER = gql`
mutation createUser(
  $email: String!,
  $firstName: String!,
  $lastName: String!
){
  createUser(
    userData: {
      email: $email,
      firstName: $firstName,
      lastName: $lastName
    }
  ){
    user{
      id,
      email,
      firstName,
      lastName
    }
  }
}
`

// // UPDATE USER MUTATION
export const UPDATE_USER = gql`
mutation updateUser(
    $email: String!,
    $firstName: String!,
    $lastName: String!
){
  updateUser(
    userData: {
      email: $email,
      firstName: $firstName,
      lastName: $lastName
    }
  ){
    user{
      id,
      email,
      firstName,
      lastName
    }
  }
}
`

// // DELETE USER MUTATION
export const DELETE_USER = gql`
mutation deleteUser($email: String!){
  deleteUser(email: $email){
    user{
      id
    }
  }
}
`

// // UNDELETE USER MUTATION
export const UNDELETE_USER = gql`
mutation undeleteUser($email: String!){
  undeleteUser(email: $email){
    user{
      id
    }
  }
}
`
