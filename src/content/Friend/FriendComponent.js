import React,{useState,useEffect} from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import './friendcomponent.scss'

const FriendComponent = () => {
  const user = JSON.parse(localStorage.getItem('user')) ?? []
  const [friends,setFriends] = useState([])
  const [onChange,setOnChange] = useState(false)
  const [clientId,setClientId] = useState(null)
  useEffect(() => {
    axios(`http://127.0.0.1:5000/get-all-friend-by-client-id/${user.clientId}`)
      .then(res => {
        setFriends(res.data)
        console.log(res.data)
      })
      .catch(err => {
        console.log('err')
      })
  // eslint-disable-next-line
  },[onChange])

  useEffect(() => {
    if(clientId !== null){
      axios.post('http://127.0.0.1:5000/friend-delete',{
        'client1': user.clientId,
        'client2': clientId
      })
        .then(res => {
          console.log('success')
          setOnChange(!onChange)
        })
        .catch(res => {
          console.log('err')
        })

    }
  // eslint-disable-next-line
  },[clientId])

  return (
    <div className='friendcomponent'>
    {
      friends.map(item => (
        <div className='friendcomponentbox' key={item.clientId}>
          <div className='friendcomponentItem'>
            <Link to={`/client/${item.clientId}`} className='friendItemImg'>
              <img src={`http://127.0.0.1:5000/img/${item.avatar}`} alt='ptc'/>
            </Link>
            <Link to={`/client/${item.clientId}`} className='friendItemName'>{item.name}</Link>
            <div className='friendItemBtn' onClick={() => setClientId(item.clientId)}>
              <button>Xóa, gỡ bỏ</button>
            </div>
          </div>
        </div>
      ))
    }
    </div>
  )
}

export default FriendComponent