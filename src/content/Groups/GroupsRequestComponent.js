import React,{useState,useEffect} from 'react'
import axios from 'axios'
import './groupsrequestcomponent.scss'
import {Link} from 'react-router-dom'

const GroupsRequestComponent = () => {
  const user = JSON.parse(localStorage.getItem('user')) ?? []
  const [groupRequest,setGroupRequest] = useState([])
  const [onChange,setOnChange] = useState(false)
  const [groupId,setGroupId] = useState(null)
  useEffect(() => {
    axios(`http://127.0.0.1:5000/get-all-group-by-group-request/${user.clientId}`)
      .then(res => {
        setGroupRequest(res.data)
        console.log(res.data)
        console.log('success')
      })
      .catch(err => {
        console.log('err')
      })
  },[onChange])

  useEffect(() => {
    if(groupId !== null){
      axios.post('http://127.0.0.1:5000/group-request-delete',{
        'clientId': user.clientId,
        'groupId': groupId
      })
        .then(res => {
          console.log('delete success')
          setOnChange(!onChange)
          setGroupId(null)
        })
        .catch(err => {
          console.log('delete fail')
        })
    }
  },[groupId])

  return (
    <div className='grouprequestcomponent'>
    {
      groupRequest.map(item => (
        <div className='grouprequestcomponentbox' key={item.groupId}>
          <div className='grouprequestcomponentItem'>
            <Link to={`/group/${item.groupId}`} className='grouprequestItemImg'>
              <img src={`http://127.0.0.1:5000/img/${item.backgroundImg}`} alt='ptc'/>
            </Link>
            <Link to={`/group/${item.groupId}`} className='grouprequestItemName'>{item.name}</Link>
            <div className='grouprequestItemBtn' onClick={() => setGroupId(item.groupId)}>
              <button>Hủy yêu cầu tham gia nhóm</button>
            </div>
          </div>
        </div>
      )
      )
    }

      

      
      
    </div>
  )
}

export default GroupsRequestComponent