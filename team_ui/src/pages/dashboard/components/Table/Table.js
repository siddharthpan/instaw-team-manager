import React, { Component } from 'react';

import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import {Grid} from "@material-ui/core";
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import TextField from '@material-ui/core/TextField';


// import { FormControlLabel, Button, FormGroup, Input} from '@material-ui/core';
// import MUIDataTable from "mui-datatables";
import MaterialTable from "material-table";
import { createMuiTheme, MuiThemeProvider, withStyles } from '@material-ui/core/styles';
import {connect} from "react-redux";
// import { inventoryActions } from '../../../../actions'

import { teamActions } from '../../../../actions'

import axios from 'axios'
import AddMemberForm from './components/AddMemberForm'

class TeamMemberTable extends Component {
  constructor(props) {
    super(props);
    this.state = {
      vendor: "",
      discount: "",
      onClick: props.onClick,
      icon: props.icon,
      ModalOpen: false,
      memberData: {
        member_id: ''
      }
    };
  }
  
    componentDidMount() {
        this.props.getTeamMemberData()
        // console.log()
    }

    // handleSubmit = (data) => {
    //   // let vendor = state.vendor
    //   // let discount = state.discount
    //   axios.post(`http://localhost:8008/team-manager/api/v1/team_manager/manage_member/`, data)
    //          .then(response => {
    //               console.log("Discount percentage Update Success")
    //               console.log(response)
    //               // if (response.status = 200){
    //               //   handleSnackbarOpen()
    //               // }
    //           })
    //           .catch( error => {
    //               console.log(error)
    //           })
    // };

      handleChange = (event,v) => {
      // console.log("called")
      const name = v;
      const value= event.target.value
      console.log(event.target.value)
  
      this.setState(() => ({
        [name]: value
      }))
    }

    handleMemberDataChange = name => ({target:{value}}) => {
      this.setState({
        memberData: {
        ...this.state.memberData,
        [name] : value
        }
      })
    }

    handleClose = (event) => {
      this.setState({ ModalOpen: false })
      this.props.getTeamMemberData()
    }

    handleDelete = (member_id) => {
      const memberData = {"member_id": member_id}
      console.log(memberData)
      this.props.deleteTeamMemberData(memberData)
      this.props.getTeamMemberData()
    }


    render() {
      const columns = [
        {
         field: "member_id",
         title: "Member ID",
         editable: "never"
        },
         {
          field: "first_name",
          title: "First Name",
          editable: 'onUpdate',
         },
         {
          field: "last_name",
          title: "Last Name",
          editable: "onUpdate"
         },
         {
          field: "email",
          title: "Email",
          editable: "onUpdate"
         }, 
         {
          field: "phone",
          title: "Phone",
          editable: "onUpdate"
         }, 
         {
          field: "member_type",
          title: "Member Type",
          editable: "onUpdate"
         }, 
         
       ];

       const actions = [ 
        {
          icon: 'refresh',
          tooltip: 'Refresh Table',
          isFreeAction: true,
          onClick: () => this.props.getTeamMemberData(),
        },
        {
          icon: 'add',
          tooltip: 'Add Member',
          isFreeAction: true,
          onClick: (event) => this.setState({ ModalOpen: true })
        },
        {
          icon: 'delete',
          tooltip: 'Delete User',
          onClick: (event, rowData) => this.handleDelete(rowData.member_id)
        }
    ];


        return (
            <div>
              {this.state.ModalOpen && 
                <div>
                <Dialog
                  open={this.state.ModalOpen}
                  onClose={this.handleClose}
                  aria-labelledby="alert-dialog-title"
                  aria-describedby="alert-dialog-description"
                  maxWidth = "xs"
                >
                  <DialogTitle id="alert-dialog-title">{"Add Member"}</DialogTitle>
                      <AddMemberForm />
                  </Dialog>
              </div>
              } 
              <MaterialTable
                title={"Members"}
                data = {this.props.tabledata}
                columns={columns}
                actions = {actions}
                options = {{
                    search:true,
                    actionsColumnIndex: -1,
                    enableRowDelete: true
                    // searchFieldAlignment:"left"
                }}
                editable={{
                  // isEditable: rowData => rowData.name === "discount_perc", // only name(a) rows would be editable
                  onRowUpdate: (newData, oldData) =>
                      new Promise((resolve, reject) => {
                        let vendor = newData.name
                        let discount = newData.discount_perc
                        axios.put(`http://localhost:8008/team-manager/api/v1/team_manager/manage_member/`, newData)
                          .then(response => {
                              console.log("Team Member Update Success")
                              console.log(response)
                              // if (response.status = 200){
                              //   handleSnackbarOpen()
                              // }
                          })
                          .catch( error => {
                              console.log(error)
                          })
                          
                          .then((response) => {
                            return this.props.getTeamMemberData()
                        })
                        .then(response => {
                        resolve({
                            data: this.props.tabledata
                        })
                        })

                          }),
              }}


              />
            </div>
        );
    }
}

const mapStateToProps = state =>{
  // console.log(state.inventory.vendor_discount)
  return {
    tabledata: state.teamTable.team_member_table_get,
  }
}

const mapDispatchToProps = dispatch => {
  return {
    getTeamMemberData: () => dispatch(teamActions.get_team_member_table_data()),
    deleteTeamMemberData: (member_id) => dispatch(teamActions.delete_team_member_table_data(member_id))
  }
}

export default connect(mapStateToProps,mapDispatchToProps)(TeamMemberTable);

