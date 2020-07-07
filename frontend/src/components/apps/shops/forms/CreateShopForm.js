// IMPORT REACT FUNCTIONALITY
import React, { Component, Fragment } from "react";
import { Link, withRouter } from 'react-router-dom';

// IMPORT FORM FUNCTIONALITY
import { Formik, Form, Field, ErrorMessage } from 'formik';

// DEFINE COMPONENTS
// // CREATE SHOP FORM
function CreateShopForm(props){
  return(
    <Formik
      initialValues={{
          _name: '',
          _slug: '',
          _category: '',
          _location: '',
          _city: '',
          _address1: '',
          _address2: '',
          _postCode: ''
      }}
      onSubmit={(values, { setSubmitting }) => {
        setTimeout(() => {
          props.createShop({
            variables: {
              name: values._name,
              slug: values._slug,
              category: values._category,
              location: values._location,
              city: values._city,
              address1: values._address1,
              address2: values._address2,
              postCode: values._postCode
            }
          });
          props.history.push('/shop/' + values._slug);
          setSubmitting(false);
        }, 400);
      }}
      >
      {({ isSubmitting }) => (
        <Form>
          <table>
            <tbody>
              <tr>
                <td>
                  <label>Slug</label>
                </td>
                <td>
                  <Field type="text" name="_slug" placeholder="Slug"/>
                </td>
              </tr>
              <tr>
                <td>
                <label>Name</label>
                </td>
                <td>
                  <Field type="text" name="_name" placeholder="Name" />
                </td>
              </tr>
              <tr>
                <td>
                <label>Category</label>
                </td>
                <td>
                  <Field type="text" name="_category" placeholder="Category" />
                </td>
              </tr>
              <tr>
                <td>
                <label>Location</label>
                </td>
                <td>
                  <Field type="text" name="_location" placeholder="Location" />
                </td>
              </tr>
              <tr>
                <td>
                <label>City</label>
                </td>
                <td>
                  <Field type="text" name="_city" placeholder="City" />
                </td>
              </tr>
              <tr>
                <td>
                <label>Address 1</label>
                </td>
                <td>
                  <Field type="text" name="_address1" placeholder="Address 1" />
                </td>
              </tr>
              <tr>
                <td>
                <label>Address 2</label>
                </td>
                <td>
                  <Field type="text" name="_address2" placeholder="Address 2" />
                </td>
              </tr>
              <tr>
                <td>
                <label>Post Code</label>
                </td>
                <td>
                  <Field type="text" name="_postCode" placeholder="Post Code" />
                </td>
              </tr>
            </tbody>
          </table>
          <hr></hr>
          <button className="btn btn-primary" type="submit" disabled={isSubmitting}>Create</button>
        </Form>
      )}
      </Formik>
  )
}

export default withRouter(CreateShopForm)
