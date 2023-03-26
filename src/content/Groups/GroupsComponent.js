import React,{useEffect,useState} from 'react'
import './groupscomponent.scss'
import {Link} from 'react-router-dom'
import axios from 'axios'

const GroupsComponent = () => {
  const [groups,setGroups] = useState([])
  const [groupId,setGroupId] = useState(null)
  const [isChange,setIsChange] = useState(false)
  const user = JSON.parse(localStorage.getItem('user')) ?? []
  useEffect(() => {
    axios(`http://127.0.0.1:5000/get-all-group-by-client-id/${user.clientId}`)
      .then(res => {
        setGroups(res.data)
      })
  },[isChange])

  useEffect(() => {
    if(groupId !== null){
      const formData = new FormData()
      formData.append('clientId',user.clientId)
      formData.append('groupId',groupId)
      axios.post('http://127.0.0.1:5000/group-member/delete',formData,{headers: {'Content-Type': 'multipart/form-data' }})
        .then(res => {
          console.log('delete success')
          setIsChange(!isChange)
        })
        .catch(err => {
          console.log('delete fail')
        })
    }
  },[groupId])

  return (
    <div className='groupcomponent'>
    {
      groups.map(item => (
        <div className='groupcomponentbox' key={item.groupId}>
          <div className='groupcomponentItem'>
            <Link to={`/group/${item.groupId}`} className='groupItemImg'>
              <img src={`http://127.0.0.1:5000/img/${item.backgroundImg}`} alt='ptc'/>
            </Link>
            <Link to={`/group/${item.groupId}`} className='groupItemName'>{item.name}</Link>
            <div className='groupItemBtn'>
              <button onClick={() => setGroupId(item.groupId)}>Rời nhóm</button>
            </div>
          </div>
        </div>
      ))
    }
      
      
    </div>
  )
}

export default GroupsComponent