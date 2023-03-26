import React,{useState,useEffect} from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import './friendresponsecomponent.scss'


const FriendResponseComponent = () => {
    const user = JSON.parse(localStorage.getItem('user')) ?? []
    const [onChange,setOnChange] = useState(false)
    const [friendRequest,setFriendRequest] = useState([])
    const [clientId,setClientId] = useState(null)

    useEffect(() => {
        axios(`http://127.0.0.1:5000/get-all-friend-by-friend-request/${user.clientId}`)
            .then(res => {
                console.log(res.data)
                setFriendRequest(res.data)
            })
            .catch(err => {
                console.log('err')
            })
    // eslint-disable-next-line
    },[onChange])

    useEffect(() => {
        if(clientId !== null){
            axios.post('http://127.0.0.1:5000/friend-request-delete',{
                'senderId': user.clientId,
                'receiverId': clientId
            })
                .then(res => {
                    setOnChange(!onChange)
                    console.log('success')
                })
                .catch(err => {
                    console.log('err')
                })
        }
    // eslint-disable-next-line
    },[clientId])

  return (
    <div className='friendrequestcomponent'>
    {
        friendRequest.map(item => (
            <div className='friendrequestcomponentbox' key={item.clientId}>
                <div className='friendrequestcomponentItem'>
                    <Link to={`/client/${item.clientId}`} className='friendrequestItemImg'>
                        <img src={`http://127.0.0.1:5000/img/${item.avatar}`} alt='ptc'/>
                    </Link>
                    <Link to={`/client/${item.clientId}`} className='friendrequestItemName'>{item.name}</Link>
                    <div className='friendrequestItemBtn' onClick={() => setClientId(item.clientId)}>
                        <button>Xóa</button>
                    </div>
                </div>
            </div>
        ))
    }
  </div>
  )
}

export default FriendResponseComponent