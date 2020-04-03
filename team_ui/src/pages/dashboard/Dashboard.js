import React, { useState } from "react";
import {
  Grid,
} from "@material-ui/core";
import { useTheme } from "@material-ui/styles";
import MaterialTable from 'material-table'

// styles
import useStyles from "./styles";

// components
import Widget from "../../components/Widget";
import PageTitle from "../../components/PageTitle";
import TeamMemberTable from "./components/Table/Table"

export default function Dashboard(props) {
  var classes = useStyles();
  var theme = useTheme();

  return (
    <>
      <PageTitle title="Team Manager"/>
      <Grid container spacing={4}>
        <Grid item lg={12} md={12} sm={12} xs={12}>
            <TeamMemberTable />
        </Grid>
      </Grid>
    </>
  );
}
