// IMPORT REACT FUNCTIONALITY
import React, { Fragment } from 'react';

// IMPORT GRAPHQL FUNCTIONALITY
import { useQuery, useMutation } from '@apollo/react-hooks';

// IMPORT QUERIES & MUTATIONS
import { GET_SHOP } from '../api/ShopQueries';
import { DELETE_SHOP } from '../api/ShopMutations';

// IMPORT FORMS
import DeleteShopForm from '../forms/DeleteShopForm';

// EXPORT COMPONENTS
// // DELETE SHOP PAGE
const UndeleteShop = (props) => {
  const urlParams = props.match.params;
  const { loading, error, data } = useQuery(GET_SHOP, {
    variables: { slug: urlParams.slug }
  });
  const [deleteShop] = useMutation(DELETE_SHOP);

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>
  const shop = data.shop;
  deleteShop({variables:{slug: shop.slug}})
  return(
    <Fragment>
      {shop.isActive}
    </Fragment>
  )
}

export default UndeleteShop
