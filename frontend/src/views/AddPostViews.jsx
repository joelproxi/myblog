import axios from 'axios'
import React, { useState } from 'react'


const url = 'http://127.0.0.1:8000/api/blog/posts/'

const AddPostViews = () => {
    
    const [title, setTitle] = useState('')
    const [body, setBody] = useState('')
    const [success, setSuccess] = useState(false)
    const [error, setError] = useState(false)

    const handleSubmit = async e => {
        const data = {
            "title": title,
            "body": body,
            "category": 1,
            "author": 1,
           
        }

        try {
            const resp = await axios.post(url, data);
            if( resp.status === 201){
                setSuccess(true)
                setError(false)
                
            }
            console.log(resp);
        } catch (error) {
            console.error(error);
            setError(true)
            setSuccess(false)
        }
        // console.log(data)
    }
  return (
    <React.Fragment>
        <h3>Ajouter une publication</h3>
        {
            success ?   <span> Le post a ete cree   </span> : <span></span>
        }
         {
            error ?   <span> Le post n'a ete cree   </span> : <span></span>
        }
      
        <form >
            <input type="text" onChange={e => setTitle(e.target.value)} placeholder='Titre de la publication'  />
            <br />
            <textarea onChange={e => setBody(e.target.value)} cols="30" rows="10" placeholder='Contenu de la publication' ></textarea>
        </form>
        <br />
        <button  onClick={ handleSubmit} type="button">Ajouter</button>
    </React.Fragment>
  )
}

export default AddPostViews