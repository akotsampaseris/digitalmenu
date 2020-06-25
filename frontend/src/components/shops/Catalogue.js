import React, { Fragment } from 'react';
import { useQuery } from '@apollo/react-hooks';
import Query from 'Query';

export default function Catalogue() {
  const { loading, errors, data } = useQuery(Query.SHOPS_LIST_VIEW);
  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>

  return (
    <Fragment>
      <h1>Catalogue</h1>
      {data && data.shopsList && data.shopsList.map(shop=>(
        <div className="shop-card" key={shop.slug}>
        <p className="shop-name">{shop.name}</p>
      )
    )
    }
    </Fragment>
  )
}
