import React,{useState,useEffect} from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import './friendrequestcomponent.scss'

const FriendRequestComponent = () => {
  const user = JSON.parse(localStorage.getItem('user')) ?? []
  const [onChange,setOnChange] = useState(false)
  const [friendResponse,setFriendResponse] = useState([])
  const [clientIdDelete,setClientIdDelete] = useState(null)
  const [clientIdConfirm,setClientIdConfirm] = useState(null)
  useEffect(() => {
    axios(`http://127.0.0.1:5000/get-all-friend-by-friend-response/${user.clientId}`)
        .then(res => {
                console.log(res.data)
            setFriendResponse(res.data)
        })
        .catch(err => {
            console.log('err')
        })
  // eslint-disable-next-line
  },[onChange])

  useEffect(() => {
    if(clientIdDelete !== null)
    axios.post('http://127.0.0.1:5000/friend-request-delete',{
      'senderId': clientIdDelete,
      'receiverId': user.clientId
    })
        .then(res => {
          console.log('success')
          setOnChange(!onChange)
        })
        .catch(err => {
          console.log('err')
        })
  // eslint-disable-next-line
  },[clientIdDelete])

  useEffect(() => {
    if(clientIdConfirm!== null)
      axios.post('http://127.0.0.1:5000/friend-request-confirm',{
        'receiverId': user.clientId,
        'senderId': clientIdConfirm
      })
        .then(res => {
          console.log('success')
          setOnChange(!onChange)
        })
        .catch(err => {
          console.log('err')
        })
  // eslint-disable-next-line
  },[clientIdConfirm])


  return (
    <div className='friendcomponentrequest'>
    {
      friendResponse.map(item => (
        <div className='friendcomponentrequestbox' key={item.clientId}>
          <div className='friendcomponentrequestItem'>
            <Link to={`/client/${item.clientId}`} className='friendrequestItemImg'>
              <img src={`http://127.0.0.1:5000/img/${item.avatar}`} alt='ptc'/>
            </Link>
            <Link to={`/client/${item.clientId}`} className='friendrequestItemName'>{item.name}</Link>
            <div className='friendrequestItemBtn' onClick={() => setClientIdConfirm(item.clientId)}>
              <button className='friendrequestItemBtn confirm'>Xác nhận</button>
            </div>
            <div className='friendrequestItemBtn' onClick={() => setClientIdDelete(item.clientId)}>
              <button>Xóa</button>
            </div>
          </div>
        </div>
      ))
    }
  </div>
  )
}

export default FriendRequestComponent