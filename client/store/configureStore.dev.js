import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import createLogger from 'redux-logger';
import promise from 'redux-promise';

// import api from '../middleware/api';    ???????????
import reducers from '../reducers';  //??????????

const finalCreateStore = compose(
  applyMiddleware(thunk,
                  promise,
                  createLogger()
                  ),
  // applyMiddleware(api),
)(createStore);

export default function configureStore(initialState) {
  const store = finalCreateStore(reducers, initialState);

  if (module.hot) {
    module.hot.accept('../reducers', () => {
      store.replaceReducer(require('../reducers'));
    });
  }

  return store;
}
