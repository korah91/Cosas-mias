import React, {Component   } from 'react'

class Table extends Component{
    render(){
        return (
            <table>
                <thead>
                    <tr>
                        <tr>Name</tr>
                        <tr>Job</tr>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Charlie</td>
                        <td>Janitor</td>
                    </tr>
                    <tr>
                        <td>Mac</td>
                        <td>Bouncer</td>
                    </tr>
                    <tr>
                        <td>Dee</td>
                        <td>Dennis</td>
                    </tr>
                </tbody>
            </table>
        )
    }
}
export default Table