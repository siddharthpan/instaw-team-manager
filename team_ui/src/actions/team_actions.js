import { teamConstants } from './types'

import axios from 'axios'

export const teamActions = {
    get_team_member_table_data,
    post_team_member_table_data,
    put_team_member_table_data,
    delete_team_member_table_data,
};

function get_team_member_table_data() {
    return dispatch => {
            dispatch(request());
            console.log(`http://localhost:8008/team-manager/api/v1/team_manager/manage_member/`)
            axios.get(`http://localhost:8008/team-manager/api/v1/team_manager/manage_member/`)
            .then(response => {
                    // console.log(response)
                    dispatch(table_success(response.data))
                    console.log("API fetch success")
                })
                .catch( error => {
                    console.log(error)
                    dispatch(failure(error.response.data.message))
                })
    }
    
    function request(response) { return { type: teamConstants.TEAM_TABLE_START, response} }
    function table_success(response) { return { type: teamConstants.TEAM_TABLE_GET_SUCCESS, response } }
    function failure(error) { return { type: teamConstants.TEAM_TABLE_FAIL, error } }
}

function post_team_member_table_data(data) {
    return dispatch => {
            dispatch(request(data));
            console.log(`http://localhost:8008/team-manager/api/v1/team_manager/manage_member/`, data)
            axios.post(`http://localhost:8008/team-manager/api/v1/team_manager/manage_member/`, data)
            .then(response => {
                    // console.log(response)
                    dispatch(table_success(response.data))
                    console.log("API fetch success")
                })
                .catch( error => {
                    console.log(error)
                    dispatch(failure(error.response.data.message))
                })
    }
    
    function request(response) { return { type: teamConstants.TEAM_TABLE_START, response} }
    function table_success(response) { return { type: teamConstants.TEAM_TABLE_POST_SUCCESS, response } }
    function failure(error) { return { type: teamConstants.TEAM_TABLE_FAIL, error } }
}

function put_team_member_table_data(data) {
    return dispatch => {
            dispatch(request(data));
            console.log(`http://localhost:8008/team-manager/api/v1/team_manager/manage_member/`, data)
            axios.put(`http://localhost:8008/team-manager/api/v1/team_manager/manage_member/`, data)
            .then(response => {
                    // console.log(response)
                    dispatch(table_success(response.data))
                    console.log("API fetch success")
                })
                .catch( error => {
                    console.log(error)
                    dispatch(failure(error.response.data.message))
                })
    }
    
    function request(response) { return { type: teamConstants.TEAM_TABLE_START, response} }
    function table_success(response) { return { type: teamConstants.TEAM_TABLE_PUT_SUCCESS, response } }
    function failure(error) { return { type: teamConstants.TEAM_TABLE_FAIL, error } }
}

function delete_team_member_table_data(data) {
    return dispatch => {
            dispatch(request(data));
            console.log(`http://localhost:8008/team-manager/api/v1/team_manager/manage_member/`)
            axios.delete(`http://localhost:8008/team-manager/api/v1/team_manager/manage_member/`, {data: data})
            .then(response => {
                    // console.log(response)
                    dispatch(table_success(response.data))
                    console.log("API fetch success")
                })
                .catch( error => {
                    console.log(error)
                    dispatch(failure(error.response.data.message))
                })
    }
    
    function request(response) { return { type: teamConstants.TEAM_TABLE_START, response} }
    function table_success(response) { return { type: teamConstants.TEAM_TABLE_DELETE_SUCCESS, response } }
    function failure(error) { return { type: teamConstants.TEAM_TABLE_FAIL, error } }
}