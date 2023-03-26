import axios from 'axios'
import React, { useState,useEffect } from 'react'
import { Link } from 'react-router-dom'
import './search.scss'

//friend
//friend-request
//friend-response
//not-friend
const SearchFriendItem = ({item}) => {
    const user = JSON.parse(localStorage.getItem('user')) ?? []
    const [isFriend,setIsFriend] = useState(false)
    const [stt,setStt] = useState('not-friend')
    const [onClick,setOnClick] = useState(false)
    const [isDelete,setIsDelete] = useState(false)

    useEffect(() => {
        axios.post('http://127.0.0.1:5000/find-friend-by-client-id',{
            'client1': user.clientId,
            'client2': item.clientId
        })
            .then(res => {
                setStt('friend')
            })
            .catch(err => {
                axios.post('http://127.0.0.1:5000/find-friend-request-by-client-id',{
                    'client1': user.clientId,
                    'client2': item.clientId
                })
                    .then(res => {
                        if(res.data.senderId === user.clientId)
                            setStt('friend-request')
                        else
                            setStt('friend-response')
                    })
                    .catch(e => {
                        setStt('not-friend')
                    })
            })

    // eslint-disable-next-line
    },[])

    useEffect(() => {
        if(onClick){
            if(stt === 'friend')
                axios.post('http://127.0.0.1:5000/friend-delete',{
                    'client1': user.clientId,
                    'client2': item.clientId
                })
                    .then(res => {
                        console.log('success')
                        setStt('not-friend')
                    })
            else if(stt === 'friend-request')
                axios.post('http://127.0.0.1:5000/friend-request-delete',{
                    'senderId': user.clientId,
                    'receiverId': item.clientId
                })
                    .then(res => {
                        console.log('success')
                        setStt('not-friend')
                    })
            else if(stt === 'friend-response'){
                if(isDelete)
                    axios.post('http://127.0.0.1:5000/friend-response-delete',{
                        'receiverId': user.clientId,
                        'senderId': item.clientId
                    })
                        .then(res => {
                            console.log('success')
                            setStt('not-friend')
                            setIsDelete(false)
                        })
                else
                    axios.post('http://127.0.0.1:5000/friend-request-confirm',{
                        'receiverId': user.clientId,
                        'senderId': item.clientId
                    })
                        .then(res => {
                            console.log('success')
                            setStt('friend')
                        })
            }
                
            else
                axios.post('http://127.0.0.1:5000/friend-request',{
                    'nguoigui': user.clientId,
                    'nguoinhan': item.clientId
                })
                    .then(res => {
                        console.log('success')
                        setStt('friend-request')
                    })

            setOnClick(false)
        }
    // eslint-disable-next-line
    },[onClick])

    const handleClickAddFriend = (value) => {
        setIsFriend(!isFriend)
        setOnClick(true)
        setIsDelete(value)
    }

    return (
        <div className='searchContentItem'>
            <div className='searchContentItemFriend'>
                <div className='searchContentItemFriendBox'>
                    <Link to={`/client/${item.clientId}`} className='searchImgFriend'>
                        <img src={`http://127.0.0.1:5000/img/${item.avatar}`} alt='ptc' className='searchImgFriendItem' />
                    </Link>
                    <Link to={`/client/${item.clientId}`} className='searchAuthor'>{item.name}</Link>
                </div>
                <div className='searchContentItemFriendBox'>
                {
                    stt === 'friend' ? (
                        <button className='cancel' onClick={() => handleClickAddFriend(false)}>Xóa bạn</button>
                    ) : stt === 'friend-request' ? (
                        <button className='cancel' onClick={() => handleClickAddFriend(false)}>Hủy yêu cầu</button>
                    ) : stt === 'friend-response' ? (
                        <>
                            <button style={{marginRight: '8px'}} onClick={() => handleClickAddFriend(false)}>Xác nhận</button>
                            <button className='cancel' onClick={() => handleClickAddFriend(true)}>Xóa</button>
                        </>
                    ) : (
                        <button onClick={() => handleClickAddFriend(false)}>Thêm bạn bè</button>
                    )
                }
                </div>
            </div>
        </div>
    )
}

export default SearchFriendItem