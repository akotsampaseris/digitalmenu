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
function LoginUserForm(props){
  return(
    <Formik
      initialValues={{
        _email: '',
        _password: '',
      }}
      onSubmit={(values, { setSubmitting }) => {
        setTimeout(() => {
          props.loginUser({
            variables: {
              email: values._email,
              password: values._password,
            }
          });
          props.history.push('/profile');
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
                  <label>E-mail</label>
                </td>
                <td>
                  <Field type="text" name="_email" placeholder="E-mail"/>
                </td>
              </tr>
              <tr>
                <td>
                <label>Password</label>
                </td>
                <td>
                  <Field type="password" name="_password" placeholder="Password" />
                </td>
              </tr>
            </tbody>
          </table>
          <hr></hr>
          <button className="btn btn-primary" type="submit" disabled={isSubmitting}>Login</button>
        </Form>
      )}
      </Formik>
  )
}

export default withRouter(LoginUserForm)
