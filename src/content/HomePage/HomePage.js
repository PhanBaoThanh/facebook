import {useState,useEffect,useRef, useContext} from 'react'
import { Link } from 'react-router-dom'
import Status from '../Status/Status'
import axios from 'axios'
import './homepage.scss'
import { PageContext } from '../../context/PageContext'
function HomePage(){
    const {
        user
    } = useContext(PageContext)
    const [value,setValue] = useState('')
    const [nameImg,setNameImg] = useState('')
    const [groups,setGroups] = useState([])
    const [posts,setPosts] = useState([])
    const [onChange,setOnChange] = useState(false)
    const [onChangePost,setOnChangePost] = useState(false)
    const [friends,setFriends] = useState([])
    const sttRef = useRef()

    useEffect(() => {
        axios.get(`http://127.0.0.1:5000/get-all-friend-by-client-id/${user.clientId}`)
        .then(res => {
            setFriends(res.data)
        })
        .catch(err => {
            console.log('loi1')
        })

        axios.get(`http://127.0.0.1:5000/get-all-group-by-client-id/${user.clientId}`)
            .then(res => {
                setGroups(res.data)
            })
            .catch(err => {
                console.log('loi2')
            })
    },[])

    useEffect(() => {
        if(onChangePost === true)
            axios.get(`http://127.0.0.1:5000/get-all-post-of-client/${user.clientId}`)
                .then(res => {
                    setPosts(res.data)
                    setOnChangePost(false)
                })
                .catch(err => {
                    console.log('loi3')
                    setOnChangePost(false)
                })
    },[onChangePost])

    useEffect(() => {
        if(onChange === true){
            if(sttRef.current.files[0]){
                const formData = new FormData()
                formData.append('manhom',null)
                formData.append('manguoidung',user.clientId)
                formData.append('noidung',value)
                if(sttRef.current.files[0])
                    formData.append('image', sttRef.current.files[0], sttRef.current.files[0].name)
                else
                    formData.append('image','')
                axios.post('http://127.0.0.1:5000/post',formData, {headers: {'Content-Type': 'multipart/form-data' }})
                    .then(res => {
                        setValue('')
                        setNameImg('')
                        sttRef.current.value = null
                        setOnChangePost(true)
                        setOnChange(false)
                    }
                    )
                    .catch(err => {
                        setValue('')
                        sttRef.current.value = null
                        setNameImg('')
                        setOnChange(false)
                    })
            }
            else
                axios.post('http://127.0.0.1:5000/post-no-img',{
                    'manhom': null,
                    'manguoidung': user.clientId,
                    'noidung': value
                })
                    .then(res=> {
                        setValue('')
                        setNameImg('')
                        sttRef.current.value = null
                        setOnChangePost(true)
                        setOnChange(false)
                    })
                    .catch(err => {
                        setValue('')
                        setOnChange(false)
                        setNameImg('')
                        sttRef.current.value = null
                    })
        }
    },[onChange])

    const handleUpPost = () => {
        if((value !== '' && value !== null) || (sttRef.current.files[0] !== undefined && sttRef.current.files[0] !== null))
            setOnChange(true)
    }

    return (
        <div className='homepage'>
            <div className='homepageNav'>
                <div className='homepageNavItems'>
                    <Link to='/myAccount' className='homepageNavItem'>
                        <div className='btnCircle marginRight8'>
                            <img style={{borderRadius: '50%',width: '100%',height: '100%'}} src={`http://127.0.0.1:5000/img/${user.avatar}`} alt='' />
                        </div>
                        <p>{user.name}</p>
                    </Link>

                    <Link to='/friend' className='homepageNavItem'>
                        <div className='btnIcon marginRight8' style={{backgroundColor: 'transparent'}}>
                            <i className='btnIconImgFriend'></i>
                        </div>
                        <p>Bạn bè</p>
                    </Link>

                    <Link to='/groups' className='homepageNavItem'>
                        <div className='btnIcon marginRight8' style={{backgroundColor: 'transparent'}}>
                            <i className='btnIconImgGroup'></i>
                        </div>
                        <p>Nhóm</p>
                    </Link>

                    <div className='homepageNavLine'></div>
                    <p style={{margin: '12px 0',paddingLeft: '8px',fontSize: '16px',opacity: '.8',cursor: 'default',userSelect: 'none'}}>Lối tắt của bạn</p>

                    {
                        groups.map(item => (
                            <Link to={`/group/${item.groupId}`} className='homepageNavItem' key={item.groupId}>
                                <div className='btnCircle marginRight8'>
                                    <img style={{borderRadius: '8px',width: '100%',height: '100%'}} src={`http://127.0.0.1:5000/img/${item.backgroundImg}`} alt='' />
                                </div>
                                <p className='homepageNavText textLimit'>{item.name}</p>
                            </Link>
                        ))
                    }         
                </div>
            </div>
            
            <div className='homepageContent'>
                <div className='homepageContents'>
                    <div className='homepageUserStt'>
                        <h2 style={{textAlign: 'center',margin: '8px 0'}}>Tạo bài viết</h2>
                        <div className='UserSttHeader'>
                            <div className='btnCircle marginRight8'>
                                <img style={{borderRadius: '50%',width: '100%',height: '100%'}} src={`http://127.0.0.1:5000/img/${user.avatar}`} alt='' />
                            </div>
                            <div className='userSttInput'>
                                <input className='userSttInputItem' placeholder='Viết bình luận...' value={value} onChange={e => setValue(e.target.value)} />
                            </div>
                        </div>
                        <div className='UserSttImg'>
                            <label onClick={() => setNameImg('')} htmlFor='imgStt'>
                                <img src="https://static.xx.fbcdn.net/rsrc.php/v3/yC/r/a6OjkIIE-R0.png" alt="" style={{height: '24px', width: '24px'}}/>
                                <span style={{marginLeft: '8px'}}>Ảnh</span>
                                <input ref={sttRef} type='file' onChange={e => setNameImg(e.target.files[0].name)} accept="image/png, image/gif, image/jpeg" id='imgStt' name='imgStt'  />
                            </label>
                            <span className='nameImg'>{nameImg}</span>


                        </div>
                        <div onClick={() => handleUpPost()} className='UserSttBtn'>Đăng</div>
                    </div>
                    {/* <Status authorImg='' author='' content='aslkdjflkajsdlkfjsakdjflkjasdlasdfasddfadfasdafsdfasdfdfasdfasdfasdfasdfasdfasdfkjflkasjlkfjlksajfdlkjsalkjflkjaslkfjlksjflkjaskjflkjaslkdfjlkasjdfkjsakajdlkfjasdjfl;ajsdlkfjalksdjflkaj;sdfjalksdjflkasdjfkadjsflkjasdlkfjfasjdklfja;sdjflk;ajsdf;jaklsdjflkas;dklfaaj;dkslkjflkajsdfka' img='' />
                    <Status authorImg='' author='' content='aslkddfadsfasdfasdfasdfasfasdfadjfklajskdjfakjsjfk;lasjfkajsfl;kasj;dflksdfasdfasdfdasdfasdsajfdlkjsalkjflkjaslkfjlksjflkjaskjflkjaslkdfjlkasjdfkjsakajdlkfjasdjfl;ajsdlkfjalksdjflkaj;sdfjalksdjflkasdjfkadjsflkjasdlkfjfasjdklfja;sdjflk;ajsdf;jaklsdjflkas;dklfaaj;dkslkjflkajsdfka' img='' />
                    <Status authorImg='' author='' content='aslkdjflkajsdlkfjsakdjflkjasdlasdfasddfadfasdafsdfasdfdfasdfasdfasdfasdfasdfasdfkjflkasjlkfjlksajfdlkjsalkjflkjaslkfjlksjflkjaskjflkjaslkdfjlkasjdfkjsakajdlkfjasdjfl;ajsdlkfjalksdjflkaj;sdfjalksdjflkasdjfkadjsflkjasdlkfjfasjdklfja;sdjflk;ajsdf;jaklsdjflkas;dklfaaj;dkslajdlkfjalksjdflkajsdlkfja;sdkfjlkasjdflkajslkdfjaslkfdjkjflkajsdfka' img='' /> */}
                </div>
            </div>

            <div className='homepageFriend'>
                <p>Người liên hệ</p>
                <div className='homepageFriends'>
                {
                    friends.map(item => (
                        <div className='homepageFriendItem' key={item.clientId}>
                            <div className='btnCircle marginRight8'>
                                <img style={{borderRadius: '50%',width: '100%',height: '100%'}} src={`http://127.0.0.1:5000/img/${item.avatar}`} alt='' />
                            </div>
                            <p className='homepageFriendText textLimit'>{item.name}</p>
                        </div>
                    ))
                }
                    
                </div>
            </div>
        </div>
    )
}

export default HomePage