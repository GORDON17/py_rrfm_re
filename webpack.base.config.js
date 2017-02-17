'use strict';

var webpack = require('webpack');
var path = require('path');

module.exports = {
  target: 'web',

  resolve: {
    modulesDirectories: [
      'node_modules'
    ],
    extensions: ['', '.js', '.jsx', '.scss']
  },

  plugins: [
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      Immutable: 'immutable'
    })
  ],

  module: {
    loaders: [
      { test: /\.scss?/, loader: 'style!css!sass' },
      { test: /\.(png|jpg|jpeg)$/, loader: 'file' },
      { test: /\.(ttf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/, loader: 'file' }
    ],
    noParse: /node_modules\/dist\/dev\/static\/server/
  }

};
