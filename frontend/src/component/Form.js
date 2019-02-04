import React from 'react'
import axios from 'axios'


class Form extends React.Component{
    constructor(){
        super()
        this.state = {
            username: '',
            email: '',
            password: '',
        }

        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    handleChange(e){

        const {name, value} = e.target
        this.setState({
            [name]: value
        })
    }

    handleSubmit(e){
        e.preventDefault()
        console.log(this.state)
        const username = e.target.elements.username.value
        const password = e.target.elements.password.value
        const email = e.target.elements.email.value
        axios.post('http://127.0.0.1:8000/getbyid/',
            {
                username: username,
                password: password,
                email: email
            })
            .then(response => console.log(response))

    }


    render() {
        return(
            <div>
                <form onSubmit={this.handleSubmit}>
                    <input
                        type='text'
                        name='username'
                        placeholder='Enter Username *'
                        onChange={this.handleChange}
                        value={this.state.username}
                    />
                    <input
                        type='email'
                        name='email'
                        placeholder='Enter Email *'
                        onChange={this.handleChange}
                        value={this.state.email}
                    />
                    <input
                        type='password'
                        name='password'
                        placeholder='Enter Password *'
                        onChange={this.handleChange}
                        value={this.state.password}
                    />
                    <input
                        type='submit'
                        name='submit'
                        value='Register'
                    />
                </form>
                <div>

                </div>
            </div>
        )
    }

}

export default Form