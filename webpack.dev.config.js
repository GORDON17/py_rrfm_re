'use strict';

var path = require('path');
var webpack = require('webpack');
var config = require('./webpack.base.config.js');
var update = require('react/lib/update');
var ExportFilesWebpackPlugin = require('export-files-webpack-plugin');
var HtmlWebpackPlugin = require('html-webpack-plugin');

if (process.env.NODE_ENV !== 'test') {
  config = update(config, {
    entry: {
      $set: [
        'webpack-dev-server/client?http://localhost:8080',
        'webpack/hot/dev-server',
        './assets/css/index.scss',
        './client/entry',
        './assets/js/index.js'
      ]
    }
  });
}

config = update(config, {
  debug: { $set: true },

  profile: { $set: true },

  devtool: { $set: 'eval-source-map' },

  output: {
    $set: {
      path: path.join(__dirname, 'dev/static/scripts'),
      publicPath: '/static/scripts/',
      filename: 'main.js'
    }
  },

  plugins: {
    $push: [
      new webpack.HotModuleReplacementPlugin(),
      new HtmlWebpackPlugin({
        inject: true,
        filename: 'dev/index.html',
        template: 'client/index.tpl'
      }),
      new ExportFilesWebpackPlugin('dev/index.html')
    ]
  },

  module: {
    loaders: {
      $push: [
        { test: /\.(js|jsx)?$/, loaders: [ 'babel' ], exclude: /node_modules/ }
      ]
    }
  },

  devServer: {
    $set: {
      publicPath: '/static/scripts/',

      port: 8080,

      contentBase: './dev',

      inline: true,

      hot: true,

      stats: {
        colors: true
      },

      historyApiFallback: true,

      headers: {
        'Access-Control-Allow-Origin': 'http://localhost:8080',
        'Access-Control-Allow-Headers': 'X-Requested-With'
      },

      proxy: {
        '/api/*': 'http://localhost:8000'
      }
    }
  }
});

module.exports = config;
