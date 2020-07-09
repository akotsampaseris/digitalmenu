// IMPORT REACT FUNCTIONALITY
import React, { Component, Fragment } from "react";
import { Link, withRouter } from 'react-router-dom';

// IMPORT FORM FUNCTIONALITY
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';

// DEFINE COMPONENTS
// // VALIDATION SCHEMA
const CreateShopSchema = Yup.object().shape({
    _name: Yup.string()
          .min(2, 'Too short!')
          .max(50, 'Too long!')
          .required('Required!'),
    _slug: Yup.string()
          .min(2, 'Too short!')
          .max(50, 'Too long!')
          .required('Required!')
})

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
      validationSchema={CreateShopSchema}
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
      {({ isSubmitting, errors, touched }) => (
        <Form>
          <table>
            <tbody>
              <tr>
                <td>
                  <label>Slug</label>
                </td>
                <td>
                  <Field type="text" name="_slug" placeholder="Slug"/>
                  { errors._slug && touched._slug ? (
                    <div className="text-danger">
                      <small>{errors._slug}</small>
                    </div>
                  ) : null }
                </td>
              </tr>
              <tr>
                <td>
                <label>Name</label>
                </td>
                <td>
                  <Field type="text" name="_name" placeholder="Name" />
                  { errors._name && touched._name ?(
                    <div className="text-danger">
                      <small>{errors._name}</small>
                    </div>
                  ) : null }
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
