import { combineReducers } from 'redux';
// import { team_table_reducer } from './team_reducer'

import team_table_reducer from './team_reducer'

const rootReducer  = combineReducers({
    teamTable: team_table_reducer
  })

export default rootReducer;

