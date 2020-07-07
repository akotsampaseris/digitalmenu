// IMPORT REACT FUNCTIONALITY
import React, { Fragment } from 'react';
import { Link, Redirect } from 'react-router-dom';

// IMPORT GRAPHQL FUNCTIONALITY
import { useQuery, useMutation } from '@apollo/react-hooks';

// IMPORT QUERIES & MUTATIONS
import { GET_SHOP } from '../api/ShopQueries';
import { UPDATE_SHOP } from '../api/ShopMutations';

// IMPORT FORMS
import UpdateShopForm from '../forms/UpdateShopForm';

// EXPORT COMPONENT
// // UPDATE SHOP PAGE
const UpdateShop = (props) => {
  const urlParams = props.match.params;
  const { loading, error, data } = useQuery(GET_SHOP, {
    variables: { slug: urlParams.slug }
  });
  const [updateShop] = useMutation(UPDATE_SHOP);

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>
  const shop = data.shop;

  return (
    <Fragment>
      <h2>Update shop info</h2>
      <hr></hr>
      <UpdateShopForm shop={shop} updateShop={updateShop} />
    </Fragment>
  )
}

export default UpdateShop
