'use strict';
import 'babel-polyfill';

import '../assets/css/index.scss';

import '../assets/js/index.js';

import React from 'react';
import ReactDOM from 'react-dom';
import jss from 'jss';
import jssVendorPrefixer from 'jss-vendor-prefixer';
import jssPx from 'jss-px';
import jssNested from 'jss-nested';
import jssCamelCase from 'jss-camel-case';
import { Provider } from 'react-redux';
import { Router, Route } from 'react-router';

import configureStore from './store/configureStore';
import AppRoutes from './routes';

jss.use(jssVendorPrefixer());
jss.use(jssPx());
jss.use(jssNested());
jss.use(jssCamelCase());

const store = configureStore();

ReactDOM.render(
  <Provider store={store}>
    {AppRoutes}
  </Provider>,
  document.getElementById('root')
);
