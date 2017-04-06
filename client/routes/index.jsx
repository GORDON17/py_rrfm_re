import React from 'react';
import { Router, Route, IndexRoute, useRouterHistory } from 'react-router';
import { createHistory, createBrowserHistory } from 'history';

import App from '../containers/App/App';
import Jobs from '../containers/Jobs/Jobs';
import Dashboard from '../containers/Dashboard/Dashboard';
// might want to use createBrowserHistory with forceRefresh: false
const appHistory = useRouterHistory(createHistory)({basename: '', hashType: 'slash'});
// const appHistory = useRouterHistory(createBrowserHistory)({basename: '', forceRefresh: false});

export default (
  <Router history={appHistory}>
    <Route path='/' component={App}>
    	<IndexRoute component={Dashboard}/>
    	<Route path='dashboard' component={Dashboard} />
      <Route path='jobs' component={Jobs} />
    </Route>
  </Router>
);
