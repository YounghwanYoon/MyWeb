import React from 'react';
import UserList from '../containers/project-list';
import UserDetails from '../containers/user-detail';
require('../../scss/style.scss');

const App = () => (
    <div class = "sidenav">
        <div id = "leftPanel">
            <h2 id ='leftPanel_Title'>Project List:</h2>
            <UserList />
        </div> 
        <div id ="rightPanel">
            <h2>User Details</h2>
            <UserDetails />
        </div>
    </div>
);

export default App;
