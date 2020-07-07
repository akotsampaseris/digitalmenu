// IMPORT REACT FUNCTIONALITY
import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

// IMPORT GRAPHQL FUNCTIONALITY
import { useQuery } from '@apollo/react-hooks';

// IMPORT QUERIES & MUTATIONS
import { GET_SHOP_LIST } from '../api/ShopQueries';

// EXPORT COMPONENT
// // SHOP LIST PAGE
const GetShopList = (props) => {
  const { loading, error, data } = useQuery(GET_SHOP_LIST);
  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>

  return (
    <Fragment>
      <h1>Catalogue</h1>
      <div className="shop-list">
        <ul className="list-unstyled">
        {data.allShops.edges.map(edge => {
          const shop = edge.node;
          return (
            <li key={shop.slug}>
              { shop.isActive &&
              <Link to={`/shop/${shop.slug}`}>{shop.name}</Link>
              }
            </li>
          )
        })}
        </ul>
      </div>
      <Link className="btn btn-primary" to="/create-shop">Create Shop</Link>
    </Fragment>
  )
}

export default GetShopList
