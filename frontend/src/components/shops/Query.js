import gql from 'graphql-tag';

export const SHOPS_LIST_VIEW = gql`
query shopsList{
  allShops{
    edges{
      node{
        name
        slug
      }
    }
  }
}`
