import React, {useState, useEffect, useContext} from 'react'
import AuthContext from '../context/AuthContext'

const HomePage = () => {
    let [letters, setLetters] = useState([])
    let {authTokens, logoutUser} = useContext(AuthContext)

    useEffect(()=> {
        getLetters()
    }, [])


    let getLetters = async() =>{
        let response = await fetch('http://127.0.0.1:8000/api/letters/', {
            method:'GET',
            headers:{
                'Content-Type':'application/json',
                'Authorization':'Bearer ' + String(authTokens.access)
            }
        })
        let data = await response.json()

        if(response.status === 200){
            setLetters(data)
        }else if(response.statusText === 'Unauthorized'){
            logoutUser()
        }

    }

    return (
        <div>
            <ul>
                {letters.map(letter => (
                    <li key={letter.id} >{letter.body}</li>
                ))}
            </ul>
        </div>
    )
}

export default HomePage