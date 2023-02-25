import React from "react";
import axios from "axios";
import { useEffect } from "react";
import { useState } from "react";

import { Link } from "react-router-dom";

const url = "http://127.0.0.1:8000/api/blog/posts/";

const HomeViews = () => {
  const [posts, setPosts] = useState([]);
  async function getPostList() {
    try {
      let resp = await axios.get(url);
      if (resp.status === 200) {
        let data = await resp.data;
        setPosts((posts) => [...data]);
        console.log(posts);
      }
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    getPostList();

    //   return () => {
    //     second
    //   }
  }, []);

  return (
    <div>
      <h2>Liste des posts</h2>
      <br />
      {posts?.map((post) => {
        return (
          <div key={post.id}>
            <Link to={`post/${post.id}`}>
              <h3>{post.title}</h3>
            </Link>
            <p>{post.body}</p>
            <hr />
            <br />
          </div>
        );
      })}
    </div>
  );
};

export default HomeViews;
