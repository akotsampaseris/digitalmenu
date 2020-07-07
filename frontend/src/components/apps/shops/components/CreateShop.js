// IMPORT REACT FUNCTIONALITY
import React, { Fragment } from 'react';

// IMPORT GRAPHQL FUNCTIONALITY
import { useMutation } from '@apollo/react-hooks';

// IMPORT QUERIES & MUTATIONS
import { CREATE_SHOP } from '../api/ShopMutations';

// IMPORT FORMS
import CreateShopForm from '../forms/CreateShopForm';

// EXPORT COMPONENTS
// // CREATE SHOP PAGE
const CreateShop = (props) => {
  const [createShop, { loading, error, data }] = useMutation(CREATE_SHOP);

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>

  return (
    <Fragment>
      <h2>Create a new shop</h2>
      <hr></hr>
      <CreateShopForm createShop={createShop} />
    </Fragment>
  )
}

export default CreateShop
