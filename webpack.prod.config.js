'use strict';

var path = require('path');
var update = require('react/lib/update');
var webpack = require('webpack');
var config = require('./webpack.base.config.js');
var HtmlWebpackPlugin = require('html-webpack-plugin');
var CleanWebpackPlugin = require('clean-webpack-plugin');

var SCRIPTS_PATH = 'server/static/scripts';
var TEMPLATES_PATH = 'server/templates';

config = update(config, {
  bail: { $set: true },

  entry: { 
    $set: [
      './assets/css/index.scss',
      './client/entry',
      './assets/js/index.js'
    ] 
  },

  debug: { $set: false },

  profile: { $set: false },

  devtool: { $set: '#source-map' },

  output: {
    $set: {
      path: SCRIPTS_PATH,
      pathInfo: true,
      publicPath: '/static/scripts/',
      filename: 'bundle.[hash].min.js'
    }
  },

  plugins: {
    $push: [
      new CleanWebpackPlugin([SCRIPTS_PATH, TEMPLATES_PATH]),
      new webpack.DefinePlugin({
        'process.env': {
          'NODE_ENV': JSON.stringify('production'),
          'SERVER_ENV': JSON.stringify('production'),
          'API_URI': JSON.stringify(process.env.API_URI),
          'RAILS_TOKEN': JSON.stringify(process.env.RAILS_TOKEN)
        }
      }),
      new webpack.optimize.DedupePlugin(),
      new webpack.optimize.UglifyJsPlugin({ 
        comments: false,
        compress: {
          warnings: false
        }
      }),
      new HtmlWebpackPlugin({
        inject: true,
        filename: '../../templates/index.html',
        template: 'client/index.tpl'
      })
    ]
  },

  module: {
    loaders: {
      $push: [
        { test: /\.(js|jsx)?$/, 
          loaders: ['babel'], 
          exclude: /node_modules/
        }
      ]
    }
  }
});

module.exports = config;
