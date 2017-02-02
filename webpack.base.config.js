var webpack = require('webpack');
var path = require('path');

module.exports = {
  target: 'web',

  resolve: {
    root: [
      path.resolve('./client')
    ],
    modulesDirectories: [
      'web_modules',
      'node_modules',
      'client',
      'assets'
    ],
    extensions: ['', '.js', '.jsx', '.scss']
  },

  plugins: [
    new webpack.DefinePlugin({
      NODE_ENV: process.env.NODE_ENV
    }),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery'
    })
  ],

  module: {
    loaders: [
      { test: /\.scss?/, loader: 'style!css!sass' },
      { test: /\.(png|jpg|jpeg)$/, loader: 'file' },
      { test: /\.(ttf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/, loader: 'file' }
    ],
    noParse: /\.min\.js\/node_modules/
  }

};
