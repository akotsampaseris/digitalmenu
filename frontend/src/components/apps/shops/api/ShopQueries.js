// IMPORT GRAPHQL FUNCTIONALITY
import gql from 'graphql-tag';


// EXPORT QUERIES
// GET SHOP LIST QUERY
export const GET_SHOP_LIST = gql`
query shopList{
    allShops{
        edges{
            node{
                id,
                isActive,
                slug,
                name,
            }
        }
    }
}`

// GET SHOP QUERY
export const GET_SHOP = gql`
query shop($slug: String!){
  shop(slug: $slug)  {
    id,
    isActive,
    slug,
    name,
    category,
    location,
    city,
    address1,
    address2,
    postCode
  }
}`
