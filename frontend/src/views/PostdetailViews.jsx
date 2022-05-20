import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'

const PostdetailViews = () => {
    const url = 'http://127.0.0.1:8000/api/blog/posts/'
    const [post, setPost] = useState({})

    const {id} = useParams()
    const getPostDetail =  async id => {
        try {
            let resp = await axios.get(url+id);
            if (resp.status === 200){
                console.log(resp.data);
                setPost(resp.data)
            }
        } catch (error) {
            console.error(error);
        }
    }

    useEffect(() => {
      getPostDetail(id)
    
    }, [id])
    
  return (
    <div>
        <h3>{post.title}</h3>
        <p>{post.body}</p>
        <footer>By {post.author}- since {post.created}</footer>
    </div>
  )
}

export default PostdetailViews