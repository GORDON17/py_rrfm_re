import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import promise from 'redux-promise';

// import api from '../middleware/api';   ??????????
import reducers from '../reducers';

const finalCreateStore = compose(
  applyMiddleware(thunk, promise),
  // applyMiddleware(api)
)(createStore);

export default function configureStore(initialState) {
  return finalCreateStore(reducers, initialState);
}
