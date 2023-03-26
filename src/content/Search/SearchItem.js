import React from 'react'
import { useState,useEffect } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import './search.scss'

//joined
//send request
//not-join
const SearchItem = ({item}) => {
    const user = JSON.parse(localStorage.getItem('user')) ?? []
    const [status,setStatus] = useState('not-join')
    const [onClick,setOnClick] = useState(false)
    const [isJoined,setIsJoined] = useState(false)

    useEffect(() => {
        axios.post('http://127.0.0.1:5000/find-group-member-by-client-id',{
            'clientId': user.clientId,
            'groupId': item.groupId 
        })
            .then(res => {
                setStatus('joined')
            })
            .catch(err => {
                axios.post('http://127.0.0.1:5000/find-group-request-by-client-id',{
                    'clientId': user.clientId,
                    'groupId': item.groupId 
                })
                    .then(r => {
                        setStatus('send-request')
                    })
                    .catch(e => {
                        setStatus('not-join')
                    })

            })
    // eslint-disable-next-line
    },[])

    useEffect(() => {
        if(onClick){
            if(status === 'joined')
                axios.post('http://127.0.0.1:5000/group-member-delete',{
                    'clientId': user.clientId,
                    'groupId': item.groupId
                })
                    .then(res=> {
                        console.log('success')
                        setStatus('not-join')
                    })
            else if(status === 'send-request')
                axios.post('http://127.0.0.1:5000/group-request-delete',{
                    'clientId': user.clientId,
                    'groupId': item.groupId
                })
                    .then(res => {
                        console.log('success')
                        setStatus('not-join')
                    })
            else
                axios.post('http://127.0.0.1:5000/group-request',{
                    'manguoidung': user.clientId,
                    'manhom': item.groupId
                })
                    .then(res=>{
                        console.log('success')
                        setStatus('send-request')
                    })
            setOnClick(false)
        }
    // eslint-disable-next-line
    },[onClick])



    const handleJoinGroup = () => {
        setOnClick(true)
        setIsJoined(!isJoined)
    }

    return (
        <div className='searchContentItemGroup'>
            <div className='searchContentItemGroupBox'>
                <Link to={`/group/${item.groupId}`} className='searchImg'>
                    <img src={`http://127.0.0.1:5000/img/${item.backgroundImg}`} alt='ptc' className='searchImgItem' />
                </Link>
                <Link to={`/group/${item.groupId}`} className='searchAuthor'>{item.name}</Link>
            </div>
            <div className='searchContentItemGroupBox'>
                {
                    status === 'joined' ? (
                        <button className='cancel' onClick={() => handleJoinGroup()}>Rời nhóm</button>
                    ) : status === 'send-request' ? (
                        <button className='cancel' onClick={() => handleJoinGroup()}>Hủy yêu cầu</button>
                    ) : (
                        <button onClick={() => handleJoinGroup()}>Tham gia</button>
                    )
                }
            </div>
        </div>
    )
}

export default SearchItem