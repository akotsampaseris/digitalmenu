// IMPORT REACT FUNCTIONALITY
import React, { Component, Fragment } from "react";
import { Link, withRouter } from 'react-router-dom';

// IMPORT FORM FUNCTIONALITY
import { Formik, Form, Field, ErrorMessage } from 'formik';

// DEFINE COMPONENTS
// // DELETE SHOP FORM
function DeleteShopForm(props) {
  return(
    <Formik
      onSubmit={(values, { setSubmitting }) => {
        setTimeout(() => {
          props.deleteShop({
            variables: {
              slug: props.shop.slug
            }
          });
          props.history.push('/catalogue');
          setSubmitting(false);
        }, 400);
      }}
      >
      {({ isSubmitting }) => (
        <Form>
          <h2>You are about to delete {props.shop.name}. Proceed?</h2>
          <hr></hr>
          <button className="btn btn-success" type="submit" disabled={isSubmitting}>Confirm</button>
          &nbsp;
          <Link className="btn btn-danger" to={`/shop/${props.shop.slug}`}>Cancel</Link>
        </Form>
      )}
      </Formik>
  )
}

export default withRouter(DeleteShopForm)
