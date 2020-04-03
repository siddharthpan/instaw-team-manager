import { teamConstants } from '../actions/types/team_types'
import { updateObject } from '../utils/utility'


const initialState ={
    team_member_table_get: [],
    team_member_table_post: [],
    team_member_table_put: [],
    team_member_table_delete: [],
    error: null,
    loading: false
    
}
const teamTableStart = ( state, action ) => {
    return updateObject( state, { error: null,loading:true } );
};

const teamTableGetSuccess = (state, action) => {
    console.log(state)
    return updateObject( state, { 
        team_member_table_get: action.response.member_data,
        error: null,
        loading: false
        
     } );
};

const teamTablePostSuccess = (state, action) => {
    console.log(action)
    return updateObject( state, { 
        team_member_table_post: action.response.member_data,
        error: null,
        loading: false
        
     } );
};

const teamTablePutSuccess = (state, action) => {
    console.log(action)
    return updateObject( state, { 
        team_member_table_put: action.response.member_data,
        error: null,
        loading: false
        
     } );
};

const teamTableDeleteSuccess = (state, action) => {
    console.log(action)
    return updateObject( state, { 
        team_member_table_delete: action.response.member_data,
        error: null,
        loading: false
        
     } );
};


const teamTableFail = (state, action) => {
    return updateObject( state, {
        error: action.error,
        loading: false
        
    });
}

const team_table_reducer = ( state = initialState, action ) => {
    switch ( action.type ) {
        case teamConstants.TEAM_TABLE_START: return teamTableStart(state, action);
        case teamConstants.TEAM_TABLE_GET_SUCCESS: return teamTableGetSuccess(state, action);
        case teamConstants.TEAM_TABLE_POST_SUCCESS: return teamTablePostSuccess(state,action);
        case teamConstants.TEAM_TABLE_PUT_SUCCESS: return teamTablePutSuccess(state,action);
        case teamConstants.TEAM_TABLE_DELETE_SUCCESS: return teamTableDeleteSuccess(state,action);
        case teamConstants.TEAM_TABLE_FAIL: return teamTableFail(state, action);
        
        
        default:
            return state;
    }
};

export default team_table_reducer;