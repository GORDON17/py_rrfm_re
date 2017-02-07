import React from 'react';
import { Router, Route, IndexRoute, useRouterHistory } from 'react-router';
import { createHistory } from 'history';

import App from '../containers/App/App';
import Jobs from '../containers/Jobs/Jobs';

const appHistory = useRouterHistory(createHistory)({basename: '', hashType: 'slash'});

export default (
  <Router history={appHistory}>
    <Route path='/' component={App}>
    	{/*<IndexRoute component={Dashboard}/>*/}
      <Route path='jobs' component={Jobs} />
    </Route>
  </Router>
);
