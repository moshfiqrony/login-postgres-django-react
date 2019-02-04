import React from 'react'
import axios from 'axios'



class Users extends React.Component{
    constructor(){
        super()
        this.state = {
            users: []
        }

        
    }

    async componentDidMount(){
        await axios.get('http://127.0.0.1:8000/getbyid/')
        .then(response => {
            const result = response.data
            this.setState({ users: result })
        })
        
    }


    render() {
        return(
            <div style={{marginTop: 50}}>
                
                <div>
                <table id="t01">
                    <tr>
                        <th>ID</th>
                        <th>Username</th>
                        <th>Email</th>
                        <th>Password</th> 
                    </tr>

                    {this.state.users.map((user) => {
                        return(<tr>
                            <td>{user.id}</td>
                            <td>{user.username}</td>
                            <td>{user.email}</td>
                            <td>{user.password}</td>
                        </tr>)
                    })}
                    
                    </table>
                    
                </div>
            </div>
        )
    }

}

export default Users