import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';
import Button from '@material-ui/core/Button';
import {Grid} from "@material-ui/core";
import TextField from '@material-ui/core/TextField';
import { teamActions } from '../../../../../actions';
import { connect } from 'react-redux'

const useStyles = makeStyles(theme => ({
  root: {
    '& > *': {
      margin: theme.spacing(4),
    },
  },
}));


class AddMemberForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      memberData:{
              member_id: '',
              first_name: '',
              last_name: '',
              email: '',
              phone: '',
              member_type: '',
            }
    };
  }

  handleSubmit = () => {
    const memberData = this.state.memberData
    console.log(this.state)
    this.props.postTeamMemberData(memberData)
  }

  
  

  // handleChange = (event, v) => {
  //   console.log(event)
  //   console.log(v)
  //   const name = v;
  //   const value= event.target.value

  //   this.setState(() => ({
  //     [name]: value
  //   }))
  //   // console.log(this.state)
  // }

  handleChange = name => ({target:{value}}) => {
    this.setState({
      memberData: {
      ...this.state.memberData,
      [name] : value
      }
    })
  }


  render() {
    return (
      <div>
            <Input type="text" placeholder="Member ID" onChange={this.handleChange('member_id')}/>
            <Input type="text" placeholder="First Name" onChange={this.handleChange('first_name')}/>
            <Input type="text" placeholder="Last Name" onChange={this.handleChange('last_name')}/>
            <Input type="text" placeholder="Email" onChange={this.handleChange('email')}/>
            <Input type="text" placeholder="Phone" onChange={this.handleChange('phone')}/>
            <Input type="text" placeholder="Member Type" onChange={this.handleChange('member_type')}/>
            <Button variant="contained" color="primary" onClick={this.handleSubmit}>Add User</Button>
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
    postTeamMemberData: (memberData) => dispatch(teamActions.post_team_member_table_data(memberData))
  }
}

export default connect(mapStateToProps,mapDispatchToProps)(AddMemberForm);

// export default AddMemberForm