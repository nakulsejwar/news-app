import React, { useEffect, useState } from "react";
import axios from "axios";

const App = () => {
  const [stories, setStories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/hackernews/")
      .then((response) => {
        setStories(response.data);
        setLoading(false);
      })
      .catch((err) => {
        setError("Failed to fetch stories");
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading stories...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Top 10 HackerNews Stories</h1>
      <ul style={{ listStyle: "none", padding: 0 }}>
        {stories.map((story, index) => (
          <li key={index} style={{ marginBottom: "10px" }}>
            <a href={story.url} target="_blank" rel="noopener noreferrer">
              <strong>{story.title}</strong>
            </a>
            <p>By {story.author} | Score: {story.score} | Time: {story.time}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
