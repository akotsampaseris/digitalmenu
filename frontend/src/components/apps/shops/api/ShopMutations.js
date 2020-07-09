// IMPORT GRAPHQL FUNCTIONALITY
import gql from 'graphql-tag';


// EXPORT MUTATIONS
// // CREATE SHOP MUTATION
export const CREATE_SHOP = gql`
mutation createShop(
  $slug: String!,
  $name: String!,
  $category: String!,
  $location: String!,
  $city: String!,
  $address1: String!,
  $address2: String!,
  $postCode: String!
){
  createShop(
    shopData: {
      slug: $slug,
      name: $name,
      category: $category,
      location: $location,
      city: $city,
      address1: $address1,
      address2: $address2,
      postCode: $postCode
    }
  ){
    shop{
      id,
      slug,
      name
    }
  }
}
`

// // UPDATE SHOP MUTATION
export const UPDATE_SHOP = gql`
mutation updateShop(
    $slug: String!,
    $name: String!,
    $category: String!,
    $location: String!,
    $city: String!,
    $address1: String!,
    $address2: String!,
    $postCode: String!
){
  updateShop(
    shopData: {
      slug: $slug,
      name: $name,
      category: $category,
      location: $location,
      city: $city,
      address1: $address1,
      address2: $address2,
      postCode: $postCode
    }
  ){
    shop{
      id, slug, name
    }
  }
}
`

// // DELETE SHOP MUTATION
export const DELETE_SHOP = gql`
mutation deleteShop($slug: String!){
  deleteShop(slug: $slug){
    shop{
      id
      slug
      isActive
    }
  }
}
`
