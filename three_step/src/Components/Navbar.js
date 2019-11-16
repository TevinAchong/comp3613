import React from 'react'
import { Link, NavLink, withRouter} from 'react-router-dom'

const NavBar = (props) =>{
    return(
        <nav className="nav-wrapper red darken-3">
            <div className="container">
                <a className="brand-logo">TwitterLytics(Tentative)</a>
                <ul className="right">
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/second">Second Page</Link></li>
                </ul>
            </div>
        </nav>
    )
}

export default withRouter(NavBar);