import React from 'react'
import './user.scss'

const ImageUser = ({posts}) => {
  return (
    <div className='imageUser'>
        <h2>Ảnh</h2>

        <div className='imageUserContent'>
        {
          posts.map(item => {
            if(item.img !== '' && item.img !== null)
              return (
                <div key={item.postId} className='imageUserContentItem'>
                  <div className='imageUserContentItemBox'>
                    <img src={`http://127.0.0.1:5000/img/${item.img}`} alt='ptc' />
                  </div>
                </div>
              )
          })
        }
        </div>
    </div>
  )
}

export default ImageUser