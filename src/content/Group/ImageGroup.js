import React from 'react'

const ImageGroup = ({posts}) => {
  return (
    <div className='imageGroup'>
        <h2>Ảnh</h2>

        <div className='imageGroupContent'>
          {
            posts.map(item => {
              if(item.img !== '' && item.img !== null)
                return (
                  <div className='imageGroupContentItem' key={item.postId}>
                    <div className='imageGroupContentItemBox'>
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

export default ImageGroup