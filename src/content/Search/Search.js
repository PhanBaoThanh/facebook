import {useContext, useState,useEffect} from 'react'
import axios from 'axios'
import { PageContext } from '../../context/PageContext'
import './search.scss'
import SearchFriendItem from './SearchFriendItem'
import SearchItem from './SearchItem'

function Search(){
    const user = JSON.parse(localStorage.getItem('user')) ?? []
    const [value,setValue] = useState('all')
    const [clients,setClients] = useState([])
    const [groups,setGroups] = useState([])
    const {
        searchValue
    } = useContext(PageContext)

    useEffect(() => {
        if(searchValue !== '' && searchValue!== null){
            axios.post('http://127.0.0.1:5000/client-search',{
                'key': searchValue,
                'clientId': user.clientId
            })
                .then(res => {
                    setClients(res.data)
                })
                .catch(err => {
                    console.log('loi')
                })

            axios.post('http://127.0.0.1:5000/group-search',{
                'key': searchValue
            })
                .then(res => {
                    setGroups(res.data)
                })
                .catch(err => {
                    console.log('err')
                })
        }
    // eslint-disable-next-line
    },[searchValue])

    return (
        <div className='searchPage'>
            <div className='searchNav'>
                <div className='searchNavItems'>

                    <h1>Kết quả tìm kiếm cho</h1>
                    <p className='searchNavItemsText'>{searchValue}</p>
                    <div className='line'></div>

                    <p className='searchNavItemsTitle'>Bộ lọc</p>

                    <button onClick={() => setValue('all')} className={`searchNavItem ${value === 'all' && 'active'}`}>
                        <div className='btnIcon marginRight8' style={ value==='all' ? {backgroundColor: '#1877f2'} : {backgroundColor: '#3a3b3c'}}>
                            <i className='btnIconImgSearchAll'></i>
                        </div>
                        <p>Tất cả</p>
                    </button>

                    <button onClick={() => setValue('friend')} className={`searchNavItem ${value==='friend' && 'active'}`}>
                        <div className='btnIcon marginRight8' style={value === 'friend' ? {backgroundColor: '#1877f2'} : {backgroundColor: '#3a3b3c'}}>
                            <i className='btnIconImgSearchFriend'></i>
                        </div>
                        <p>Mọi người</p>
                    </button>

                    <button onClick={() => setValue('group')} className={`searchNavItem ${value==='group' && 'active'}`}>
                    <div className='btnIcon marginRight8' style={value  === 'group' ? {backgroundColor: '#1877f2'} : {backgroundColor: '#3a3b3c'}}>
                            <i className='btnIconImgSearchGroup'></i>
                        </div>
                        <p>Nhóm</p>
                    </button>
                </div>
            </div>
            
            <div className='searchContent'>
                {
                    (value === 'all' || value === 'friend') && 
                    clients.map(item => (
                        <SearchFriendItem key={item.clientId} item={item} />
                    ))
                }
                
                {
                    (value ==='all' || value ==='group') && (
                        <div className='searchContentItem'>
                            <h3>Nhóm</h3>
                            {
                                groups.map(item => (
                                    <SearchItem item={item} key={item.groupId} />
                                ))
                            }
                        </div>
                    )
                }
                
                
            </div>
        </div>
    )
}

export default Search