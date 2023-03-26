import {useState,useEffect} from 'react'
import axios from 'axios'
import BlogClient from './BlogClient'
import './client.scss'
import FriendClient from './FriendClient'
import ImageClient from './ImageClient'
import { useParams } from 'react-router-dom'

function Client(){
    const pagrams = useParams('clientId')
    const [friends,setFriends] = useState([])
    const [client,setClient] = useState({})
    const [posts,setPosts] = useState([])

    useEffect(() => {
        axios.get(`http://127.0.0.1:5000/find-client/${pagrams.clientId}`)
            .then(res => {
                setClient(res.data)
            })

        axios.get(`http://127.0.0.1:5000/get-all-friend-by-client-id/${pagrams.clientId}`)
            .then(res => {
                setFriends(res.data)
            })

        axios.get(`http://127.0.0.1:5000/get-all-post-of-client/${pagrams.clientId}`)
            .then(res => {
                setPosts(res.data)
            })
    // eslint-disable-next-line
    },[])

    const [isClick,setIsClick] = useState('baiviet')
    return (
        <div className='client'>
            <div className='clientHeader'>
                <div className='clientHeaderItem'>
                    <div className='clientHeaderImg'>
                        <img src={`http://127.0.0.1:5000/img/${client.backgroundImg}`} alt='ptc' className='clientHeaderImgItem' />
                    </div>

                    <div className='clientHeaderInfo'>
                        <div className='clientHeaderInfoBox'>
                            <div className='clientHeaderInfoAvt'>
                                <img src={`http://127.0.0.1:5000/img/${client.avatar}`} alt='avt' className='clientHeaderInfoAvtItem' />
                                
                            </div>
                            <div className='clientHeaderInfoText'>
                                <h3>{client.name}</h3>
                                <span>{friends.length} bạn bè</span>
                            </div>
                        </div>

                        


                    </div>

                    <div className='clientHeaderLine'></div>

                    <div className='clientHeaderNav'>
                        <div className='clientHeaderNavItems'>
                            <div className={`clientHeaderNavItem ${isClick === 'baiviet' ? 'isClick' : ''}`} onClick={() => setIsClick('baiviet')}>Bài viết</div>
                            <div className={`clientHeaderNavItem ${isClick === 'banbe' ? 'isClick' : ''}`} onClick={() => setIsClick('banbe')}>Bạn bè</div>
                            <div className={`clientHeaderNavItem ${isClick === 'anh' ? 'isClick' : ''}`} onClick={() => setIsClick('anh')}>Ảnh</div>
                        </div>
                    </div>
                </div>
            </div>

            <div className='clientContent'>
                {
                    isClick === 'baiviet' ? <BlogClient setIsClick={setIsClick} friends={friends} posts={posts} client={client} /> : 
                    isClick === 'banbe' ? <FriendClient client={client} friends={friends} /> : <ImageClient posts={posts} />
                }
                
            </div>
        </div>
    )
}

export default Client