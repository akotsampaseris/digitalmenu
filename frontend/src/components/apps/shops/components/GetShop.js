// IMPORT REACT FUNCTIONALITY
import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

// IMPORT GRAPHQL FUNCTIONALITY
import { useQuery } from '@apollo/react-hooks';

// IMPORT QUERIES & MUTATIONS
import { GET_SHOP } from '../api/ShopQueries';

// EXPORT COMPONENTS
// // GET SHOP PAGE
const GetShop = (props) => {
  const urlParams = props.match.params;
  const { loading, error, data } = useQuery(GET_SHOP, {
    variables: {slug: urlParams.slug}
  });
  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>
  const shop = data.shop;

  return (
    <Fragment>
      <h2>{shop.name}</h2>
      <hr></hr>
      <p>Category: {shop.category}</p>
      <p>Location: {shop.location}</p>
      <p>City: {shop.city}</p>
      <p>Address 1: {shop.address1}</p>
      <p>Address 2: {shop.address2}</p>
      <p>Post Code: {shop.postCode}</p>
      <hr></hr>
      <Link className="btn btn-primary" to={`/shop/${shop.slug}/edit`}>Edit Shop</Link>
      &nbsp;
      <Link className="btn btn-danger" to={`/shop/${shop.slug}/delete`}>Delete Shop</Link>
    </Fragment>
  )
}

export default GetShop
