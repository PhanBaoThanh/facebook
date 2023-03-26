import React, { useContext,useState,useRef,useEffect } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import { PageContext } from '../../context/PageContext'
import './statusgroup.scss'
import Comment from '../Status/Comment'

const StatusGroup = ({changePost,group,item}) => {
  const {
    user
  } = useContext(PageContext)
  const [value,setValue] = useState('')
  const [onChangeComment,setOnChangeComment] = useState([])
  const [onChangeReaction,setOnChangeReaction] = useState([])
  const [reactions,setReactions] = useState([])
  const [comments,setComments] = useState([])
  const [client,setClient] = useState({})
  const [isSendComment,setIsSendComment] = useState(false)
  const [isClickLikeBtn,setIsClickLikeBtn] = useState(false)
  const [isLiked,setIsLiked] = useState(false)
  const [isOpen,setIsOpen] = useState(false)
  const [onChangePost,setOnChangePost] = useState('')
  const [isOpenModal,setIsOpenModal] = useState(false)
  const [nameImg,setNameImg] = useState('')
  const inputRef = useRef()
  const statusRef = useRef()
  const sttInputRef = useRef()

  useEffect(() => {
    axios.get(`http://127.0.0.1:5000/find-client/${item.clientId}`)
        .then(res => {
            setClient(res.data)
        })
  // eslint-disable-next-line
  },[])

  useEffect(() => {
      axios.get(`http://127.0.0.1:5000/find-client/${item.clientId}`)
          .then(res => {
              setClient(res.data)
          })

      axios(`http://127.0.0.1:5000/get-all-comment-by-post-id/${item.postId}`)
          .then(res => {
              setComments(res.data)
          })

      axios(`http://127.0.0.1:5000/get-all-reaction-by-post-id/${item.postId}`)
          .then(res => {
              setReactions(res.data)
              if(res.data.find(item => item.clientId === user.clientId))
                  setIsLiked(true)
          })
  // eslint-disable-next-line
  },[])

  useEffect(() => {
      if(onChangeComment === true)
          axios(`http://127.0.0.1:5000/get-all-comment-by-post-id/${item.postId}`)
              .then(res => {
                  setComments(res.data)
                  setOnChangeComment(false)
              })
              .catch(err => {
                  setOnChangeComment(false)
              })

      if(onChangeReaction === true)
          axios(`http://127.0.0.1:5000/get-all-reaction-by-post-id/${item.postId}`)
              .then(res => {
                  setReactions(res.data)
                  if(res.data.find(item => item.clientId === user.clientId))
                      setIsLiked(true)
                  setOnChangeReaction(false)
              })
              .catch(err => {
                  setOnChangeReaction(false)
              })

  // eslint-disable-next-line
  },[onChangeComment,onChangeReaction])

  useEffect(() => {
      if(isSendComment === true)
          axios.post('http://127.0.0.1:5000/comment',{
              'mabaidang': item.postId,
              'manguoidung': user.clientId,
              'noidung': value
          })
              .then(res => {
                  setIsSendComment(false)
                  setOnChangeComment(true)
                  setValue('')
              })
              .catch(err => {
                  setIsSendComment(false)
                  setValue('')
              })
  // eslint-disable-next-line
  },[isSendComment])

  useEffect(() => {
      if(isClickLikeBtn === true){
          if(isLiked)
              axios.post('http://127.0.0.1:5000/reaction-delete',{
                  'clientId': user.clientId,
                  'postId': item.postId
              })
                  .then(res => {
                      setIsClickLikeBtn(false)
                      setOnChangeReaction(true)
                      setIsLiked(false)
                  })
                  .catch(err => {
                      setIsClickLikeBtn(false)
                  })
          else
              axios.post('http://127.0.0.1:5000/reaction',{
                  'mabaidang': item.postId,
                  'manguoidung': user.clientId
              })
                  .then(res => {
                      setIsClickLikeBtn(false)
                      setOnChangeReaction(true)
                      setIsLiked(true)
                  })
                  .catch(err => {
                      setIsClickLikeBtn(false)
                  })
      }
  // eslint-disable-next-line
  },[isClickLikeBtn])

  useEffect(() => {
      if(onChangePost === 'delete')
          axios.delete(`http://127.0.0.1:5000/post/${item.postId}`)
              .then(res => {
                  setOnChangePost('')
                  changePost(true)
                  
              })
              .catch(err => {
                  setOnChangePost('')
              })
      else if(onChangePost === 'edit'){
          if(statusRef.current.files[0]){
              const formData = new FormData()
              formData.append('mabaidangnhom',item.postId)
              formData.append('noidung',sttInputRef.current.value)
              formData.append('image', statusRef.current.files[0], statusRef.current.files[0].name)
              axios.post('http://127.0.0.1:5000/post-update',formData,{headers: {'Content-Type': 'multipart/form-data' }})
                  .then(res => {
                      setOnChangePost(false)
                      changePost(true)

                  })
                  .catch(err => {
                      setOnChangePost(false)
                  })
          }
          else{
              axios.post('http://127.0.0.1:5000/post-update-no-img',{
                  'mabaidangnhom': item.postId,
                  'noidung': sttInputRef.current.value,
              })
                  .then(res => {
                      setOnChangePost(false)
                      changePost(true)

                  })
                  .catch(err => {
                      setOnChangePost(false)
                  })
          }
          
      }
  // eslint-disable-next-line
  },[onChangePost])

  const urlToObject= async()=> {
      const response = await fetch(`http://127.0.0.1:5000/img/${item.img}`);
      const blob = await response.blob();
      let list = new DataTransfer();
      let file = new File([blob], item.img, {type: blob.type})
      list.items.add(file);
      let myFileList = list.files;
      statusRef.current.files = myFileList
      setNameImg(item.img)
  }

  const handleClickEditBtn = () => {
      setIsOpenModal(true)
      if(item.img !== '' && item.img !== null)
          urlToObject()
      setIsOpen(false)
  }

  const handleClickDeleteBtn = () => {
      setOnChangePost('delete')
      setIsOpen(false)
  }

  const handleEditStatus = () => {
      setIsOpenModal(false)
      setOnChangePost('edit')
  }



  return (
    <>
            <div className='StatusGroup'>
                <div className='StatusGroupHeader'>
                    <div style={{display: 'flex'}}> 
                        <div className='btnCircle marginRight8'>
                            <img style={{borderRadius: '50%',width: '100%',height: '100%'}} src={`http://127.0.0.1:5000/img/${client.avatar}`} alt='' />
                        </div>
                        <div className='StatusGroupHeaderInfo'>
                            {
                                client.clientId === user.clientId ? (
                                    <Link to={`/myAccount`} className='StatusGroupHeaderInfoAuthor'>{client.name}</Link>

                                ) : (
                                    <Link to={`/client/${client.clientId}`} className='StatusGroupHeaderInfoAuthor'>{client.name}</Link>
                                )
                            }
                            <p className='StatusGroupHeaderInfoTime'>{`${new Date(item.createdAt.slice(1,-1)).getHours()}:${new Date(item.createdAt.slice(1,-1)).getMinutes()} ${new Date(item.createdAt.slice(1,-1)).getDate()}-${new Date(item.createdAt.slice(1,-1)).getMonth() + 1}-${new Date(item.createdAt.slice(1,-1)).getFullYear()}`}</p>
                        </div>
                    </div>

                    {
                        item.clientId === user.clientId && (
                            <div className='StatusGroupHeaderBtn' style={{display: 'flex',alignItems: 'center',justifyContent:'center',float: 'right'}}>
                                <div onClick={() => setIsOpen(!isOpen)} className='StatusGroupHeaderBtnAnimation' style={{padding: '8px',display: 'flex'}}>
                                    <svg fill="currentColor" viewBox="0 0 20 20" width="1em" height="1em" ><g fillRule="evenodd" transform="translate(-446 -350)"><path d="M458 360a2 2 0 1 1-4 0 2 2 0 0 1 4 0m6 0a2 2 0 1 1-4 0 2 2 0 0 1 4 0m-12 0a2 2 0 1 1-4 0 2 2 0 0 1 4 0"></path></g></svg>
                                </div>

                                {
                                    isOpen && (
                                        <div className='dropBox'>
                                            <button onClick={() => handleClickEditBtn()}>Chỉnh sửa bài viết</button>
                                            <button onClick={() => handleClickDeleteBtn()}>Xóa bài viết</button>
                                        </div>
                                    )
                                }
                                
                            </div>
                        )
                    }
                </div>
                {
                    item.content !== '' && item.content !== null && (
                        <div className='StatusGroupContent'>
                            <span>{item.content}</span>
                        </div>
                    )
                }
                
                {
                    item.img !== '' && item.img !== null && (
                        <div className='StatusGroupImg'>
                            <img className='StatusGroupImgItem' src={`http://127.0.0.1:5000/img/${item.img}`} alt=''/>
                        </div>
                    )
                }

                
                <div className='StatusGroupCount' style={{marginTop: '12px'}}>
                    <div className='StatusGroupCountLike'>
                    {
                        reactions.length !== 0 && (
                            <>
                                <img height="18" role="presentation" src="data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 16 16'%3e%3cdefs%3e%3clinearGradient id='a' x1='50%25' x2='50%25' y1='0%25' y2='100%25'%3e%3cstop offset='0%25' stop-color='%2318AFFF'/%3e%3cstop offset='100%25' stop-color='%230062DF'/%3e%3c/linearGradient%3e%3cfilter id='c' width='118.8%25' height='118.8%25' x='-9.4%25' y='-9.4%25' filterUnits='objectBoundingBox'%3e%3cfeGaussianBlur in='SourceAlpha' result='shadowBlurInner1' stdDeviation='1'/%3e%3cfeOffset dy='-1' in='shadowBlurInner1' result='shadowOffsetInner1'/%3e%3cfeComposite in='shadowOffsetInner1' in2='SourceAlpha' k2='-1' k3='1' operator='arithmetic' result='shadowInnerInner1'/%3e%3cfeColorMatrix in='shadowInnerInner1' values='0 0 0 0 0 0 0 0 0 0.299356041 0 0 0 0 0.681187726 0 0 0 0.3495684 0'/%3e%3c/filter%3e%3cpath id='b' d='M8 0a8 8 0 00-8 8 8 8 0 1016 0 8 8 0 00-8-8z'/%3e%3c/defs%3e%3cg fill='none'%3e%3cuse fill='url(%23a)' xlink:href='%23b'/%3e%3cuse fill='black' filter='url(%23c)' xlink:href='%23b'/%3e%3cpath fill='white' d='M12.162 7.338c.176.123.338.245.338.674 0 .43-.229.604-.474.725a.73.73 0 01.089.546c-.077.344-.392.611-.672.69.121.194.159.385.015.62-.185.295-.346.407-1.058.407H7.5c-.988 0-1.5-.546-1.5-1V7.665c0-1.23 1.467-2.275 1.467-3.13L7.361 3.47c-.005-.065.008-.224.058-.27.08-.079.301-.2.635-.2.218 0 .363.041.534.123.581.277.732.978.732 1.542 0 .271-.414 1.083-.47 1.364 0 0 .867-.192 1.879-.199 1.061-.006 1.749.19 1.749.842 0 .261-.219.523-.316.666zM3.6 7h.8a.6.6 0 01.6.6v3.8a.6.6 0 01-.6.6h-.8a.6.6 0 01-.6-.6V7.6a.6.6 0 01.6-.6z'/%3e%3c/g%3e%3c/svg%3e" alt='ptc' width="18"/>
                                <span>{reactions.length}</span>
                            </>
                        )
                    }
                    </div>
                    <div className='StatusGroupCountComment'>
                        {
                            comments.length !== 0 && `${comments.length} Bình luận`
                        }
                    </div>
                </div>

                <div style={{backgroundColor: '#4e4e4e',height: '1px',margin: '12px 0 4px'}}></div>
                <div className='StatusGroupIcon'>
                    <div className='StatusGroupIconItem' onClick={() => setIsClickLikeBtn(true)}>
                        <span>
                            <i className={`like ${isLiked && 'clicked'}`}></i>
                        </span>
                        <span className={`StatusGroupIconText ${isLiked && 'clickedLike'}`}>Thích</span>
                    </div>

                    <div className='StatusGroupIconItem' onClick={() => inputRef.current.focus()}>
                        <span>
                            <i className='comment'></i>
                        </span>
                        <span className='StatusGroupIconText'>Bình luận</span>
                    </div>

                </div>
                <div style={{backgroundColor: '#4e4e4e',height: '1px',margin: '4px 0'}}></div>

                <div className='StatusGroupComment'>
                    <div className='StatusGroupCommentUser'>
                        <div className='btnCircle marginRight8'>
                            <img style={{borderRadius: '50%',width: '100%',height: '100%'}} src={`http://127.0.0.1:5000/img/${user.avatar}`} alt='' />
                        </div>
                        <div className='StatusGroupCommentInput'>
                            <input onKeyDown={e => {if(value !== '' && value !== null && e.keyCode === 13) setIsSendComment(true)}} className='StatusGroupCommentInputItem' spellCheck='false' ref={inputRef} placeholder='Viết bình luận...' value={value} onChange={e => setValue(e.target.value)} />
                        </div>
                    </div>

                    {
                        comments.map(item => (
                            <Comment setOnChangeComment={setOnChangeComment} comment={item} key={item.commentId} />
                        ))
                    }

                    {/* <div className='statusCommentBtn'>Xem thêm bình luận</div> */}
                </div>
            </div>
            <div className='modalEditStatusGroup' style={isOpenModal ? {display: 'flex'}:{display: 'none'}}>
                <div className='StatusGroupEditContentStt'>
                    <div className='StatusGroupEditStt'>
                        <h2 style={{textAlign: 'center',margin: '8px 0'}}>Chỉnh sửa bài viết</h2>
                        <div className='StatusGroupEditSttHeader'>
                            <div className='StatusGroupEditSttInput'>
                                <textarea style={{resize: 'none'}} rows={3} ref={sttInputRef} className='StatusGroupEditSttInputItem' placeholder='Viết bình luận...' defaultValue={item.content} />
                            </div>
                        </div>
                        <div className='StatusGroupEditSttImg'>
                            <label onClick={() => setNameImg('')} htmlFor={`nameStatusGroupChange${item.postId}`}>
                                <img src="https://static.xx.fbcdn.net/rsrc.php/v3/yC/r/a6OjkIIE-R0.png" alt="" style={{height: '24px', width: '24px'}}/>
                                <span style={{marginLeft: '8px'}}>Ảnh</span>
                                <input ref={statusRef} type='file' onChange={e => setNameImg(e.target.files[0].name)} accept="image/png, image/gif, image/jpeg" id={`nameStatusGroupChange${item.postId}`} name={`nameStatusGroupChange${item.postId}`}/>
                            </label>
                            <span className='nameImg'>{nameImg}</span>
                        </div>
                        <>
                            <button className='StatusGroupEditSttBtn' onClick={() => handleEditStatus()}>Lưu</button>
                            <button className='StatusGroupEditSttBtn' style={{backgroundColor: '#3a3b3c'}} onClick={() => {setIsOpenModal(false);sttInputRef.current.value = item.content;statusRef.current.files[0] = null}}>Hủy</button>
                        </>
                    </div>
                </div>
            </div>
        </>
  )
}

export default StatusGroup